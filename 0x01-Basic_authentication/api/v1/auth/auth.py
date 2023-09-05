#!/usr/bin/env python3
"""API Authentication"""
from flask import request
from typing import TypeVar, List


class Auth():
    """Manages the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns a boolean"""
        if path is None and excluded_paths is None:
            return True
        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """Returns None - request"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None - request"""
        return None
