# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py
from datetime import datetime
import pygame
from lcd_font_pg import LCD_font
from pygame.locals import Rect

#mc = Minecraft.create(port=param.PORT_MC)


DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

pygame.init()


screen = pygame.display.set_mode([480, 320])
screen.fill(DARK_GRAY)


x1,y1 = 0,1
color_on = (240, 120, 120)
color_off = (120, 120, 120)
for x0 in range(5):
        for y0 in range(7):
            # pygame.draw.circle(screen, color_off, (24 + x0 * 16, 24 + y0 * 16), 8)
            pygame.draw.rect(screen, color_off, Rect(24 + x0 * 16, 24 + y0 * 16, 12, 12))
clock = pygame.time.Clock()
running = True


while running:
        
         screen.fill((238, 238, 170))  # back ground color

pygame.draw.circle(screen, (176, 176, 222), (320, 240), 120)
pygame.draw.circle(screen, (222, 176, 222), (120, 120), 20)
pygame.draw.circle(screen, (222, 176, 222), (120, 120), 20)
pygame.draw.rect(screen, (120, 120, 120), Rect(120, 120, 200, 120))

for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
if not running:

   dt_now = datetime.now()
time_now = (dt_now.hour * 10000
                    + dt_now.minute * 100
                    + dt_now.second)
        
pygame.draw.rect(screen, color_on, Rect(24 + x1 * 16, 24 + y1 * 16, 12, 12))
x1 += 1
if x1 > 4:
        x1 = 0
        y1 += 1
if y1 > 6:
       y1 = 0
pygame.display.flip()  # update
clock.tick(5)  # FPS, Frame Per Second
# infinit loop bottom ----

pygame.quit()

# infinite loop top ----


        

        

