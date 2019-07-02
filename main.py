import sys
import pygame
from pygame.locals import *



def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((960,500))
    pygame.display.set_caption("Chaos")

    background_img = pygame.image.load('res/background.jpg').convert()
    pygame.mixer.music.load('res/You.mp3')
    pygame.mixer.music.play(-1, 0.0)


    while True:
        #screen.blit(background_img, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    main()