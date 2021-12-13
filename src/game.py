import pygame
from classes.board import Board
from classes.pacman import Pacman
from classes.fantasma import *
from classes.variaveis import *

pygame.init()
variaveis = Variaveis()

tela = pygame.display.set_mode((800, 600), 0)

pacman = Pacman(variaveis.size)
cenario = Board(variaveis.size, pacman)
blinky = Fantasma (variaveis.vermelho, variaveis.size)

while True:
    pacman.calcular_regras()
    cenario.calcular_regras()

    tela.fill(variaveis.preto)
    cenario.pintar(tela)
    pacman.pintar(tela)
    blinky.pintar(tela)
    pygame.display.update()
    pygame.time.delay(100)
    
    eventos = pygame.event.get()
    
    pacman.processar_eventos(eventos)
    cenario.processar_eventos(eventos)

