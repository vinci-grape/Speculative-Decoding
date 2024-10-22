from abc import ABC, abstractmethod

class BaseTask(ABC):
    @abstractmethod
    def evaluate(self, model, dataset):
        pass
