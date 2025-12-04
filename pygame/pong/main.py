import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 90
BALL_SIZE = 15
PADDLE_SPEED = 6
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Font for score
font = pygame.font.Font(None, 74)


class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 0

    def move(self):
        self.rect.y += self.speed
        # Keep paddle on screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(
            WINDOW_WIDTH // 2 - BALL_SIZE // 2,
            WINDOW_HEIGHT // 2 - BALL_SIZE // 2,
            BALL_SIZE,
            BALL_SIZE,
        )
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off top and bottom
        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

    def reset(self):
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.speed_x *= -1
        self.speed_y = BALL_SPEED_Y


# Create game objects
left_paddle = Paddle(30, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2)
right_paddle = Paddle(
    WINDOW_WIDTH - 30 - PADDLE_WIDTH, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
)
ball = Ball()

# Scores
left_score = 0
right_score = 0

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_paddle.speed = -PADDLE_SPEED
            if event.key == pygame.K_s:
                left_paddle.speed = PADDLE_SPEED
            if event.key == pygame.K_UP:
                right_paddle.speed = -PADDLE_SPEED
            if event.key == pygame.K_DOWN:
                right_paddle.speed = PADDLE_SPEED

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                left_paddle.speed = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                right_paddle.speed = 0

    # Update game objects
    left_paddle.move()
    right_paddle.move()
    ball.move()

    # Ball collision with paddles
    if ball.rect.colliderect(left_paddle.rect) or ball.rect.colliderect(
        right_paddle.rect
    ):
        ball.speed_x *= -1

    # Ball goes out of bounds
    if ball.rect.left <= 0:
        right_score += 1
        ball.reset()
    if ball.rect.right >= WINDOW_WIDTH:
        left_score += 1
        ball.reset()

    # Drawing
    screen.fill(BLACK)

    # Draw center line
    for i in range(0, WINDOW_HEIGHT, 20):
        pygame.draw.rect(screen, WHITE, (WINDOW_WIDTH // 2 - 2, i, 4, 10))

    # Draw paddles and ball
    left_paddle.draw()
    right_paddle.draw()
    ball.draw()

    # Draw scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WINDOW_WIDTH // 4, 30))
    screen.blit(right_text, (3 * WINDOW_WIDTH // 4 - right_text.get_width(), 30))

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
