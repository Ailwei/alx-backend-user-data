#!/usr/bin/env python3
"""
Module for authentication using Session auth
"""

from .auth import Auth
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """Handles session-based authentication."""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session for a given user ID.

        Args:
            user_id (str, optional): The user ID for which the
            session is to be created. Defaults to None.

        Returns:
            str: The session ID if creation is successful, otherwise None.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        id = uuid4()
        self.user_id_by_session_id[str(id)] = user_id
        return str(id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieves a user ID based on a given session ID.

        Args:
            session_id (str, optional): The session ID to look up.
            Defaults to None.

        Returns:
            str: The corresponding user ID if found, otherwise None.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Gets the current user based on the session cookie in the request.

        Args:
            request (_type_, optional): The request object
            containing session cookie. Defaults to None.

        Returns:
            User: The user object if found, otherwise None.
        """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """Destroys the session associated with the request.

        Args:
            request (_type_, optional): The request object
            containing session cookie. Defaults to None.

        Returns:
            bool: True if the session was successfully destroyed,
            otherwise False.
        """
        if request is None:
            return False
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_cookie]
        return True
