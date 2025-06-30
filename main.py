import math 
import random
import pygame
import time
pygame.init()

WIDTH, HEIGHT = 800, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Aim Trainer")

class Target: 
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = 'red'

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0

    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False

        if self.grow:
            self.size += self.GROWTH_RATE
        else: 
            self.size -= self.GROWTH_RATE
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y,), self.size)
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()

if __name__ == "__main__":
    main()
