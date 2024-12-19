from dataclasses import dataclass
from authorization.domain.filters.base import BaseFilter


@dataclass
class ByUserId(BaseFilter):
    id: int

    def get_filter_dict(self):
        return {'telegram_user__pk': self.id}
    

@dataclass
class ByTokenOid(BaseFilter):
    oid: str

    def get_filter_dict(self):
        return {'oid': self.oid}
