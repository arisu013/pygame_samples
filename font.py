# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py

from datetime import datetime
import pygame
from lcd_font_pg import LCD_font

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 400])


lcd1 = LCD_font(screen)

lcd1.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=GREEN, COLOR_OFF=GRAY)
lcd1.init_row(X_ORG=8, Y_ORG=8, COL_INTV=6)

running = True
# infinite loop top ----

while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not running:
            break

        dt_now = datetime.now()
        time_now = (dt_now.hour * 10000
                    + dt_now.minute * 100
                    + dt_now.second)
        
        lcd1.update_col(col=0,code=0)
        lcd1.update_col(col=1,code=1)
        lcd1.update_col(col=2,code=2)
        lcd1.update_col(col=3,code=3)
        lcd1.update_col(col=4,code=4)
        lcd1.update_col(col=5,code=5)
        lcd1.update_col(col=6,code=6)
        lcd1.update_col(col=7,code=7)
        lcd1.update_col(col=8,code=8)
        lcd1.update_col(col=9,code=9)
        lcd1.update_col(col=10,code=10)

        pygame.display.flip()  # update_col
        clock.tick(20)  # FPS, Frame Per Second
        screen.fill(DARK_GRAY)
# infinit loop bottom ----

pygame.quit()


