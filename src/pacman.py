import pygame

amarelo = (255, 255 , 0)
preto = (0, 0, 0)

velocidade = 0.6

pygame.init()

tela = pygame.display.set_mode((640, 480), 0, 0)
x = 10
y = 10
raio = 30

vel_x = velocidade
vel_y = velocidade


while True:
    # 1 - Calcular regras do jogo.
    x += vel_x
    y += vel_y

    if x + raio > 640:
        vel_x = -velocidade
    if x - raio < 0:
        vel_x = velocidade
    if y + raio > 480:
        vel_y = -velocidade
    if y - raio < 0:
        vel_y = velocidade
    
    # 2 - Pintar as coisas na tela.
    tela.fill(preto)
    pygame.draw.circle(tela, amarelo, (int(x), int(y)), raio ,0)
    pygame.display.update()
    # 3 - Verificando eventos
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()