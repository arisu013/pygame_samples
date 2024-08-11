import pygame
from pygame.locals import Rect

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("pygame demo - window title here")

running = True
x1, y1 = 0, 2
angle1,angle2 = 45
rcos45 = 100 * 1 / ^ 2 = 70.71 
rsin45 = 100 * 1 / ^ 2 = 70.71

# infinite loop top ----
while running:
    # press ctrl-c to stop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((238, 238, 170))  # back ground color

   
    color_on = (240, 120, 120)
    color_off = (240,120,120)    
    
pygame.draw.rect(screen, color_on, Rect(34 + x1 * 26, 34 + y1 * 26, 32, 32))
x1 += 1
y1 += 1
pygame.display.flip()  # update
clock.tick(5)  # FPS, Frame Per Second
# infinite loop bottom ----

pygame.quit()
