from anyid import crypto_random
from anyid.crypto_random.generator import CryptoRandomGenerator


def test_crypto_random_defaults():
    """Test crypto_random with default settings (32 bytes -> 64 hex chars)."""
    token = crypto_random()
    assert isinstance(token, str)
    assert len(token) == 64  # 32 bytes * 2 chars/byte
    # Check if it looks like hex
    int(token, 16)


def test_crypto_random_custom_length():
    """Test crypto_random with custom length."""
    token = crypto_random(nbytes=16)
    assert len(token) == 32  # 16 bytes * 2 chars/byte


def test_crypto_random_uniqueness():
    """Test that generated tokens are unique."""
    tokens = {crypto_random() for _ in range(100)}
    assert len(tokens) == 100


def test_generator_class():
    """Test the CryptoRandomGenerator class directly."""
    generator = CryptoRandomGenerator()
    token = generator.generate(nbytes=10)
    assert len(token) == 20
