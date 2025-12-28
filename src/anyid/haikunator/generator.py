import secrets

from .data import ADJECTIVES, NOUNS


class HaikunatorGenerator:
    """
    A generator for creating Haiku-like identifiers.

    Haikunator IDs are in the format "adjective-noun-number", e.g., "yellow-frog-6434".

    Usage:
        >>> generator = HaikunatorGenerator()
        >>> haiku_id = generator.generate()
        >>> print(haiku_id)  # e.g., "yellow-frog-6434"
    """

    def generate(
        self,
        token_range: int = 10000,
        delimiter: str = "-",
    ) -> str:
        """
        Generates a new Haikunator ID.

        Args:
            token_range: The exclusive upper bound for the random number (0 to token_range - 1).
                         Defaults to 10000 (produces 0-9999).
            delimiter: The delimiter between words and number. Defaults to "-".

        Returns:
            A new Haikunator string.
        """
        adjective = secrets.choice(ADJECTIVES)
        noun = secrets.choice(NOUNS)
        token = str(secrets.randbelow(token_range))

        return delimiter.join([adjective, noun, token])


_haikunator_generator = HaikunatorGenerator()


def haikunator(token_range: int = 10000, delimiter: str = "-") -> str:
    """
    Generates a new Haikunator ID.

    This function uses a module-level singleton instance of `HaikunatorGenerator`.

    Args:
        token_range: The exclusive upper bound for the random number (0 to token_range - 1).
                     Defaults to 10000 (produces 0-9999).
        delimiter: The delimiter between words and number. Defaults to "-".

    Returns:
        A new Haikunator string.
    """
    return _haikunator_generator.generate(token_range=token_range, delimiter=delimiter)
