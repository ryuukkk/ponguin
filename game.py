import time
import cProfile
from game_objects import *
import abstracts


# PENDING IMPLEMENTATIONS:
# 1. PADDLE ROTATION AND PUSH
# 2. CONTROL SET
# 3. SCOREBOARD AND WINNING
# 4. HOLE MOVEMENT AND BONUSES
# 5. MUSIC AND SOUNDS
# 6. UI
# 7. BALL ADVANCED MOVEMENT
# 8. DIFFERENT PADDLES AND ARENAS
# 9. ONLINE MULTIPLAYER
# 10. PLAYER DATABASE
# 11. CONTROLLING THROUGH COMPUTER VISION

# DUE TODAY
# 1. SCOREBOARD AND WINNING

def setup():
    global WIN
    WIN = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('BURN PONG')


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

    if user_input[pg.K_LEFT]:
        right_paddle.rotate(clockwise=True)


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
def draw_game(win, paddles, balls, holes):
    win.fill(WHITE)
    pg.draw.rect(WIN, BG_ELEMENTS_COLOR, (PADDING, PADDING, PLAY_WIDTH, PLAY_HEIGHT))
    pg.draw.rect(WIN, WHITE, (WIDTH // 2, 0, 1, HEIGHT))
    for paddle in paddles:
        paddle.draw(win)
    for ball in balls:
        ball.draw(win)
    for hole in holes:
        hole.draw(win)

    pg.display.update()


# Main Loop
@abstracts.profiling
def main():
    run = True
    clock = pg.time.Clock()
    setup()
    while run:
        clock.tick(FPS)  # to lock the fps at 60 in every computer
        user_input = pg.key.get_pressed()

        draw_game(WIN, Paddle.instances, Ball.instances, Hole.instances)
        paddle_movement(user_input, L_PAD, R_PAD)
        ball_movement(user_input, BALL_1)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break

    pg.quit()


if __name__ == '__main__':
    main()