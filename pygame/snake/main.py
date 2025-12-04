import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GREEN = (0, 200, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)


class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)

        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, new_direction):
        # Prevent reversing into itself
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def check_collision(self):
        head_x, head_y = self.body[0]

        # Check wall collision
        if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
            return True

        # Check self collision
        if self.body[0] in self.body[1:]:
            return True

        return False

    def draw(self):
        for i, segment in enumerate(self.body):
            x, y = segment
            color = GREEN if i == 0 else DARK_GREEN
            pygame.draw.rect(
                screen,
                color,
                (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE - 2, GRID_SIZE - 2),
            )


class Food:
    def __init__(self):
        self.position = self.randomize_position()

    def randomize_position(self):
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        return (x, y)

    def respawn(self, snake_body):
        while True:
            self.position = self.randomize_position()
            if self.position not in snake_body:
                break

    def draw(self):
        x, y = self.position
        pygame.draw.rect(
            screen, RED, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE - 2, GRID_SIZE - 2)
        )


def draw_text(text, font, color, x, y, center=False):
    text_surface = font.render(text, True, color)
    if center:
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)
    else:
        screen.blit(text_surface, (x, y))


def game_over_screen(score):
    screen.fill(BLACK)
    draw_text(
        "GAME OVER",
        game_over_font,
        RED,
        WINDOW_WIDTH // 2,
        WINDOW_HEIGHT // 2 - 50,
        center=True,
    )
    draw_text(
        f"Score: {score}",
        font,
        WHITE,
        WINDOW_WIDTH // 2,
        WINDOW_HEIGHT // 2 + 20,
        center=True,
    )
    draw_text(
        "Press SPACE to play again or ESC to quit",
        font,
        WHITE,
        WINDOW_WIDTH // 2,
        WINDOW_HEIGHT // 2 + 80,
        center=True,
    )
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False
        clock.tick(FPS)


def main():
    while True:
        # Initialize game objects
        snake = Snake()
        food = Food()
        score = 0

        # Game loop
        running = True
        while running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        snake.change_direction(UP)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        snake.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        snake.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        snake.change_direction(RIGHT)
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            # Update snake
            snake.move()

            # Check if snake ate food
            if snake.body[0] == food.position:
                snake.grow = True
                score += 1
                food.respawn(snake.body)

            # Check collision
            if snake.check_collision():
                running = False

            # Drawing
            screen.fill(BLACK)

            # Draw grid (optional)
            for x in range(0, WINDOW_WIDTH, GRID_SIZE):
                pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, WINDOW_HEIGHT))
            for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
                pygame.draw.line(screen, (40, 40, 40), (0, y), (WINDOW_WIDTH, y))

            # Draw game objects
            snake.draw()
            food.draw()

            # Draw score
            draw_text(f"Score: {score}", font, WHITE, 10, 10)

            # Update display
            pygame.display.flip()
            clock.tick(FPS)

        # Game over
        if not game_over_screen(score):
            break

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
