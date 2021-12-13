import pygame
from .variaveis import Variaveis

pygame.init()
variaveis = Variaveis()

tela = pygame.display.set_mode((800, 600), 0)
fonte = pygame.font.SysFont("arial", 24, True, False)   

class Pacman:
    def __init__(self, tamanho):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300 
        self.tamanho = tamanho
        self.vel_x = 0
        self.vel_y = 0
        self.raio = self.tamanho // 2
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha
    
    def calcular_regras(self):
        self.coluna_intencao = self.coluna + self.vel_x
        self.linha_intencao = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha  * self.tamanho + self.raio)

    def pintar(self,tela):
        # desenhando corpo pacman
        pygame.draw.circle(tela, variaveis.amarelo, (self.centro_x, self.centro_y), self.raio, 0)

        #Desenho boca pacman
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)

        pontos_boca_pacman = [canto_boca, labio_superior, labio_inferior]

        pygame.draw.polygon(tela, variaveis.preto, pontos_boca_pacman, 0)

        #Desenho olho Pacman
        olho_x = int(self.centro_x + (self.raio / 3))
        olho_y = int(self.centro_y - (self.raio * 0.70))
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, variaveis.preto, (olho_x, olho_y), olho_raio, 0)
    
    def processar_eventos(self,eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = variaveis.velocidade
                elif e.key == pygame.K_LEFT:
                    self.vel_x = -variaveis.velocidade
                elif e.key == pygame.K_UP:
                    self.vel_y = -variaveis.velocidade
                elif e.key == pygame.K_DOWN:
                    self.vel_y = variaveis.velocidade
            
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT or e.key == pygame.K_LEFT:
                    self.vel_x = 0
                elif e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                    self.vel_y = 0
    
    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao