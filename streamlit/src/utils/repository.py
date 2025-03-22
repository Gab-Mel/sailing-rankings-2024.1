from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def create(self): ...

    @abstractmethod
    def read(self): ...

    @abstractmethod
    def list(self): ...

    @abstractmethod
    def update(self): ...

    @abstractmethod
    def delete(self): ...