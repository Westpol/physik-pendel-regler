import time
import pygame
import math
import pendulum
import controller
import controlSwitch

pygame.init()

screen = pygame.display.set_mode((1500, 1300))

pendulum = pendulum.Pendulum(cartMass=5)
controller = controller.Controller(pendulum)

clock = pygame.time.Clock()

maxForce = 100
correction = 0

control_switch = controlSwitch.controlSwitch(30, 1200, "Controller", state=True)
debug_switch = controlSwitch.controlSwitch(150, 1200, "Debug", state=False)

paused: bool = False

while True:
    # ========================== main loop ============================
    if not paused:
        if control_switch.getState():
            correction = controller.update()    # PID controller

        if pygame.key.get_pressed()[pygame.K_RIGHT]:    # override
            correction = 100
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            correction = -100
        elif not control_switch.getState():
            correction = 0

        pendulum.update(min(max(correction, -maxForce), maxForce))

    screen.blit(pendulum.render(), (0, 0))
    screen.blit(control_switch.renderAll(), control_switch.getPos())
    screen.blit(debug_switch.renderAll(), debug_switch.getPos())
    pygame.display.flip()
    clock.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                control_switch.toggleState()
            if event.key == pygame.K_d:
                debug_switch.toggleState()
            if event.key == pygame.K_p:
                paused = not paused
                if not paused:
                    pendulum.unpause()
                    controller.unpause()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            control_switch.checkClick(mousePos)
            debug_switch.checkClick(mousePos)
