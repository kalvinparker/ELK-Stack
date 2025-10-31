# tests/test_app.py

import pytest
from app.main import app

def test_app_import():
    """
    A simple test to ensure the FastAPI application object can be imported.
    This acts as a basic sanity check.
    """
    assert app is not None