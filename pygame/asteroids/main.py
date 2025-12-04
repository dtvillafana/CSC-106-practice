import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

# Game settings
SHIP_SIZE = 15
SHIP_ACCELERATION = 0.2
SHIP_ROTATION_SPEED = 5
SHIP_FRICTION = 0.99
MAX_SPEED = 8
BULLET_SPEED = 10
BULLET_LIFETIME = 60
ASTEROID_SPEEDS = {"large": 1.5, "medium": 2.5, "small": 3.5}
ASTEROID_SIZES = {"large": 40, "medium": 25, "small": 15}

# Set up display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)


class Ship:
    def __init__(self):
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.angle = 0
        self.vel_x = 0
        self.vel_y = 0
        self.alive = True

    def rotate(self, direction):
        self.angle += direction * SHIP_ROTATION_SPEED

    def accelerate(self):
        rad = math.radians(self.angle)
        self.vel_x += math.cos(rad) * SHIP_ACCELERATION
        self.vel_y += math.sin(rad) * SHIP_ACCELERATION

        # Limit speed
        speed = math.sqrt(self.vel_x**2 + self.vel_y**2)
        if speed > MAX_SPEED:
            self.vel_x = (self.vel_x / speed) * MAX_SPEED
            self.vel_y = (self.vel_y / speed) * MAX_SPEED

    def update(self):
        # Apply friction
        self.vel_x *= SHIP_FRICTION
        self.vel_y *= SHIP_FRICTION

        # Move
        self.x += self.vel_x
        self.y += self.vel_y

        # Wrap around screen
        if self.x < 0:
            self.x = WINDOW_WIDTH
        elif self.x > WINDOW_WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = WINDOW_HEIGHT
        elif self.y > WINDOW_HEIGHT:
            self.y = 0

    def draw(self):
        if not self.alive:
            return

        rad = math.radians(self.angle)

        # Ship triangle points
        points = [
            (self.x + math.cos(rad) * SHIP_SIZE, self.y + math.sin(rad) * SHIP_SIZE),
            (
                self.x + math.cos(rad + 2.5) * SHIP_SIZE * 0.6,
                self.y + math.sin(rad + 2.5) * SHIP_SIZE * 0.6,
            ),
            (
                self.x + math.cos(rad - 2.5) * SHIP_SIZE * 0.6,
                self.y + math.sin(rad - 2.5) * SHIP_SIZE * 0.6,
            ),
        ]

        pygame.draw.polygon(screen, WHITE, points, 2)

    def get_position(self):
        return (self.x, self.y)


class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        rad = math.radians(angle)
        self.vel_x = math.cos(rad) * BULLET_SPEED
        self.vel_y = math.sin(rad) * BULLET_SPEED
        self.lifetime = BULLET_LIFETIME
        self.active = True

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.lifetime -= 1

        # Wrap around screen
        if self.x < 0:
            self.x = WINDOW_WIDTH
        elif self.x > WINDOW_WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = WINDOW_HEIGHT
        elif self.y > WINDOW_HEIGHT:
            self.y = 0

        if self.lifetime <= 0:
            self.active = False

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 2)

    def get_position(self):
        return (self.x, self.y)


class Asteroid:
    def __init__(self, x, y, size="large"):
        self.x = x
        self.y = y
        self.size = size
        self.radius = ASTEROID_SIZES[size]

        angle = random.uniform(0, 2 * math.pi)
        speed = ASTEROID_SPEEDS[size]
        self.vel_x = math.cos(angle) * speed
        self.vel_y = math.sin(angle) * speed

        self.active = True

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y

        # Wrap around screen
        if self.x < -self.radius:
            self.x = WINDOW_WIDTH + self.radius
        elif self.x > WINDOW_WIDTH + self.radius:
            self.x = -self.radius
        if self.y < -self.radius:
            self.y = WINDOW_HEIGHT + self.radius
        elif self.y > WINDOW_HEIGHT + self.radius:
            self.y = -self.radius

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius, 2)

    def get_position(self):
        return (self.x, self.y)

    def split(self):
        if self.size == "large":
            return [Asteroid(self.x, self.y, "medium") for _ in range(2)]
        elif self.size == "medium":
            return [Asteroid(self.x, self.y, "small") for _ in range(2)]
        return []


def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)


def check_collision(obj1, obj2, radius1, radius2):
    return distance(obj1.get_position(), obj2.get_position()) < radius1 + radius2


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
        f"Final Score: {score}",
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


def create_initial_asteroids(num=5):
    asteroids = []
    for _ in range(num):
        # Spawn away from center
        while True:
            x = random.randint(0, WINDOW_WIDTH)
            y = random.randint(0, WINDOW_HEIGHT)
            if distance((x, y), (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)) > 150:
                break
        asteroids.append(Asteroid(x, y, "large"))
    return asteroids


def main():
    while True:
        # Initialize game
        ship = Ship()
        bullets = []
        asteroids = create_initial_asteroids(5)
        score = 0
        shoot_cooldown = 0

        # Game loop
        running = True
        while running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if (
                        event.key == pygame.K_SPACE
                        and shoot_cooldown == 0
                        and ship.alive
                    ):
                        bullets.append(Bullet(ship.x, ship.y, ship.angle))
                        shoot_cooldown = 15
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            if ship.alive:
                # Continuous key presses
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    ship.rotate(-1)
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    ship.rotate(1)
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    ship.accelerate()

            # Update cooldown
            if shoot_cooldown > 0:
                shoot_cooldown -= 1

            # Update ship
            ship.update()

            # Update bullets
            for bullet in bullets[:]:
                bullet.update()
                if not bullet.active:
                    bullets.remove(bullet)

            # Update asteroids
            for asteroid in asteroids:
                asteroid.update()

            # Check bullet-asteroid collisions
            for bullet in bullets[:]:
                for asteroid in asteroids[:]:
                    if check_collision(bullet, asteroid, 2, asteroid.radius):
                        bullet.active = False
                        if bullet in bullets:
                            bullets.remove(bullet)

                        # Split asteroid
                        new_asteroids = asteroid.split()
                        asteroids.remove(asteroid)
                        asteroids.extend(new_asteroids)

                        # Update score
                        if asteroid.size == "large":
                            score += 20
                        elif asteroid.size == "medium":
                            score += 50
                        elif asteroid.size == "small":
                            score += 100
                        break

            # Check ship-asteroid collisions
            if ship.alive:
                for asteroid in asteroids:
                    if check_collision(ship, asteroid, SHIP_SIZE, asteroid.radius):
                        ship.alive = False
                        running = False

            # Spawn new asteroids if all destroyed
            if len(asteroids) == 0:
                asteroids = create_initial_asteroids(min(5 + score // 500, 10))

            # Drawing
            screen.fill(BLACK)

            # Draw game objects
            ship.draw()
            for bullet in bullets:
                bullet.draw()
            for asteroid in asteroids:
                asteroid.draw()

            # Draw score and lives
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
