import pygame
import page1
import page2
import page3
import end_page
from pygame.locals import *

pygame.init()
screenWidth=1000
screenHeight=600
screen = pygame.display.set_mode((screenWidth, screenHeight))

#pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('ElevatE escape room main map')

bg = pygame.image.load('elevator.jpg')
bg = pygame.transform.scale(bg, (screenWidth, screenHeight))

def drawStartScreen():
    
    screen.blit(bg, (0,0))
    pygame.display.update()



def main_page():
    m_page_run = True
    while m_page_run == True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_e:
                    pygame.quit()
                elif event.key == K_SPACE:
                    m_page_run = False
        drawStartScreen()
    #bg.clear()
    page1.page()
if __name__=='__main__':
	main_page()


    
    
        
