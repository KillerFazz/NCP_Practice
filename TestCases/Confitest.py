import pytest

def pytest_configure(config):
    config._metadata["Project name"] = "Nop Commerce"
    config._metadata["Module Name"] = "Customers"
    config._metadata["Tester"] = 'Shaik'