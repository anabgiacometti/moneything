from typing import List
from fastapi import UploadFile
import pandas as pd
from app.crud.transactions import TRANSACTION

from app.utils.import_file import NubankFile


FILE = {"nubank": NubankFile()}


class CVSImport:
    def __init__(self, origin: str, files: List[UploadFile]) -> None:
        self.origin = origin
        self.files = files

    def buid_df(self):
        dfs = [pd.read_csv(file.file) for file in self.files]
        return pd.concat(dfs, axis=0, ignore_index=True)

    def validate_files(self):
        for file in self.files:
            assert file.content_type == "text/csv"

    async def get_data(self, exclude_dependencies=False):
        self.validate_files()
        file_mapper = FILE[self.origin]
        df = self.buid_df()
        return await file_mapper.parse_data(df, exclude_dependencies)

    async def get_preview(self):
        df = await self.get_data()
        return {
            "origin": self.origin,
            "preview": df.to_dict(orient="records"),
            "no_category": set(df[df.category.isnull()]["description"].to_list()),
            "no_title": set(df[df.title.isnull()]["description"].to_list()),
        }

    async def save(self, on_duplicate: str):
        df = await self.get_data(exclude_dependencies=True)
        updating_rows, inserting_rows = await self.prepare_data(df, on_duplicate=on_duplicate)
        if updating_rows:
            await TRANSACTION.update_from_csv(updating_rows)
        if inserting_rows:
            await TRANSACTION.create_from_csv(inserting_rows)
        return len(inserting_rows) + len(updating_rows)

    async def prepare_data(self, df: pd.DataFrame, on_duplicate: str):
        df.rename(
            columns={"id_legacy": "_id_legacy"},
            inplace=False,
        )
        inserting_rows = df[df.is_duplicated == False]
        inserting_rows = inserting_rows.drop("is_duplicated", axis=1)
        inserting_rows = inserting_rows.to_dict(orient="records")

        if on_duplicate == "update":
            updating_rows = df[df.is_duplicated == True]
            updating_rows = updating_rows.drop("is_duplicated", axis=1)
            updating_rows = updating_rows.to_dict(orient="records")
        elif on_duplicate == "exclude":
            updating_rows = []

        return updating_rows, inserting_rows
