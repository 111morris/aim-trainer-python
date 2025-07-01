import math
import random
import pygame
import time

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT
TARGET_PADDING = 30
BG_COLOR = (0, 25, 40)
GREY = (100, 100, 100)
LIVES = 3
TOP_BAR_HEIGHT = 50

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

LABEL_FONT = pygame.font.SysFont("comicsans", 24)


class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2

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
        # Cast sizes to int for pygame.draw.circle
        pygame.draw.circle(win, RED, (self.x, self.y), int(self.size))
        pygame.draw.circle(win, WHITE, (self.x, self.y), int(self.size * 0.8))
        pygame.draw.circle(win, RED, (self.x, self.y), int(self.size * 0.6))
        pygame.draw.circle(win, WHITE, (self.x, self.y), int(self.size * 0.4))

    def collide(self, x, y):
        dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        return dis <= self.size


def draw(win, targets):
    win.fill(BG_COLOR)
    for target in targets:
        target.draw(win)


def format_time(secs):
    milli = int((secs * 1000) % 1000 // 100)
    seconds = int(secs % 60)
    minutes = int(secs // 60)
    return f"{minutes:02d}:{seconds:02d}.{milli}"


def draw_top_bar(win, elapsed_time, targets_pressed, misses):
    pygame.draw.rect(win, GREY, (0, 0, WIDTH, TOP_BAR_HEIGHT))
    time_label = LABEL_FONT.render(
        f"Time: {format_time(elapsed_time)}", True, BLACK)

    speed = 0
    if elapsed_time > 0:
        speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", True, BLACK)

    hits_label = LABEL_FONT.render(f"Hits: {targets_pressed}", True, BLACK)
    lives_label = LABEL_FONT.render(f"Lives: {LIVES - misses}", True, BLACK)

    win.blit(time_label, (5, 5))
    win.blit(speed_label, (200, 5))
    win.blit(hits_label, (450, 5))
    win.blit(lives_label, (650, 5))


def end_screen(win, elapsed_time, targets_pressed, clicks):
    win.fill(BG_COLOR)
    time_label = LABEL_FONT.render(
        f"Time: {format_time(elapsed_time)}", True, WHITE)

    speed = 0
    if elapsed_time > 0:
        speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", True, WHITE)

    hits_label = LABEL_FONT.render(f"Hits: {targets_pressed}", True, WHITE)

    accuracy = 0
    if clicks > 0:
        accuracy = round(targets_pressed / clicks * 100, 1)
    accuracy_label = LABEL_FONT.render(f"Accuracy: {accuracy}%", True, WHITE)

    message_label = LABEL_FONT.render("Press any key or close to quit", True, WHITE)

    win.blit(time_label, (get_middle(time_label), 100))
    win.blit(speed_label, (get_middle(speed_label), 200))
    win.blit(hits_label, (get_middle(hits_label), 300))
    win.blit(accuracy_label, (get_middle(accuracy_label), 400))
    win.blit(message_label, (get_middle(message_label), 500))

    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False


def get_middle(surface):
    return WIDTH / 2 - surface.get_width() / 2


def main():
    run = True
    targets = []
    clock = pygame.time.Clock()
    targets_pressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()

    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

    while run:
        clock.tick(60)
        click = False
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING + TOP_BAR_HEIGHT, HEIGHT - TARGET_PADDING)
                targets.append(Target(x, y))

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1

        # Iterate over a copy of targets to safely remove while iterating
        for target in targets[:]:
            target.update()

            if target.size <= 0:
                targets.remove(target)
                misses += 1
                continue  # skip collision check if removed

            if click and target.collide(*mouse_pos):
                targets.remove(target)
                targets_pressed += 1

        elapsed_time = time.time() - start_time

        if misses >= LIVES:
            end_screen(WIN, elapsed_time, targets_pressed, clicks)
            run = False
            continue

        draw(WIN, targets)
        draw_top_bar(WIN, elapsed_time, targets_pressed, misses)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

