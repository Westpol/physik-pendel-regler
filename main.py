import time
import pygame
import math
import pendulum

pygame.init()

screen = pygame.display.set_mode((1500, 1300))

pendulum = pendulum.Pendulum()

clock = pygame.time.Clock()

counter = 0
cartForce = 0

while True:
    # ========================== main loop ============================
    pendulum.update(cartForce)
    screen.blit(pendulum.render(), (0, 0))
    pygame.display.flip()
    clock.tick(60)

    counter += 1

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        cartForce = 30
    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        cartForce = -30
    else:
        cartForce = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
