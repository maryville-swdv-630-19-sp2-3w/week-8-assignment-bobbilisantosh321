from abc import ABC,abstractmethod

#Interface class for differnt Role
class Role(ABC):
    @abstractmethod
    def displayActions(self):
        pass

    @abstractmethod
    def performAction(self, input):
        pass









