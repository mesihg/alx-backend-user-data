#!/usr/bin/env python3
""" Module of Basic_Auth class
"""
import re
import base64
import binascii
from typing import Tuple
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str
            ) -> str:
        """Returns the Base64 Authorization header for a Basic Authentication
        """
        if type(authorization_header) == str:
            pattern = r'Basic (?P<token>.+)'
            field_match = re.fullmatch(pattern, authorization_header.strip())
            if field_match is not None:
                return field_match.group('token')
        return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str,
    ) -> str:
        """Returns decoded value  of Base64-encoded string authorization header
        """
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(
                base64_authorization_header, validate=True)
            return decoded.decode('utf-8')
        except (binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
        decoded_base64_authorization_header: str,
    ) -> Tuple[str, str]:
        """Returns user email and password from the Base64 decoded value
        """
        if not isinstance(decoded_base64_authorization_header, str):
            return None
        pattern = r'(?P<user>[^:]+):(?P<password>.+)'
        match = re.match(pattern, decoded_base64_authorization_header.strip())
        if match:
            user = match.group('user')
            password = match.group('password')
            return user, password
        return None
