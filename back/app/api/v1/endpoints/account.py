from fastapi import APIRouter

from app.api.v1.utils.decorators import login_required


router = APIRouter()


@router.get("/")
@login_required
async def get_accounts():
    # TODO: get all accounts data
    ...


@router.pots("/")
@login_required
async def add_account():
    # TODO: add a new account
    ...


@router.delete("/")
@login_required
async def remove_account():
    # TODO: remove account
    ...


@router.put("/")
@login_required
async def update_account():
    # TODO: update account data
    ...
