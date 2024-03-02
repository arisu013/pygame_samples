# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py

from datetime import datetime
import pygame
from seven_seg_pg import Seven_seg
from lcd_font_pg import LCD_font

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

pygame.init()



lcd1 = LCD_font_styles

running = True
# infinite loop top ----
while running:
    for count in range(16 ** 4):  # 0から65535まで
        # press ctrl-c or close the window to stop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not running:
            break
        dt_now = datetime.now()
        time_now = (dt_now.hour * 10000
                    + dt_now.minute * 100
                    + dt_now.second)
        
lcd1.update_col(col=0, code=dt_now.hour // 10)
lcd1.update_col(col=1, code=dt_now.hour % 10)
lcd1.update_col(col=2, code=10)
lcd1.update_col(col=3, code=dt_now.minute // 10)
lcd1.update_col(col=4, code=dt_now.minute % 10)
lcd1.update_col(col=5, code=10)
lcd1.update_col(col=6, code=dt_now.second // 10)
lcd1.update_col(col=7, code=dt_now.second % 10)

       
 

pygame.quit()


