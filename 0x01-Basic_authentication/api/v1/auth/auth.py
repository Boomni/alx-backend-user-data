#!/usr/bin/env python3
""" Auth """
from flask import request
from typing import List, TypeVar
from fnmatch import fnmatch


class Auth():
    """ Auth Class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method

        Returns:
            True -  if the path is not in the list of strings excluded_paths,
                    if path is None,
                    if excluded_paths is None or empty
            False - if path is in excluded_paths
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if not path.endswith('/'):
            path = path + '/'
        for excluded_path in excluded_paths:
            if fnmatch(path, excluded_path):
                return False
        return True


    def authorization_header(self, request=None) -> str:
        """ returns None
        """
        if request is None or not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')


    def current_user(self, request=None) -> TypeVar('User'):
        """ returns None
        """
        return None

