#!/usr/bin/env python3
"""Auth module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashe password
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
