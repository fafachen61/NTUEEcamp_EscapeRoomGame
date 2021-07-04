import pygame
import sys
from pygame.locals import *

pygame.init()
screenWidth=1200
screenHeight=900
screen = pygame.display.set_mode((screenWidth, screenHeight))


def drawScreen(pic):
    screen.blit(pic, (0,0))
    pygame.display.update()

pic = 'ps/8F.png'
pic = pygame.image.load(pic)
pic = pygame.transform.scale(pic, (screenWidth, screenHeight))
drawScreen(pic)
pygame.display.update()

while True:
   for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print( (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]) )
   '''for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
               
                if 761 < pygame.mouse.get_pos()[0] < 779 and 382 < pygame.mouse.get_pos()[1] < 400:
                    #floor = 8
                    print('8')
                elif 726 < pygame.mouse.get_pos()[0] < 744 and 354 < pygame.mouse.get_pos()[1] < 372:
                    #floor = 9
                    print('9')
                elif 761 < pygame.mouse.get_pos()[0] < 779 and 354 < pygame.mouse.get_pos()[1] < 372:
                    #floor = 10
                    print('10')'''
