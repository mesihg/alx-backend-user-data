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
        if path is not None or excluded_paths is not None:
            for excluded_path in excluded_paths:
                if path == excluded_path[:-1]:
                    return False
                elif path[len(excluded_path)-1] == '/':
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Get the authorization header field from the request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user from the request
        """
        return None
