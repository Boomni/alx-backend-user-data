#!/usr/bin/env python3
"""API Authentication"""
from api.v1.auth.auth import Auth
import base64
import binascii


class BasicAuth(Auth):
    """Inherits from Auth class"""
    pass

    def extract_base64_authorization_header(
            self,
            authorization_header: str
            ) -> str:
        """
        Returns the Base64 part of the Authorization header for a Basic Auth
        """

        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header[:6] == "Basic ":
            return authorization_header[6:]
        else:
            return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """Basic - Base64 decode"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_b_header = base64.b64decode(base64_authorization_header)
            header = decoded_b_header.decode('utf-8')
            return header
        except binascii.Error:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> str:
        """Basic - User credentials"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        username, password = decoded_base64_authorization_header.split(":")
        return username, password
