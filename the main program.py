import pygame
import main_page
from pygame.locals import *

pygame.init()
screenWidth=1000
screenHeight=600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('ElevatE escape room main map')

logo = pygame.image.load('elevate.png')

game_start = False

## initial animation
class animation:
    
    def __init__(self,x,y,imglist):
        self.pos=pygame.Vector2(x,y)
        self.frames=[]
        for img in imglist:
            self.frames.append(pygame.image.load(img))
        self.counter=0
        self.frame_num=len(imglist)
    def next(self):
        self.counter=(self.counter+1)%self.frame_num
    def clear(self):
        for i in range(self.frame_num):
            self.frames[i]=None

class background(animation):
    def __init__(self,imglist):
        self.frames=[]
        for img in imglist:
            self.frames.append(pygame.image.load(img))
        self.counter=0
        self.frame_num=len(imglist)

animate = background([f'background0/bg{i}.png' for i in range(52)])

def drawStartScreen():
    screen.blit(animate.frames[animate.counter], (0,0))
    screen.blit(logo, (screenWidth/2-100,screenHeight/2-50))
    pygame.display.update()
        
def start_menu():
    startscreen_run=True
    delay=0

    while startscreen_run == True:
        delay = (delay+1)%2  # stop the animation from moving too fast
        if delay==0:
            animate.next()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_e:
                    pygame.quit()
                elif event.key == K_SPACE:
                    startscreen_run = False
            #if event.type == pygame.MOUSEBUTTONDOWN:
            #    startscreen_run=False
        drawStartScreen()
    animate.clear()
    main_page.main_page()

if __name__=='__main__':
	start_menu()


