#!/usr/bin/env python3
""" Module of Auth class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if path requires authentication
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Get the authorization header field from the request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user from the request
        """
        return None
