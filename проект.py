import pygame


class Board:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.clock = pygame.time.Clock()
        self.delay = 0

    def your_tank(self, pos):
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

    def move_tank(self):
        global key, pos
        for i in range(len(key)):
            if key[i] == pygame.K_w:
                self.y -= 1
            elif key[i] == pygame.K_s:
                self.y += 1
            elif key[i] == pygame.K_a:
                self.x -= 1
            elif key[i] == pygame.K_d:
                self.x += 1
        self.your_tank(pos)


board = Board()
push = False
pos = 0
key = []
screen = pygame.display.set_mode((1920, 1020))
screen.fill((0, 150, 0))
pygame.display.flip()
running = True
x = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pos = event.pos
            board.move_tank()
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):
                push = True
                key.append(event.key)
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d) and len(key) == 1:
                key = []
                push = False
            elif event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):
                del key[key.index(event.key)]
    if push:
        board.move_tank()
    pygame.display.flip()
