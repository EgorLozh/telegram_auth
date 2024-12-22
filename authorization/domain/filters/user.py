from dataclasses import dataclass
from authorization.domain.filters.base import BaseFilter


@dataclass
class ByUserId(BaseFilter):
    id: int

    def get_filter_dict(self):
        return {'pk': self.id}
    

@dataclass
class ByUsername(BaseFilter):
    username: str

    def get_filter_dict(self):
        return {'username': self.username}
    

@dataclass
class ByTelegramToken(BaseFilter):
    token: str

    def get_filter_dict(self):
        return {'token__token': self.token}
