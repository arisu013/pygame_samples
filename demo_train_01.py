import math
import pygame
from pygame.locals import Rect
from pygame.colordict import THECOLORS as pg_colors
from mcje.minecraft import Minecraft
import param_MCJE as param


pygame.init()
mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('cube-train in the Minecraft')

MC_X0, MC_Y0, MC_Z0 = 50, 0, -200

color_on_mc = param.SEA_LANTERN_BLOCK
color_off_mc = param.AIR

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
#書き始め
length = 0
#半径
r = 8
speed = 3
reso = 180 / math.pi * 0.6
speed = 4
reso = 180 / math.pi * 0.1
#幅
dy = 5


def draw_train(start=0, draw_length=0, color=color_on):
    th = start
    while th > start - draw_length:
        x = x0 + int(math.cos(math.radians(th)) * r)
        y = y0 + int(math.sin(math.radians(th)) * r)
        pygame.draw.rect(screen, color, Rect((x0 + x) * dot_size, (y0 + y) * dot_size, dot_size, dot_size))
        th -= reso

def draw_train_mc(start=0, draw_length=0, dy=0, color=color_on):
    global MC_Y0
    th = start
    while th > (start - draw_length):
        x = MC_X0 + int(math.cos(math.radians(th)) * r)
        z = MC_Z0 + int(math.sin(math.radians(th)) * r)
        y = MC_Y0 + int(dy * (th / 360))
        mc.setBlock(x, y, z, color)
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
    draw_train_mc(start=theta - length, draw_length=speed, dy=dy, color=color_off_mc)
    # draw trail
    # draw_train(start=theta - length, draw_length=speed, color=color_off)
    # draw new train
    draw_train(start=theta, draw_length=speed, color=color_on)
    draw_train_mc(start=theta, draw_length=speed, dy=dy, color=color_off_mc)
    theta += speed

    pygame.display.flip()  # update
    clock.tick(30)  # FPS, Frame Per Second
# infinite loop bottom ----

pygame.quit()