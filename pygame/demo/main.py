import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 800
ROWS = 3
COLS = 3
BLACK = (0,0,0)
WHITE = (255,255,255)
LINETHICKNESS = 10
SQUARE_SIZE = WIDTH // 3
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tictactoe")
clock = pygame.time.Clock()

rect = pygame.Rect(100, 100, 200, 150)
running = True

def move_rectangle(rect: pygame.Rect, x_delta, y_delta):
    return rect.move(x_delta, y_delta)

def draw_game_board():
    pygame.draw.line(
        screen,
        WHITE,
        (WIDTH // 3, 0),
        (WIDTH // 3, HEIGHT),
        LINETHICKNESS
    )
    pygame.draw.line(
        screen,
        WHITE,
        (WIDTH // 3 * 2, 0),
        (WIDTH // 3 * 2, HEIGHT),
        LINETHICKNESS
    )
    pygame.draw.line(
        screen,
        WHITE,
        (0, HEIGHT // 3),
        (WIDTH, HEIGHT // 3),
        LINETHICKNESS
    )
    pygame.draw.line(
        screen,
        WHITE,
        (0, HEIGHT // 3 * 2),
        (WIDTH, HEIGHT // 3 * 2),
        LINETHICKNESS
    )

player = 1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def mark_square(row, col, player):
    board[row][col] = player


def square_available(row, col):
    return board[row][col] == 0


def check_win(player):
    # check rows for win
    for row in range(ROWS):
        if all([square == player for square in board[row]]):
            return True
    # check columns for win
    for col in range(COLS):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # check diagonals for win
    if all([board[x][x] == player for x in range(3)]):
        return True
    if all([board[x][3 - x - 1] == player for x in range(3)]):
        return True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            clicked_row = mouse_y // SQUARE_SIZE
            clicked_col = mouse_x // SQUARE_SIZE
            if square_available(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    running = False
                    print(f"Player {player} wins!")
                player = 2 if player == 1 else 1

    screen.fill(BLACK)
    draw_game_board()


    pygame.display.flip()
    clock.tick(FPS)
    [print(x) for x in board]
    print()

pygame.quit()
sys.exit()
