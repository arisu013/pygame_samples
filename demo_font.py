# demo for text display by pygame.font (this is OLD)
# NOTICE: You should use replacement module  pygame.freetypeinstead.
# 注意：これを置き換えるpygame.freetypeを代わりに使うべし


import pygame
import pygame.freetype


pygame.init()
screen = pygame.display.set_mode((320, 120))
pygame.display.set_caption('font demo')
large_text = pygame.font.Font('fonts/hack-fonts/Hack-Regular.ttf', 36)
small_text = pygame.font.Font('fonts/hack-fonts/Hack-Bold.ttf', 24)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((250, 180, 250))
    text_surface = large_text.render('hello world!', True, (0, 0, 0))
    screen.blit(text_surface, (20, 12))

    text_surface = small_text.render('how are you?', True, (0, 0, 0))
    screen.blit(text_surface, (20, 48))

    pygame.display.flip()

pygame.quit()
