"""tests for context manager"""
import pytest
from cookbook.context_managers.logging_context import LoggingContextManager
# pylint: disable=missing-function-docstring


class TestContextManager:

    @pytest.fixture(autouse=True)
    def logging_ctx(self):
        return LoggingContextManager()

    def test_one(self, logging_ctx):
        with logging_ctx as logger:
            pass
