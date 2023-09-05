#!/usr/bin/env python3
"""API Authentication"""
from api.v1.auth.auth import Auth


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
