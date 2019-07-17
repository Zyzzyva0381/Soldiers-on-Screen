import pygame
import sys
import colors
from pygame.locals import *


class Tower(object):
    def __init__(self, x, y, name):
        self.pos = (x, y)
        self.surf = "tower%d" % name

    def draw(self):
        screen.blit(resources[self.surf], self.pos)


def check_quit():
    for _ in pygame.event.get(QUIT):
        pygame.quit()
        sys.exit()


def main():
    global screen, resources

    pygame.init()

    resources = {
        "tower1": pygame.image.load("images\\tower1.png"),
        "tower2": pygame.image.load("images\\tower2.png")

    }

    tower1 = Tower(50, 200, 1)
    tower2 = Tower(650, 200, 2)

    winwidth = 800
    winheight = 600
    screen = pygame.display.set_mode((winwidth, winheight))

    fpsclock = pygame.time.Clock()
    fps = 40

    while True:
        check_quit()

        screen.fill(colors.white)
        tower1.draw()
        tower2.draw()
        pygame.display.update()

        fpsclock.tick(fps)


if __name__ == "__main__":
    main()
