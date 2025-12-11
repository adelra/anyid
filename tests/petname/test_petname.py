"""
Tests for the Petname generator.
"""

import pytest
from hypothesis import given, strategies as st

from anyid.petname import petname
from anyid.petname.generator import PetnameGenerator
from anyid.petname.data import ADJECTIVES, ANIMALS


def test_petname_generator_defaults():
    """
    Tests that the PetnameGenerator returns a valid petname with defaults.
    """
    generator = PetnameGenerator()
    generated_petname = generator.generate()
    assert isinstance(generated_petname, str)
    parts = generated_petname.split("-")
    assert len(parts) == 2
    assert parts[0] in ADJECTIVES
    assert parts[1] in ANIMALS


def test_petname_generator_custom_words():
    """
    Tests that the PetnameGenerator respects the words count.
    """
    generator = PetnameGenerator()

    # 1 word (animal only)
    p1 = generator.generate(words=1)
    assert p1 in ANIMALS
    assert "-" not in p1

    # 3 words (adj-adj-animal)
    p3 = generator.generate(words=3)
    parts = p3.split("-")
    assert len(parts) == 3
    assert parts[0] in ADJECTIVES
    assert parts[1] in ADJECTIVES
    assert parts[2] in ANIMALS


def test_petname_generator_custom_separator():
    """
    Tests that the PetnameGenerator respects the separator.
    """
    generator = PetnameGenerator()
    sep = "_"
    p = generator.generate(separator=sep)
    assert sep in p
    assert "-" not in p
    parts = p.split(sep)
    assert len(parts) == 2


def test_petname_generator_invalid_words():
    """
    Tests that the PetnameGenerator raises ValueError for invalid words count.
    """
    generator = PetnameGenerator()
    with pytest.raises(ValueError):
        generator.generate(words=0)
    with pytest.raises(ValueError):
        generator.generate(words=-1)


def test_petname_function():
    """
    Tests the module-level petname function.
    """
    p = petname()
    assert isinstance(p, str)
    assert len(p.split("-")) == 2


@given(
    words=st.integers(min_value=1, max_value=10),
    separator=st.text(min_size=1, max_size=3, alphabet="-_.|"),
)
def test_petname_properties(words, separator):
    """
    Tests properties of the PetnameGenerator.
    """
    generator = PetnameGenerator()
    generated = generator.generate(words=words, separator=separator)

    parts = generated.split(separator)
    assert len(parts) == words

    # The last part should be an animal
    assert parts[-1] in ANIMALS

    # All preceding parts should be adjectives
    if words > 1:
        for part in parts[:-1]:
            assert part in ADJECTIVES
