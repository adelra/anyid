import string
import pytest
from anyid import random_sequence


def test_random_sequence_length():
    length = 12
    seq = random_sequence(length=length)
    assert len(seq) == length


def test_random_sequence_alphabet():
    length = 50
    alphabet = "abc"
    seq = random_sequence(length=length, alphabet=alphabet)
    assert len(seq) == length
    assert all(c in alphabet for c in seq)


def test_random_sequence_default_alphabet():
    length = 100
    seq = random_sequence(length=length)
    default_alphabet = string.ascii_letters + string.digits
    assert all(c in default_alphabet for c in seq)
    # Ensure it's not just digits or just letters (statistically probable for length 100)
    # This is a bit flaky but highly unlikely to fail if logic is correct
    assert any(c in string.digits for c in seq)
    assert any(c in string.ascii_letters for c in seq)


def test_random_sequence_invalid_length():
    with pytest.raises(ValueError, match="Length must be non-negative"):
        random_sequence(length=-1)


def test_random_sequence_empty_alphabet():
    with pytest.raises(ValueError, match="Alphabet must not be empty"):
        random_sequence(length=10, alphabet="")
