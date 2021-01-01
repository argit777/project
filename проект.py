import pygame


class Board:
    def __init__(self):
        self.x = 300
        self.y = 300

    def your_tank(self, pos, screen):
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


board = Board()
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
            screen = pygame.display.set_mode((1920, 1020))
            screen.fill((0, 150, 0))
            board.your_tank(event.pos, screen)
    pygame.display.flip()
