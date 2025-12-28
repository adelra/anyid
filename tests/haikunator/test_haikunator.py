"""
Tests for the Haikunator generator.
"""

from hypothesis import given, strategies as st

from anyid.haikunator import haikunator
from anyid.haikunator.generator import HaikunatorGenerator
from anyid.haikunator.data import ADJECTIVES, NOUNS


def test_haikunator_generator_defaults():
    """
    Tests that the HaikunatorGenerator returns a valid haikunator with defaults.
    """
    generator = HaikunatorGenerator()
    generated = generator.generate()
    assert isinstance(generated, str)
    parts = generated.split("-")
    assert len(parts) == 3
    assert parts[0] in ADJECTIVES
    assert parts[1] in NOUNS
    assert parts[2].isdigit()
    assert 0 <= int(parts[2]) < 10000


def test_haikunator_generator_custom_range():
    """
    Tests that the HaikunatorGenerator respects the token range.
    """
    generator = HaikunatorGenerator()
    # Small range
    generated = generator.generate(token_range=10)
    parts = generated.split("-")
    assert 0 <= int(parts[2]) < 10


def test_haikunator_generator_custom_delimiter():
    """
    Tests that the HaikunatorGenerator respects the separator.
    """
    generator = HaikunatorGenerator()
    sep = "_"
    generated = generator.generate(delimiter=sep)
    assert sep in generated
    assert "-" not in generated
    parts = generated.split(sep)
    assert len(parts) == 3


def test_haikunator_function():
    """
    Tests the module-level haikunator function.
    """
    h = haikunator()
    assert isinstance(h, str)
    assert len(h.split("-")) == 3


@given(
    token_range=st.integers(min_value=1, max_value=100000),
    delimiter=st.text(min_size=1, max_size=3, alphabet="-_.|"),
)
def test_haikunator_properties(token_range, delimiter):
    """
    Tests properties of the HaikunatorGenerator.
    """
    generator = HaikunatorGenerator()
    generated = generator.generate(token_range=token_range, delimiter=delimiter)

    parts = generated.split(delimiter)
    assert len(parts) == 3
    assert parts[0] in ADJECTIVES
    assert parts[1] in NOUNS
    assert parts[2].isdigit()
    assert 0 <= int(parts[2]) < token_range
