import pygame
import sys
import animation
from pygame.locals import *

class Ending_scene:
    def __init__(self, score, screen):
        self.screen = screen
        self.score = score
        self.counter = 0
        self.bg_first = pygame.transform.scale(pygame.image.load(f'4Ending/1.png'), (1200, 900))
        self.bg_good = [pygame.transform.scale(pygame.image.load(f'4Ending/1-1.png'), (1200, 900)), 
                        pygame.transform.scale(pygame.image.load(f'4Ending/1-2.png'), (1200, 900)), 
                        pygame.transform.scale(pygame.image.load(f'4Ending/1-3.png'), (1200, 900))]
        self.bg_bad = [pygame.transform.scale(pygame.image.load(f'4Ending/2-1.png'), (1200, 900)), 
                       pygame.transform.scale(pygame.image.load(f'4Ending/2-2.png'), (1200, 900)), 
                       pygame.transform.scale(pygame.image.load(f'4Ending/2-3.png'), (1200, 900))]
        #self.initial()

    def initial(self):
        pygame.init()
        screenWidth=1200
        screenHeight=900
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))
        #self.screen.fill((0, 255, 255))
        #pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def drawscreen_good(self):
        self.screen.blit(self.bg_good[self.counter], (0, 0))
        pygame.display.update()
        self.counter += 1

    def drawscreen_bad(self):
        self.screen.blit(self.bg_bad[self.counter], (0, 0))
        pygame.display.update()
        self.counter += 1

    def run(self):
        self.screen.blit(self.bg_first, (0, 0))
        pygame.display.update()
        if self.score == 3:
            while self.counter < 3:
                next_scene = False
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_e:
                            pygame.quit()
                        elif event.key == K_SPACE or event.key == K_RETURN:
                            next_scene = True
                            self.drawscreen_good()
                if self.counter == 3:
                    next_scene = False
                    while next_scene == False:
                        for event in pygame.event.get():
                            if event.type == KEYDOWN:
                                if event.key == K_e or event.key == K_SPACE:
                                    fin = animation.finale()
                                    fin.run()
        else:
            while self.counter < 3:
                next_scene = False
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_e:
                            pygame.quit()
                        elif event.key == K_SPACE or event.key == K_RETURN:
                            next_scene = True
                            self.drawscreen_bad()
                if self.counter == 3:
                    next_scene = False
                    while next_scene == False:
                        for event in pygame.event.get():
                            if event.type == KEYDOWN:
                                if event.key == K_e or event.key == K_SPACE:
                                    fin = animation.finale()
                                    fin.run()

if __name__ == '__main__':
    ending = Ending_scene(2)
    ending.run()
