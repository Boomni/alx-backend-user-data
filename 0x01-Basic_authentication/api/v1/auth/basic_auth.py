#!/usr/bin/env python3
"""API Authentication"""
from api.v1.auth.auth import Auth
import base64
import binascii
from models.user import User
from typing import TypeVar


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

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """Basic - User object"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})
        if not users:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Basic - Overload current_user"""
        authorized_header = self.authorization_header(request)
        if not authorized_header:
            return None

        encoded = self.extract_base64_authorization_header(authorized_header)
        if not encoded:
            return None

        decoded = self.decode_base64_authorization_header(encoded)
        if not decoded:
            return None

        email, pwd = self.extract_user_credentials(decoded)
        if not email or not pwd:
            return None

        user = self.user_object_from_credentials(email, pwd)
        return user
