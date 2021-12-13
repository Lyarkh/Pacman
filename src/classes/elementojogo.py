from abc import ABCMeta, abstractmethod


class ElementoJogo(metaclass= ABCMeta):
    
    @abstractmethod
    def calcular_regras(self):
        pass

    @abstractmethod    
    def pintar(self, tela):
        pass

    @abstractmethod
    def processar_eventos(self, eventos):
        pass