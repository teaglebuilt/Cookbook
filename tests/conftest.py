"""Shared Fixtures"""
# pylint: disable=missing-function-docstring
import pytest
from cookbook.context_managers.logging_context import LoggingContextManager


@pytest.fixture
def logging_ctx():
    return LoggingContextManager()
