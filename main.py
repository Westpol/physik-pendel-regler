import time
import pygame
import math
import pendulum

pygame.init()

screen = pygame.display.set_mode((1500, 1300))

pendulum = pendulum.Pendulum()

clock = pygame.time.Clock()

counter = 0
cartPos = 0

while True:
    # ========================== main loop ============================
    pendulum.update()
    screen.blit(pendulum.render(math.sin((counter / 100)) * math.pi, cartPos), (0, 0))
    pygame.display.flip()
    clock.tick(60)

    counter += 1

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        cartPos += 10
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        cartPos -= 10

    cartPos = max(min(cartPos, 650), -650)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
