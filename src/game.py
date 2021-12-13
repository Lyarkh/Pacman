import pygame
from classes.board import *
from classes.pacman import *
from classes.fantasma import *
from classes.variaveis import *

pygame.init()
variaveis = VariaveisGlobais()

tela = pygame.display.set_mode((800, 600), 0)

pacman = Pacman(variaveis.size)

blinky = Fantasma(variaveis.vermelho, variaveis.size)
inky = Fantasma(variaveis.ciano, variaveis.size)
clyde = Fantasma(variaveis.laranja, variaveis.size)
pinky = Fantasma(variaveis.rosa, variaveis.size)
cenario = Board(variaveis.size, pacman)

cenario.adicionar_movivel(pacman)
cenario.adicionar_movivel(blinky)
cenario.adicionar_movivel(inky)
cenario.adicionar_movivel(clyde)
cenario.adicionar_movivel(pinky)

while True:
    pacman.calcular_regras()

    blinky.calcular_regras()
    inky.calcular_regras()
    clyde.calcular_regras()
    pinky.calcular_regras()
    cenario.calcular_regras()

    tela.fill(variaveis.preto)

    cenario.pintar(tela)
    pacman.pintar(tela)

    blinky.pintar(tela)
    inky.pintar(tela)
    clyde.pintar(tela)
    pinky.pintar(tela)

    pygame.display.update()
    pygame.time.delay(100)
    
    eventos = pygame.event.get()
    
    pacman.processar_eventos(eventos)
    cenario.processar_eventos(eventos)

