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

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([480, 320])
screen.fill(DARK_GRAY)



lcd1 = LCD_font(screen)
lcd2 = LCD_font(screen)
lcd3 = LCD_font(screen)
lcd4 = LCD_font(screen)

running = True
lcd1.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=GREEN, COLOR_OFF=GRAY)
lcd1.init_row(X_ORG=8, Y_ORG=8, COL_INTV=6)

lcd2.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=GREEN, COLOR_OFF=GRAY)
lcd2.init_row(X_ORG=10, Y_ORG=21, COL_INTV=6)

lcd3.init_col(COLOR_ON=param.GLOWSTONE, COLOR_OFF=param.AIR)
lcd3.init_row(X_ORG=-26, Y_ORG=param.Y_SEA + 55, Z_ORG=5, COL_INTV=6)

lcd4.init_col(COLOR_ON=param.SEA_LANTERN_BLOCK , COLOR_OFF=param.AIR)
lcd4.init_row(X_ORG=-26, Y_ORG=param.Y_SEA + 64, Z_ORG=5, COL_INTV=6)

running = True
# infinite loop top ----
mc.postToChat("clock")
mc.setBlock(5, 5, 5,"gold block")


while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not running:
            break

        

        clock.tick(10)  # FPS, Frame Per Second
        
# infinit loop bottom ----

pygame.quit()

# infinite loop top ----


        

        

