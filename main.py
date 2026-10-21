import time
import pygame
import math
import pendulum
import controller

pygame.init()

screen = pygame.display.set_mode((1500, 1300))

pendulum = pendulum.Pendulum()
controller = controller.Controller(pendulum)

clock = pygame.time.Clock()

maxForce = 100

while True:
    # ========================== main loop ============================
    correction = controller.update()    # PID controller

    if pygame.key.get_pressed()[pygame.K_RIGHT]:    # override
        correction = 100
    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        correction = -100

    pendulum.update(min(max(correction, -maxForce), maxForce))
    screen.blit(pendulum.render(), (0, 0))
    pygame.display.flip()
    clock.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pass
