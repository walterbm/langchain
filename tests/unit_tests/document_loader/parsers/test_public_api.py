from langchain.document_loaders.parsers import __all__


def test_parsers_public_api_correct() -> None:
    """Test public API of parsers for breaking changes."""
    assert set(__all__) == {
        "PyPDFParser",
        "PDFMinerParser",
        "PyMuPDFParser",
        "PyPDFium2Parser",
    }
