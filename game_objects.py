import pygame as pg

WIDTH, HEIGHT = 1100, 600
PADDING = 40
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_ELEMENTS_COLOR = (200, 200, 200)
HOLE_COLOR = (0, 100, 100)
PADDLE_HEIGHT = 100
PADDLE_WIDTH = 20
PADDLES = []
BALLS = []
HOLES = []
BALL_RADIUS = 7
LEFT, RIGHT = -1, 1
GAME_STARTED = False
PLAY_WIDTH, PLAY_HEIGHT = WIDTH - 2 * PADDING, HEIGHT - 2 * PADDING


# Defining a paddle
class Paddle:
    COLOR = WHITE
    VEL = 10

    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.rect = pg.Surface((self.width, self.height))
        self.angle = 0
        self.rotating = False
        self.rotation_start_time = 0
        self.rotation_end_time = 0
        PADDLES.append(self)

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
class Ball:
    COLOR = HOLE_COLOR

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.dx = 10
        self.dy = 10
        BALLS.append(self)

    def draw(self, win):
        pg.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def is_off_screen(self):
        return self.x > WIDTH - PADDING or self.x < PADDING

    def detect_collision(self):
        if self.y >= HEIGHT - PADDING or self.y <= PADDING:
            self.dy *= -1
        if self.x >= R_PAD.x - self.radius and self.y in range(R_PAD.y, R_PAD.y + PADDLE_HEIGHT):
            self.dx *= -1
        if self.x <= L_PAD.x + self.radius + PADDLE_WIDTH and self.y in range(L_PAD.y,
                                                                                    L_PAD.y + PADDLE_HEIGHT):
            self.dx *= -1
        if self.x <= PADDING + 6 + self.radius and self.y not in range(L_HOL.y1, L_HOL.y2):
            self.dx *= -1
        if self.x >= PADDING + PLAY_WIDTH - 6 - self.radius and self.y not in range(R_HOL.y1, R_HOL.y2):
            self.dx *= -1


class Hole:
    def __init__(self, y1, y2, side=LEFT):
        self.y1, self.y2 = y1, y2
        self.side = side
        HOLES.append(self)

    def draw(self, win):
        if self.side == RIGHT:
            pg.draw.rect(win, HOLE_COLOR, (PADDING + PLAY_WIDTH - 6, PADDING, 6, self.y1 - PADDING))
            pg.draw.rect(win, HOLE_COLOR, (PADDING + PLAY_WIDTH - 6, self.y2, 6, HEIGHT - self.y2 - PADDING))
        else:
            pg.draw.rect(win, HOLE_COLOR, (PADDING, PADDING, 6, self.y1 - PADDING))
            pg.draw.rect(win, HOLE_COLOR, (PADDING, self.y2, 6, HEIGHT - self.y2 - PADDING))


L_PAD = Paddle(10 + PADDING, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
R_PAD = Paddle(WIDTH - PADDLE_WIDTH - 10 - PADDING, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH,
                      PADDLE_HEIGHT)
BALL_1 = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)
L_HOL = Hole(PADDING + int(PLAY_HEIGHT * 0.1), PADDING + int(PLAY_HEIGHT * 0.9), LEFT)
R_HOL = Hole(PADDING + int(PLAY_HEIGHT * 0.1), PADDING + int(PLAY_HEIGHT * 0.9), RIGHT)
