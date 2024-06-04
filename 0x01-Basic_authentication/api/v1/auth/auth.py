#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for validating if endpoint requires auth """
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True

        if path.endswith('/'):
            path = path[:-1]  # Remove trailing slash to match excluded_paths

        for exc_path in excluded_paths:
            if exc_path.endswith('/'):
                exc_path = exc_path[:-1]  # Remove trailing slash to match path
            if path == exc_path:
                return False
            if exc_path.endswith('*') and path.startswith(exc_path[:-1]):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates current user """
        return None
