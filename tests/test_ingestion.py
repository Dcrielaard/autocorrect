" This file tests the ingestion module from the vocabulair "

from autocorrect.ingestion import Vocabulair

test_words = ["A", "B", "A", "C"]


def test_initialization() -> None:
    """
    Asserts if the initialized class is an instance of Vocabulair.
    """
    assert isinstance(Vocabulair(test_words), Vocabulair)
