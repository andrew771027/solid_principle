import abc
class ILogger(abc.ABC):

    @abc.abstractmethod
    def Log(self, message: str):
        raise NotImplementedError
