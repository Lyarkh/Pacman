import pygame
from .elementojogo import *
from .variaveis import Variaveis

pygame.init()

variaveis = Variaveis()
tela = pygame.display.set_mode((800, 600), 0)

class Fantasma(ElementoJogo):
    def __init__(self, cor, tamanho):
        self.coluna = 6.0
        self.linha = 8.0
        self.tamanho = tamanho
        self.cor = cor

    def calcular_regras(self):
        pass

    def pintar(self, tela):
        fatia = self.tamanho // 8
        px = int(self.coluna * self.tamanho)
        py = int(self.linha * self.tamanho)
        contorno = [(px, py + self.tamanho), 
                    (px + fatia, py + fatia * 2),
                    (px + fatia * 2, py + fatia // 2),
                    (px + fatia * 3, py),
                    (px + fatia * 5, py),
                    (px + fatia * 6, py + fatia // 2),
                    (px + fatia * 7, py + fatia * 2),
                    (px + self.tamanho, py + self.tamanho)
                    ]

        olho_raio_ext = fatia
        olho_raio_int = fatia // 2

        olho_e_x = int(px + fatia * 2.5)
        olho_e_y = int(py + fatia * 2.5)
        olho_d_x = int(px + fatia * 5.5)
        olho_d_y = int(py + fatia * 2.5)

        pygame.draw.polygon(tela, self.cor, contorno, 0)

        pygame.draw.circle(tela, variaveis.branco, (olho_e_x, olho_e_y), olho_raio_ext, 0)
        pygame.draw.circle(tela, variaveis.preto, (olho_e_x, olho_e_y), olho_raio_int, 0)

        pygame.draw.circle(tela, variaveis.branco, (olho_d_x, olho_d_y), olho_raio_ext, 0)
        pygame.draw.circle(tela, variaveis.preto, (olho_d_x, olho_d_y), olho_raio_int, 0)


    def processar_eventos(self, eventos):
        pass