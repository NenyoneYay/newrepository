print ("hello world")
import pygame
import time
pygame.init()

screenWidth = 800
screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))

player = pygame.Rect((300,250,50,50))

# time.sleep(5)
run = True
while run == True:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0), player)

    key = pygame.key.get_pressed()
    #WASD up down left right
    playerSpeed = 1
    if key[pygame.K_a]==True and key[pygame.K_w]==True:
        player.move_ip(-1,-1)
    elif key[pygame.K_a]==True and key[pygame.K_s]==True:
        player.move_ip(-1,1)
    elif key[pygame.K_d]==True and key[pygame.K_w] == True:
        player.move_ip(1,-1)
    elif key[pygame.K_d]==True and key[pygame.K_s] == True:
        player.move_ip(1,1)
    elif key[pygame.K_a]==True:
        player.move_ip(-1,0)
    elif key[pygame.K_d]==True:
        player.move_ip(1,0)
    elif key[pygame.K_w]==True:
        player.move_ip(0,-1)
    elif key[pygame.K_s]==True:
        player.move_ip(0,1)
    #WASD diagonall



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
