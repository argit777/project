import pygame


class Board:
    def __init__(self):
        self.x = 300
        self.y = 300

    def your_tank(self, pos, screen):
        screen = pygame.display.set_mode((1920, 1020))
        screen.fill((0, 150, 0))
        if pos[0] - self.x == 0:
            sin = 0
            cos = 1
        else:
            tangent = (pos[1] - self.y) / (pos[0] - self.x)
            cos = (1 / (tangent ** 2 + 1)) ** 0.5
            sin = (tangent ** 2 / (tangent ** 2 + 1)) ** 0.5
        width_gun = 20
        if self.x > pos[0]:
            cos = -cos
        if self.y > pos[1]:
            sin = -sin
        x1 = self.x + cos * 100
        y1 = self.y + sin * 100
        pygame.draw.polygon(screen, (0, 0, 0), ((self.x + width_gun * sin, self.y - width_gun * cos),
                                                (self.x - width_gun * sin, self.y + width_gun * cos),
                                                (x1 - width_gun * sin, y1 + width_gun * cos),
                                                (x1 + width_gun * sin, y1 - width_gun * cos)))
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 30)

    def move_tank(self, key, screen, pos):
        if key == pygame.K_w:
            self.y -= 1
        elif key == pygame.K_s:
            self.y += 1
        elif key == pygame.K_a:
            self.x -= 1
        else:
            self.x += 1
        self.your_tank(pos, screen)


board = Board()
push = False
pos = 0
key = 0
screen = pygame.display.set_mode((1920, 1020))
screen.fill((0, 150, 0))
pygame.display.flip()
running = True
x = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            board.your_tank(event.pos, screen)
            pos = event.pos
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):
                push = True
                key = event.key
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):
                push = False
    if push:
        board.move_tank(key, screen, pos)
    pygame.display.flip()
