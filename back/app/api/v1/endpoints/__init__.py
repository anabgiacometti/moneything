"""
Application endpoints.
For better organization, each endpoint should have a named file.
Each file must have a router, and each router must be registered here.
"""

from fastapi import APIRouter

from .login import router as login
from .transactions import router as transactions
from .import_csv import router as import_csv
from .title import router as title
from .category import router as category

router = APIRouter()
router.include_router(login, tags=["Login"])
router.include_router(transactions, prefix="/transaction", tags=["Transaction"])
router.include_router(import_csv, prefix="/import_csv", tags=["Import CSV"])
router.include_router(title, prefix="/title", tags=["Title"])
router.include_router(category, prefix="/category", tags=["Category"])
