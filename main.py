import math 
import random
import pygame
import time
pygame.init()

WIDTH, HEIGHT = 800, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Aim Trainer")

TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT
TARGET_PADDING = 30
BG_COLOR = (0, 25, 40)

class Target: 
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = 'red'
    SECOND_COLOR = 'white'

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True

    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False

        if self.grow:
            self.size += self.GROWTH_RATE
        else: 
            self.size -= self.GROWTH_RATE


    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y,), self.size)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y,), self.size * 0.8)
        pygame.draw.circle(win, self.COLOR, (self.x, self.y,), self.size * 0.6)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y,), self.size * 0.4)

def draw(win, targets): 
    win.fill(BG_COLOR)
    
    for target in targets:
        target.draw(win)

    pygame.display.update()

def main():
    run = True
    targets = []
    clock = pygame.time.Clock()
    target_pressed = 0 
    clicks = 0 
    misses = 0 
    start_time = time.time()


    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

    while run:
        clock.tick(60)
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True 
                clicks += 1

        for target in targets:
            target.update()

            if target.size <= 0:
                targets.remove(target)
                misses += 1

        draw(WIN, targets)

    pygame.quit()

if __name__ == "__main__":
    main()
