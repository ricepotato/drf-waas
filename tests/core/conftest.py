# in conftest.py
def pytest_collection_modifyitems(items):
    for item in items:
        item.add_marker("all")