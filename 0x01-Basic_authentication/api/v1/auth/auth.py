#!/usr/bin/env python3
"""API Authentication"""
from flask import request
from typing import TypeVar, List


class Auth():
    """Manages the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns a boolean"""
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if path.endswith("/") is False:
            path = path + "/"

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/') is false:
                excluded_path += '/'

        astericks = [stars[:-1]
                     for stars in excluded_paths if stars[-1] == '*']

        for stars in astericks:
            if path.startswith(stars):
                return False

        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Validates the request"""
        if request is None:
            return None
        authorized = request.headers.get("Authorization")
        if not authorized:
            return None
        return authorized

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None - request"""
        return None
