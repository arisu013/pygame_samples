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
lcd2 = LCD_font(screen)

lcd1.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=GREEN, COLOR_OFF=GRAY)
lcd1.init_row(X_ORG=8, Y_ORG=20, COL_INTV=6)

lcd2.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=GREEN, COLOR_OFF=GRAY)
lcd2.init_row(X_ORG=8, Y_ORG=8, COL_INTV=6)

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
        #時計
        lcd1.update_col(col=0, code=dt_now.hour // 10)
        lcd1.update_col(col=1, code=dt_now.hour % 10)
        lcd1.update_col(col=2, code=10)
        lcd1.update_col(col=3, code=dt_now.minute // 10)
        lcd1.update_col(col=4, code=dt_now.minute % 10)
        lcd1.update_col(col=5, code=10)
        lcd1.update_col(col=6, code=dt_now.second // 10)
        lcd1.update_col(col=7, code=dt_now.second % 10)
        #日付
        lcd2.update_col(col=0,code=dt_now.year // 1000)
        lcd2.update_col(col=1,code=dt_now.year // 100 -20)
        lcd2.update_col(col=2,code=dt_now.year // 10 -200)
        lcd2.update_col(col=3,code=dt_now.year -2020)
        lcd2.update_col(col=4,code=10)
        lcd2.update_col(col=5,code=dt_now.month // 10)
        lcd2.update_col(col=6,code=dt_now.month % 10)
        lcd2.update_col(col=7,code=10)
        lcd2.update_col(col=8,code=dt_now.day // 10)
        lcd2.update_col(col=9,code=dt_now.day % 10)
        

        pygame.display.flip()  # update_col
        clock.tick(20)  # FPS, Frame Per Second
        screen.fill(DARK_GRAY)
# infinit loop bottom ----

pygame.quit()


