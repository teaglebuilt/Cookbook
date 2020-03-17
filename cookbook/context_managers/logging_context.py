"""
   logging_context.py
   -------------
   Basic example of a context manager.
"""


class LoggingContextManager:
    """Context Manager Class"""

    def __enter__(self):
        print("LoggingContextManager.__enter__()")
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"LoggingContextManager.__exit__({exc_type}-{exc_val}-{exc_tb})")
        return


__test__ = {
    'LoggingContextManager': '''
        >>> with LoggingContextManager() as x:
        ...     print(x)
        ... 
        LoggingContextManager.__enter__()
        None
        LoggingContextManager.__exit__(None-None-None)
    '''
}

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
