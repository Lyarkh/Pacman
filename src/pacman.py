#pip install
import pygame

pygame.init()

tela = pygame.display.set_mode((800, 600), 0)

amarelo = (255,255,0)
preto = (0,0,0)

class Pacman:
    def __init__(self):
        self.centro_x = 400
        self.centro_y = 300 
        self.tamanho = 100
        self.vel_x = 1
        self.vel_y = 1
        self.raio = self.tamanho/2
    
    def calcular_regras(self):
        self.centro_x += self.vel_x
        self.centro_y += self.vel_y

        if self.centro_x + self.raio > 800:
            self.vel_x = -1
        if self.centro_x - self.raio < 0:
            self.vel_x = 1

        if self.centro_y + self.raio > 600:
            self.vel_y = -1
        if self.centro_y - self.raio < 0:
            self.vel_y = 1


    def pintar(self,tela):
        # desenhando corpo pacman
        pygame.draw.circle(tela, amarelo, (self.centro_x, self.centro_y), self.raio, 0)

        #Desenho boca pacman
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)

        pontos_boca_pacman = [canto_boca, labio_superior, labio_inferior]

        pygame.draw.polygon(tela, preto, pontos_boca_pacman, 0)

        #Desenho olho Pacman
        olho_x = int(self.centro_x + (self.raio / 3))
        olho_y = int(self.centro_y - (self.raio * 0.70))
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, preto, (olho_x, olho_y), olho_raio, 0)

if __name__ == "__main__":
    pacman = Pacman()


while True:
    pacman.calcular_regras()

    tela.fill(preto)
    pacman.pintar(tela)
    pygame.display.update()
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()