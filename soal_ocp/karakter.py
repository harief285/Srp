from abc import ABC, abstractmethod
class Karakter(ABC):
        
    def __init__(self,nama:str, power:int):
        self.__nama=nama
        self.__power=power
        
        
        
    
    @abstractmethod
    def menyerang (self):
        pass