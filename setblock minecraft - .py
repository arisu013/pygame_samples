# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py
from datetime import datetime
import pygame
from lcd_font_pg import LCD_font
from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

x_coordinate = 5
y_coordinate = 80
z_coordinate = 5
pygame.init()

clock = pygame.time.Clock()


lcd1 = LCD_font
lcd2 = LCD_font


running = True

# infinite loop top ----
mc.postToChat("clock")
mc.setBlock(x_coordinate, y_coordinate, z_coordinate, param.GLOWSTONE)


        

        

