import pygame
import random
import time
(catx, caty) = (0, 0)
(mousex, mousey) = (500, 500)
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Cheese Chaser')
cheese = pygame.image.load("cheese.png")
cheese = pygame.transform.scale(cheese, (30, 30))
cat = pygame.image.load("HungryCat.png")
cat = pygame.transform.scale(cat, (100, 100))
mouse = pygame.image.load("HungryMouse.png")
mouse = pygame.transform.scale(mouse, (80, 80))
win = pygame.image.load("win.gif")
win = pygame.transform.scale(win, (600, 600))
game_over = pygame.image.load("GameOver.jpeg")
game_over = pygame.transform.scale(game_over, (600, 600))
field = pygame.image.load("field.png")
done = False
while not done:
    screen.blit(field, [0, 0])
    screen.blit(cat, (catx, caty))
    screen.blit(mouse, (mousex, mousey))
    screen.blit(cheese, (160, 0))
    if (catx + -20) <= mousex <= (catx + 20) and (caty + -20) <= mousey <= (caty + 20):
        break
    if 140 <= mousex <= 180 and -20 <= mousey <= 20:
        screen.blit(win, [0, 0])
        pygame.display.flip()
        time.sleep(1)
        pygame.quit()
        quit()
    xy = random.randint(0, 3)
    if xy == 1:
        if mousex > catx:
            catx = catx + 3.5
        elif mousex < catx:
            catx = catx - 3.5
    elif xy == 2:
        if mousey > caty:
            caty = caty + 3.5
        elif mousey < caty:
            caty = caty - 3.5
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                mousey = mousey + 20
            elif event.key == pygame.K_UP:
                mousey = mousey -20
            elif event.key == pygame.K_RIGHT:
                mousex = mousex + 20
            elif event.key == pygame.K_LEFT:
                mousex = mousex - 20
    pygame.display.flip()
screen.blit(game_over, [0, 0])
pygame.display.flip()
time.sleep(1)
pygame.quit()
quit()
    