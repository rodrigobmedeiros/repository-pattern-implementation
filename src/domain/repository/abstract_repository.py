from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    def get(self, id):
        raise NotImplementedError

    @abstractmethod
    def get_all(self):
        raise NotImplementedError
