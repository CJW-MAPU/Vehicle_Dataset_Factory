from abc import *


class AttackService(metaclass = ABCMeta):
    @abstractmethod
    def make_dos(self, dataset):
        pass

    @abstractmethod
    def make_fuzzing(self, dataset):
        pass

    @abstractmethod
    def make_replay(self, dataset):
        pass

    @abstractmethod
    def make_spoofing(self, dataset):
        pass
