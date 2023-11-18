import pygame
from pygame.locals import *
pygame.init()

screenWidth = 300
screenHeight = 300

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("tictactoe")
run = True

lineWidth = 6
markers = []
clicked = False
pos = []
pyukumuku = pygame.image.load('pyukumuku.png')
def pyuki(x,y):
    screen.blit(pyukumuku, (x,y))
# x = (screenWidth * 0.5)
# y = (screenHeight * 0.5)
x=0
y=0
def draw_grid():
    background = (255,255,200)
    grid = (50,50,50)
    screen.fill(background)
    for x in range(1,3):
        pygame.draw.line(screen, grid, (0, x*100), (screenWidth, x*100), lineWidth)
        pygame.draw.line(screen, grid, (x*100, 0), (x*100, screenHeight), lineWidth)

for x in range(3):
    row = [0]*3
    markers.append(row)

######################################################################################
while run:
    draw_grid()
    pyuki(x,y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            if event.button == 1:
                clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            if event.button == 1:
                clicked = False
            pos = pygame.mouse.get_pos()
            # print(pos)
            x = (pos[0]-50)
            y = (pos[1]-50)
            print(x)
            print(y)
            pyuki(x+500,y)


    pygame.display.update()

pygame.quit()