from datetime import datetime
import pandas as pd
from app.crud.category import CATEGORY
from app.crud.title import TITLE
from app.crud.transactions import TRANSACTION
from app.utils.enums import PaymentMehtod


class ImportBase:
    def __init__(self):
        self.day_first = True
        self.date_format = "%d/%m/%Y"

    # DO NOT OVERWRITE THIS METHOD
    async def parse_data(self, df: pd.DataFrame, exclude_dependencies: bool):
        df = self.rename_columns(df)
        df["origin"] = "nubank"
        df["amount"] = self.parse_amount(df)
        df["id_legacy"] = self.parse_id_legacy(df)
        df["date"] = self.parse_date(df)
        df["payment_method"] = self.parse_payment_method(df)
        df["description"] = self.parse_description(df)
        # populating dependencies
        self.transactions_id_legacy = [
            id.id_legacy for id in await TRANSACTION.get_many_by_id_legacy(set(df["id_legacy"].to_list()))
        ]
        df["is_duplicated"] = df["id_legacy"].apply(self.check_duplicates)
        if not exclude_dependencies:
            await self.get_dependencies(set(df["description"].to_list()))
            df["title"] = df["description"].apply(self.get_title)
            df["category"] = df["description"].apply(self.get_category)

        df.drop_duplicates(subset="id_legacy", keep=False, inplace=True)
        return df

    async def get_dependencies(self, descriptions):
        self.categories = await CATEGORY.get_many_by_description(descriptions) or []
        self.titles = await TITLE.get_many_by_description(descriptions) or []

    def rename_columns(self, df: pd.DataFrame):
        raise NotImplementedError

    def parse_payment_method(self, df: pd.DataFrame):
        raise NotImplementedError

    def parse_amount(self, df: pd.DataFrame):
        return df["amount"].astype(float)

    def parse_id_legacy(self, df: pd.DataFrame):
        return df["id_legacy"].astype(str)

    def parse_date(self, df: pd.DataFrame):
        return df["date"].apply(lambda x: datetime.strptime(x, self.date_format).date())

    def parse_description(self, df: pd.DataFrame):
        return df["description"].astype(str)

    def get_title(self, description: str):
        return next(
            ({"id": title.id, "name": title.name} for title in self.titles if description in title.descriptions),
            None,
        )

    def get_category(self, description: str):
        return next(
            (
                {"id": category.id, "name": category.name}
                for category in self.categories
                if description in category.descriptions
            ),
            None,
        )

    def check_duplicates(self, id_legacy: str):
        return id_legacy in self.transactions_id_legacy


class NubankFile(ImportBase):
    def __init__(self):
        super().__init__()

    def rename_columns(self, df: pd.DataFrame):
        return df.rename(
            columns={
                "Valor": "amount",
                "Identificador": "id_legacy",
                "Data": "date",
                "Descrição": "description",
            },
            inplace=False,
        )

    def parse_payment_method(self, df: pd.DataFrame):
        return df["description"].apply(self.get_payment_method)

    def parse_description(self, df: pd.DataFrame):
        return df["description"].apply(self.get_description)

    def get_payment_method(self, description: str):
        method = description.split("-")[0].lower().strip()
        match method:
            case "compra no débito" | "pagamento da fatura" | "recarga de celular" | "débito em conta":
                return PaymentMehtod.DEBIT.value
            case "ajuste de compra no débito" | "crédito em conta" | "estorno":
                return PaymentMehtod.CHARGEBACK.value
            case "transferência recebida" | "transferência enviada":
                return PaymentMehtod.TRANSFER.value
            case "transferência enviada pelo pix" | "transferência recebida pelo pix":
                return PaymentMehtod.PIX.value
            case "pagamento de boleto efetuado":
                return PaymentMehtod.BANK_SLIP.value
            case "contratação de limite adicional" | "resgate de limite adicional":
                return PaymentMehtod.CREDIT_CARD_LIMIT.value
            case "ajuste (nubank)":
                return f"{PaymentMehtod.ADJUSTMENT.value} - NUBANK"
            case _:
                raise Exception(method)

    def get_description(self, description: str):
        _description = " ".join(description.split("-")[1:])
        return " ".join(_description.split()).strip() or description
