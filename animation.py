import pygame
from pygame.locals import *


class animation:
    def __init__(self,x,y,imglist):
        self.pos=pygame.Vector2(x,y)
        self.frames=[]
        for img in imglist:
            self.frames.append(pygame.transform.scale(pygame.image.load(img), (1200, 900)))
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
            self.frames.append(pygame.transform.scale(pygame.image.load(img), (1200, 900)))
        self.counter=0
        self.frame_num=len(imglist)

class finale:
    def __init__(self):
        self.logo = pygame.image.load('elevate.png')
        self.animate = background([f'background0/bg{i}.png' for i in range(52)])
        self.initial()

    def initial(self):
        pygame.init()
        self.screenWidth=1200
        self.screenHeight=900
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('ElevatE escape room main map')

    def drawStartScreen(self):
        self.screen.blit(self.animate.frames[self.animate.counter], (0,0))
        self.screen.blit(self.logo, (self.screenWidth/2-100,self.screenHeight/2-50))
        pygame.display.update()

    def run(self):
        startscreen_run=True
        delay=0
        while startscreen_run == True:
            delay = (delay+1)%2  # stop the animation from moving too fast
            if delay==0:
                self.animate.next()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_e:
                        pygame.quit()
                    elif event.key == K_SPACE or event.key == K_RETURN:
                        startscreen_run = False
                #if event.type == pygame.MOUSEBUTTONDOWN:
                #    startscreen_run=False
            self.drawStartScreen()
        self.animate.clear()
        pygame.quit()

if __name__=='__main__':
    fin = finale()
    fin.run()
        
        
    
