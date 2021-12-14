from abc import ABCMeta, abstractmethod

#Classe abstrata para as classes que tem movimentação (Pacman e Fantasma)
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

