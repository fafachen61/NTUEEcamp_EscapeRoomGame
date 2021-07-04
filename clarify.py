import pygame
import sys
from pygame.locals import *
import ending


class Clarify_scene:
    def __init__(self):
        self.score_now = 0
        self.counter = 0
        self.bg = []
        for i in range(31):
            img = pygame.transform.scale(pygame.image.load(f'3Clarify/{i+1}.png'), (1200, 900))
            self.bg.append(img)
        self.initial()
    def initial(self):
        pygame.init()
        screenWidth=1200
        screenHeight=900
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))
        #self.screen.fill((0, 255, 255))
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def run(self):
        choice = [13, 21, 30]
        while self.counter < 31:
            self.drawscreen()
            next_scene = False
            if self.counter == 13:
                q = 1
            elif self.counter == 21:
                q = 2
            elif self.counter == 30:
                q = 3
            while next_scene == False:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_e:
                            pygame.quit()
                        elif (event.key == K_SPACE or event.key == K_RETURN) and self.counter not in choice:
                            next_scene = True
                    if event.type == pygame.MOUSEBUTTONDOWN and self.counter in choice:
                        if 50 < pygame.mouse.get_pos()[0]<1150 and 160<pygame.mouse.get_pos()[1]<260:
                            print(1)
                            next_scene = True
                            a = 1
                            self.score(q, a)
                        if 50 < pygame.mouse.get_pos()[0]<1150 and 300<pygame.mouse.get_pos()[1]<400:
                            print(2)
                            next_scene = True
                            a = 2
                            self.score(q, a)
                        if 50 < pygame.mouse.get_pos()[0]<1150 and 445<pygame.mouse.get_pos()[1]<550:
                            print(3)
                            next_scene = True
                            a = 3
                            self.score(q, a)
        print(self.get_score())
        #pygame.quit()
        end = ending.Ending_scene(self.get_score(), self.screen)
        end.run()
    
    def drawscreen(self):
        self.screen.blit(self.bg[self.counter], (0, 0))
        pygame.display.update()
        self.counter += 1
        #print('dao')

    def score(self, q, a):
        if q == a:
            self.score_now += 1

    def get_score(self):
        return self.score_now 


if __name__ == '__main__':
    clarify = Clarify_scene()
    #clarify.initial()
    clarify.run()
        

