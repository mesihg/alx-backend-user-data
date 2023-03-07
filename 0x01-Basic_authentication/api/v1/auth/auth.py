#!/usr/bin/env python3
""" Module of Auth class
"""
import re
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if path requires authentication
        """
        if path is None or excluded_paths is None:
            return False
        for exclusion_path in excluded_paths:
            pattern = exclusion_path.replace('*', '.*').rstrip('/') + '/?$'
        if re.match(pattern, path):
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
