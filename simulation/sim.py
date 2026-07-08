import pygame


pygame.init()

width = 1000
height = 700
running = True

board = pygame.display.set_mode((width, height))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False