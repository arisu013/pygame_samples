import math
import pygame
from pygame.locals import Rect
from pygame.colordict import THECOLORS as pg_colors
# see: https://www.pygame.org/docs/ref/color_list.html


pygame.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("train demo")
color_on = pg_colors['aquamarine4']
color_off = pg_colors['aquamarine2']
color_bg = pg_colors['navajowhite2']
screen.fill(color_bg)  # back ground color
dot_size = 24

x0, y0 = 4, 4
x1, y1 = 0, 0
theta = 0
length = 45
r = 8
speed = 3
reso = 180 / math.pi * 0.6


def draw_train(start=0, draw_length=0, color=color_on):
    th = start
    while th > start - draw_length:
        x = x0 + int(math.cos(math.radians(th)) * r)
        y = y0 + int(math.sin(math.radians(th)) * r)
        pygame.draw.rect(screen, color, Rect((x0 + x) * dot_size, (y0 + y) * dot_size, dot_size, dot_size))
        th -= reso


draw_train(start=theta, draw_length=length, color=color_on)
running = True
# infinite loop top ----
while running:
    # press ctrl-c to stop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # delete previous drawing
    draw_train(start=theta - length, draw_length=speed, color=color_bg)
    # draw trail
    # draw_train(start=theta - length, draw_length=speed, color=color_off)
    # draw new train
    draw_train(start=theta, draw_length=speed, color=color_on)
    theta += speed

    pygame.display.flip()  # update
    clock.tick(30)  # FPS, Frame Per Second
# infinite loop bottom ----

pygame.quit()