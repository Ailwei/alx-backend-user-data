#!/usr/bin/env python3
"""
Module for authentication
"""

from typing import List, TypeVar
from flask import request
import os


class Auth:
    """Handles the authentication logic."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if authentication is required for a given path.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): The list of paths that
            are excluded from authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
            elif path.startswith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_path[:-1]):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """Gets the Authorization header from the request.

        Args:
            request (_type_, optional): The request object. Defaults to None.

        Returns:
            str: The Authorization header if present, otherwise None.
        """
        if request is None:
            return None

        header = request.headers.get('Authorization')

        if header is None:
            return None

        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user based on the request.

        Args:
            request (_type_, optional): The request object. Defaults to None.

        Returns:
            User: The current user, if any, otherwise None.
        """
        return None

    def session_cookie(self, request=None):
        """Gets the session cookie from the request.

        Args:
            request (_type_, optional): The request object. Defaults to None.

        Returns:
            str: The session cookie if present, otherwise None.
        """
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
