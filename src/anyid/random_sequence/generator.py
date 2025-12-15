import secrets
import string


class RandomSequenceGenerator:
    """
    A generator for creating cryptographically secure random sequences.

    This implementation uses Python's `secrets` module to ensure that the
    generated sequences are suitable for security-sensitive applications.
    """

    def generate(
        self,
        length: int,
        alphabet: str = string.ascii_letters + string.digits,
    ) -> str:
        """
        Generates a random sequence.

        Args:
            length: The desired length of the sequence.
            alphabet: The set of characters to use. Defaults to alphanumeric (a-z, A-Z, 0-9).

        Returns:
            A random sequence string.
        """
        if length < 0:
            raise ValueError("Length must be non-negative.")
        if not alphabet:
            raise ValueError("Alphabet must not be empty.")

        return "".join(secrets.choice(alphabet) for _ in range(length))


_generator = RandomSequenceGenerator()


def random_sequence(
    length: int,
    alphabet: str = string.ascii_letters + string.digits,
) -> str:
    """
    Generates a random sequence.

    Args:
        length: The desired length of the sequence.
        alphabet: The set of characters to use. Defaults to alphanumeric (a-z, A-Z, 0-9).

    Returns:
        A random sequence string.
    """
    return _generator.generate(length=length, alphabet=alphabet)
