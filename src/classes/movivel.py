from abc import ABCMeta, abstractmethod

class Movivel(metaclass= ABCMeta):
    
    @abstractmethod
    def aceitar_movimento(self):
        pass

    @abstractmethod
    def recusar_movimento(self, direcoes):
        pass

    @abstractmethod
    def esquina(self, direcoes):
        pass

