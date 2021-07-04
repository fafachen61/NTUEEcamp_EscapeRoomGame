import pygame
import sys
import clarify
from time import sleep
from pygame.locals import *
pygame.init()

screenWidth=1200
screenHeight=900
screen = pygame.display.set_mode((screenWidth, screenHeight))

clock = pygame.time.Clock()

min_counter, sec_counter, min_text, sec_text = 90, 00, '90'.rjust(2), '00'.rjust(2)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 100)
font_out = pygame.font.SysFont('Consolas', 100)

out_of_time = False

while True:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT:
            if sec_counter == 0 and min_counter == 0 :
                out_of_time = True
                
            if out_of_time == True:
                if sec_counter == 59:
                    min_counter += 1
                    sec_counter = 0
                else:
                    sec_counter += 1
            elif out_of_time == False:
                if sec_counter > 0 :
                    sec_counter -= 1
                elif sec_counter <= 0:
                    min_counter -= 1
                    sec_counter = 59
            
        if e.type == pygame.QUIT: break
    else:
        screen.fill((255, 255, 255))
        if out_of_time == True:
            screen.blit(font_out.render( str(min_counter).rjust(2,'0') + ':' + str(sec_counter).rjust(2,'0'), True, (255, 0, 0)), (32, 48))
        else:
            screen.blit(font.render( str(min_counter).rjust(2,'0') + ':' + str(sec_counter).rjust(2,'0'), True, (0, 0, 0)), (32, 48))
        pygame.display.flip()
        clock.tick(60)
        continue
    break
