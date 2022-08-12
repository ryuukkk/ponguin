import pygame as pg

WIDTH, HEIGHT = 1100, 600
PADDING = 40
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('BURN PONG')

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_ELEMENTS_COLOR = (100, 100, 100)
PADDLE_HEIGHT = 100
PADDLE_WIDTH = 20
PADDLES = []
BALLS = []
BALL_RADIUS = 7
LEFT, RIGHT = -1, 1
GAME_STARTED = False


# Defining a paddle
class Paddle:
    COLOR = WHITE
    VEL = 4
    THETA = 2
    ROT_SPEED = 2

    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.rect = pg.Surface((self.width, self.height))
        PADDLES.append(self)

    def draw(self, win):
        win.blit(self.rect, (self.x, self.y))

    def move(self, up=True):
        if up and self.y > 0:
            self.y -= self.VEL
        elif up is False and self.y < HEIGHT - PADDLE_HEIGHT:
            self.y += self.VEL

    def rotate(self, win):
        # Implementation pending
        pass


# Defining the ball
class Ball:
    COLOR = BLACK

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.dx = 1
        self.dy = 1
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
        if self.x == right_paddle.x - self.radius and self.y in range(right_paddle.y, right_paddle.y + PADDLE_HEIGHT):
            self.dx *= -1
        if self.x == left_paddle.x + self.radius + PADDLE_WIDTH and self.y in range(left_paddle.y,
                                                                                    left_paddle.y + PADDLE_HEIGHT):
            self.dx *= -1


class Hole:
    def __init__(self, x, y, height):
        self.x, self.y = x, y
        self.height = height

    # PENDING IMPLEMENTATION:
    # 1. HOLE CLASS
    # 2. PLAY AREA
    # 3. ROTATE


# Creating Paddles and Ball
left_paddle = Paddle(10 + PADDING, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = Paddle(WIDTH - PADDLE_WIDTH - 10 - PADDING, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball1 = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)


# Handle paddle movement
def paddle_movement(user_input, left_paddle, right_paddle):
    if user_input[pg.K_w]:
        left_paddle.move()
    elif user_input[pg.K_s]:
        left_paddle.move(up=False)

    '''if user_input[pg.K_a]:
        left_paddle.rotate(WIN)
    elif user_input[pg.K_d]:
        left_paddle.rotate(WIN)'''

    if user_input[pg.K_UP]:
        right_paddle.move()
    elif user_input[pg.K_DOWN]:
        right_paddle.move(up=False)


# Handle ball movement
def ball_movement(user_input, ball):
    global GAME_STARTED

    if user_input[pg.K_SPACE]:
        GAME_STARTED = True

    if GAME_STARTED:
        ball.move()
        ball.detect_collision()

    if ball.is_off_screen():
        GAME_STARTED = False
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2


# Draw elements
def draw_game(win, paddles, balls):
    win.fill(WHITE)
    pg.draw.rect(WIN, BG_ELEMENTS_COLOR, (WIDTH // 2, 0, 1, HEIGHT))
    for paddle in paddles:
        paddle.draw(win)
    for ball in balls:
        ball.draw(win)

    pg.display.update()


# Main Loop
def main():
    run = True
    clock = pg.time.Clock()

    while run:
        clock.tick(FPS)  # to lock the fps at 60 in every computer
        user_input = pg.key.get_pressed()

        draw_game(WIN, PADDLES, BALLS)
        paddle_movement(user_input, left_paddle, right_paddle)
        ball_movement(user_input, ball1)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break

    pg.quit()


if __name__ == '__main__':
    main()
