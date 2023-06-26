import pygame as pg
import abstracts
from abstracts import WIDTH, HEIGHT, PADDING, FPS, WHITE, BLACK, BG_ELEMENTS_COLOR, HOLE_COLOR, PADDLE_HEIGHT, \
    PADDLE_WIDTH, BALL_RADIUS, LEFT, RIGHT, GAME_STARTED, PLAY_WIDTH, PLAY_HEIGHT, HOLE_HEIGHT, PLAY_HEIGHT


# Defining a paddle
class Paddle(abstracts.RectObjects):
    COLOR = WHITE
    VEL = 10

    def __init__(self, x, y, width, height, side):
        super().__init__(x, y, width, height, side)
        self.rect = pg.Surface((self.width, self.height))
        self.angle = 0

    def draw(self, win):
        win.blit(self.rect, (self.x, self.y))

    def move(self, up=True):
        if up and self.y > PADDING:
            self.y -= self.VEL
        elif up is False and self.y < HEIGHT - PADDLE_HEIGHT - PADDING:
            self.y += self.VEL

    def rotate(self, clockwise):
        pass


# Defining the ball
class Ball():
    COLOR = HOLE_COLOR
    instances = []

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.dx = 10
        self.dy = 10
        Ball.instances.append(self)

    def draw(self, win):
        pg.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def is_off_screen(self):
        return self.x > WIDTH - PADDING or self.x < PADDING

    def detect_collision(self):
        if self.y >= HEIGHT - PADDING - self.radius or self.y <= PADDING + self.radius:
            self.dy *= -1
        if self.x >= R_PAD.x - self.radius and R_PAD.y <= self.y <= R_PAD.y + PADDLE_HEIGHT:
            self.dx *= -1
        if self.x <= L_PAD.x + self.radius + PADDLE_WIDTH and L_PAD.y <= self.y <= L_PAD.y + PADDLE_HEIGHT:
            self.dx *= -1
        if self.x <= PADDING + 6 + self.radius and not L_HOL.y <= self.y <= L_HOL.y + HOLE_HEIGHT:
            self.dx *= -1
        if self.x >= PADDING + PLAY_WIDTH - 6 - self.radius and not R_HOL.y <= self.y <= R_HOL.y + HOLE_HEIGHT:
            self.dx *= -1


class Hole(abstracts.RectObjects):
    def __init__(self, x, y, width, height, side):
        super().__init__(x, y, width, height, side)
        self.width, self.height = width, height
        self.rect = pg.Surface((self.width, self.height))
        self.rect.fill(HOLE_COLOR)

    def draw(self, win):
        win.blit(self.rect, (self.x, self.y))

    def move(self, win):
        # PENDING
        pass


L_PAD = Paddle(10 + PADDING, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, LEFT)
R_PAD = Paddle(WIDTH - PADDLE_WIDTH - 10 - PADDING, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH,
               PADDLE_HEIGHT, RIGHT)
BALL_1 = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)
L_HOL = Hole(0, HEIGHT / 2 - HOLE_HEIGHT / 2, PADDING, HOLE_HEIGHT, LEFT)
R_HOL = Hole(WIDTH - PADDING, HEIGHT / 2 - HOLE_HEIGHT / 2, PADDING, + HOLE_HEIGHT, RIGHT)
