import secrets
from typing import List

from .data import ADJECTIVES, ANIMALS


class PetnameGenerator:
    """
    A generator for creating human-readable "petname" identifiers.

    Petnames are combinations of words (typically adjectives and nouns) that are
    easy to remember and pronounce.

    Usage:
        >>> generator = PetnameGenerator()
        >>> petname = generator.generate()
        >>> print(petname)  # e.g., "happy-swallow"
    """

    def generate(self, words: int = 2, separator: str = "-") -> str:
        """
        Generates a new petname ID.

        Args:
            words: The number of words in the petname. Defaults to 2.
                   Must be at least 1.
            separator: The string used to join the words. Defaults to "-".

        Returns:
            A new petname string.

        Raises:
            ValueError: If words is less than 1.
        """
        if words < 1:
            raise ValueError("words must be at least 1")

        parts: List[str] = []

        # Add adjectives (words - 1)
        for _ in range(words - 1):
            parts.append(secrets.choice(ADJECTIVES))

        # Add the final animal name
        parts.append(secrets.choice(ANIMALS))

        return separator.join(parts)


_petname_generator = PetnameGenerator()


def petname(words: int = 2, separator: str = "-") -> str:
    """
    Generates a new petname ID.

    This function uses a module-level singleton instance of `PetnameGenerator`.

    Args:
        words: The number of words in the petname. Defaults to 2.
               Must be at least 1.
        separator: The string used to join the words. Defaults to "-".

    Returns:
        A new petname string.
    """
    return _petname_generator.generate(words=words, separator=separator)
