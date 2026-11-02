import time
import pygame
import math
import pendulum
import controller
import controlSwitch

pygame.init()

screen = pygame.display.set_mode((1500, 1300))

pendulum = pendulum.Pendulum()
controller = controller.Controller(pendulum)

clock = pygame.time.Clock()

maxForce = 100
controllerEnabled: bool = True
correction = 0

control_switch = controlSwitch.controlSwitch(30, 1220, "Controller", state=True)

while True:
    # ========================== main loop ============================
    if controllerEnabled:
        correction = controller.update()    # PID controller

    if pygame.key.get_pressed()[pygame.K_RIGHT]:    # override
        correction = 100
    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        correction = -100

    pendulum.update(min(max(correction, -maxForce), maxForce))
    screen.blit(pendulum.render(), (0, 0))
    screen.blit(control_switch.renderSwitch(), control_switch.getPos())
    pygame.display.flip()
    clock.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                controllerEnabled = not controllerEnabled

        if event.type == pygame.MOUSEBUTTONDOWN:
            control_switch.checkClick(pygame.mouse.get_pos())
            controllerEnabled = control_switch.getState()
