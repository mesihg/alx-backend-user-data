#!/usr/bin/env python3
""" Module of SessionAuth class
"""
from uuid import uuid4
from .auth import Auth


class SessionAuth(Auth):
    """SessionAuth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create session"""
        if isinstance(user_id, str) and user_id is not None:
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return User ID for session ID"""
        if isinstance(session_id, str) and session_id is not None:
            return self.user_id_by_session_id.get(session_id)
        return None
