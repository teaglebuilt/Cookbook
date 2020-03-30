


class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass # pylint: disable=unnecessary-pass

    def extract_text(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file."""
        pass # pylint: disable=unnecessary-pass


class PdfParser(InformalParserInterface):
    """ concrete class """
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass # pylint: disable=unnecessary-pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides InformalParserInterface.extract_text()"""
        pass # pylint: disable=unnecessary-pass


class EmailParser(InformalParserInterface):
    """Extract text from an email"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass # pylint: disable=unnecessary-pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override InformalParserInterface.extract_text()
        """
        pass # pylint: disable=unnecessary-pass


__test__ = {
    'InformalPartialInterface': '''
        >>> issubclass(PdfParser, InformalParserInterface)
        True
        >>> issubclass(EmailParser, InformalParserInterface)
        True
    '''
}

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
