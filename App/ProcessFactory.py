import multiprocessing

class AbstractFactory:
    FactoryName = None
    def __init__(self, Name):
        self.FactoryName = Name

    def CreateInstance(self):
        return None

class ProcessFactory(AbstractFactory):
    def __init__(self, Name):
        super().__init__(Name)

    def CreateInstance(self, ptr_function):
        return multiprocessing.Process(target=ptr_function)