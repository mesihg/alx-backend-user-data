#!/usr/bin/env python3
""" Module of Basic_Auth class
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Returns the Base64 Authorization header for a Basic Authentication
        """
        if authorization_header is isinstance(authorization_header, str):
            if authorization_header.startswith("Basic "):
                return authorization_header[6:]
        return None