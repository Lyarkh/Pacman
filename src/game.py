import pygame

from classes.board import Board
from classes.pacman import Pacman

pygame.init()

tela = pygame.display.set_mode((800, 600), 0)
preto = (0, 0, 0)
size = 600 // 30


pacman = Pacman(size)
cenario = Board(size, pacman)

while True:
    pacman.calcular_regras()
    cenario.calcular_regras()

    tela.fill(preto)
    cenario.pintar(tela)
    pacman.pintar(tela)
    pygame.display.update()
    pygame.time.delay(100)
    
    eventos = pygame.event.get()
    for e in eventos:
        if e.type == pygame.QUIT:
            exit()

    pacman.processar_eventos(eventos)

