import uuid

from authorization.domain.repos import BaseUserTokenRepo


class UserToken:
    oid: str
    repo: BaseUserTokenRepo

    def __init__(self, repo: BaseUserTokenRepo, oid: str = None):
        self.repo = repo
        self.oid = oid or str(uuid.uuid4())
    
    def __eq__(self, value):
        if isinstance(value, UserToken):
            return self.oid == value.oid
        return False
    
    def save(self, user: 'User'| None = None):
        self.repo.save(self, user)

from authorization.domain.entities.user import User
    