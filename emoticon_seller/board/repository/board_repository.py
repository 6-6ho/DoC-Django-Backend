from abc import ABC, abstractmethod


class BoardRepository(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def register(self, boardTitle, boardWriter, boardContent, boardImage):
        pass

    @abstractmethod
    def findByBoardId(self, boardId):
        pass