import abc
from src.solid.lsp.correspond.lib.interface_employee import IEmployee


class IManager:

    @abc.abstractmethod
    def generate_performance_review(self):
        raise NotImplementedError
