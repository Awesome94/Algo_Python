from abc import ABC, abstractmethod

class AbstractExample(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def do_something(self):
        pass
class AbstractInheritor(AbstractExample):
    def do_something(self):
        return "this is awesome"
