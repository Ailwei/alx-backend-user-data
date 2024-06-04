#!/usr/bin/env python3
"""
you will create a class to manage the API authentication
"""


from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for validating if endpoint requires auth """
        if path is None:
            return True
        if excluded_paths is None or exclude_paths == []:
            return True
        if path.endswith('/'):
            path = path[:-1]

        for exec_path in excluded_paths:
            if ecex_path.endswith('/'):
                exec_path = exec_path[:-1]
            if path == exec_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates current user """
        return None
