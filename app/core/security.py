from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, InvalidHashError

ph = PasswordHasher()

def password_hash(plaintext: str) -> str | None:
    if not plaintext:
        return None
    return ph.hash(plaintext)

def password_verify(hash_str: str, plaintext: str) -> bool:
    if not hash_str or not plaintext:
        return False
    try:
        return ph.verify(hash_str, plaintext)
    except (VerifyMismatchError, InvalidHashError):
        return False

