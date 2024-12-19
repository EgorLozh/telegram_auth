from abc import ABC, abstractmethod


class BaseFilter(ABC):

    @abstractmethod
    def get_filter_dict(self) -> dict:
        ...
