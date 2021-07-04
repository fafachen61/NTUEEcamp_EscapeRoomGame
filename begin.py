import pygame
import sys
import floor
from pygame.locals import *

class Begin_scene:
    def __init__(self):
        screenWidth=1200
        screenHeight=900
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))
        #self.screen.fill((0, 255, 255))
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.counter = 0
        self.bg = []
        self.bg.append(pygame.transform.scale(pygame.image.load(f'0Login.png'), (1200, 900)))
        self.bg.append(pygame.transform.scale(pygame.image.load('rule.png'), (1200, 900)))
        for i in range(12):
            self.bg.append(pygame.transform.scale(pygame.image.load(f'1Begin/{i+1}.png'), (1200, 900)))
        for i in range(3):
            self.bg.append(pygame.transform.scale(pygame.image.load(f'2Elevator/{i+1}.png'), (1200, 900)))
    
    def drawscreen(self):
        self.screen.blit(self.bg[self.counter], (0, 0))
        pygame.display.update()
        self.counter += 1

    def run(self):
        
        while self.counter < 17:
            self.drawscreen()
            next_scene = False
            while next_scene == False:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_e:
                            pygame.quit()
                        elif event.key == K_SPACE or event.key == K_RETURN:
                            next_scene = True
        floor.floorpic(self.screen)
        

if __name__ == '__main__':
    begin = Begin_scene()
    begin.run()



