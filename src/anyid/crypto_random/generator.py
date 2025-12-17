import secrets


class CryptoRandomGenerator:
    """
    A generator for creating cryptographically secure random hex strings.

    This implementation uses Python's `secrets` module (CSPRNG) to generate
    high-entropy values suitable for cryptographic keys, tokens, and identifiers.

    Usage:
        >>> generator = CryptoRandomGenerator()
        >>> random_id = generator.generate()
        >>> len(random_id)
        64
    """

    def generate(self, nbytes: int = 32) -> str:
        """
        Generates a new cryptographically secure random hex string.

        Args:
            nbytes: The number of random bytes to generate.
                    The resulting hex string will be twice this length.
                    Defaults to 32 bytes (256 bits), producing a 64-char string.

        Returns:
            A new, unique random hex string.

        Example:
            >>> generator = CryptoRandomGenerator()
            >>> token = generator.generate(nbytes=16)
            >>> len(token)
            32
        """
        return secrets.token_hex(nbytes)


_crypto_random_generator = CryptoRandomGenerator()


def crypto_random(nbytes: int = 32) -> str:
    """
    Generates a new cryptographically secure random hex string.

    This function uses a module-level singleton instance of `CryptoRandomGenerator`.

    Args:
        nbytes: The number of random bytes to generate.
                The resulting hex string will be twice this length.
                Defaults to 32 bytes (256 bits).

    Returns:
        A new, unique random hex string.
    """
    return _crypto_random_generator.generate(nbytes=nbytes)
