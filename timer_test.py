import pygame
pygame.init()
screen = pygame.display.set_mode((128, 128))
clock = pygame.time.Clock()

start = pygame.time.get_ticks()
font = pygame.font.SysFont('Consolas', 30)
print(start)
while True:
    print((pygame.time.get_ticks() - start)/1000)
