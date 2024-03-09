import pytest
from rest_framework.test import APIClient
# in conftest.py
def pytest_collection_modifyitems(items):
    for item in items:
        item.add_marker("all")


@pytest.fixture
def api_client():
    return APIClient()