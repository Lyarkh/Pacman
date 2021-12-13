import random
import pygame
from .elementojogo import *
from .variaveis import Variaveis

pygame.init()

variaveis = Variaveis()
tela = pygame.display.set_mode((800, 600), 0)

class Fantasma(ElementoJogo):
    def __init__(self, cor, tamanho):
        self.coluna = 6.0
        self.linha = 2.0
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.velocidade = 1
        self.direcao = variaveis.a_baixo
        self.tamanho = tamanho
        self.cor = cor

    def calcular_regras(self):
        if self.direcao == variaveis.a_cima:
            self.linha_intencao -= self.velocidade
        elif self.direcao == variaveis.a_baixo:
            self.linha_intencao += self.velocidade
        elif self.direcao == variaveis.a_esquerda:
            self.coluna_intencao -= self.velocidade
        elif self.direcao == variaveis.a_direita:
            self.coluna_intencao += self.velocidade
    
    def mudar_direcoes(self, direcoes):
        self.direcao = random.choice(direcoes)

    def esquina(self, direcoes):
        self.mudar_direcoes(direcoes)

    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao
    
    def recusar_movimento(self, direcoes):
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.mudar_direcoes(direcoes)

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