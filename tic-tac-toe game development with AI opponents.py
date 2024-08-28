import random
import pygame

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_WIDTH = 10

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

def print_board(board):
    screen.fill(WHITE)
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT), LINE_WIDTH)
    for i, cell in enumerate(board):
        if cell == "x":
            pygame.draw.line(screen, BLACK, ((i % 3) * WIDTH // 3 + 50, (i // 3) * HEIGHT // 3 + 50), (((i % 3) + 1) * WIDTH // 3 - 50, ((i // 3) + 1) * HEIGHT // 3 - 50), LINE_WIDTH)
            pygame.draw.line(screen, BLACK, ((i % 3) * WIDTH // 3 + 50, ((i // 3) + 1) * HEIGHT // 3 - 50), (((i % 3) + 1) * WIDTH // 3 - 50, (i // 3) * HEIGHT // 3 + 50), LINE_WIDTH)
        elif cell == "o":
            pygame.draw.circle(screen, BLACK, ((i % 3) * WIDTH // 3 + WIDTH // 6, (i // 3) * HEIGHT // 3 + HEIGHT // 6), WIDTH // 12, LINE_WIDTH)
    pygame.display.flip()

def initialize_board():
    return [""] * 9

def is_valid_move(board, move):
    return board[move] == ""

def is_winner(board, player):
    winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def ai_move(board):
    valid_moves = [i for i, x in enumerate(board) if x == ""]
    return random.choice(valid_moves)

def game_loop():
    board = initialize_board()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                user_move = (event.pos[0] // (WIDTH // 3)) + (event.pos[1] // (HEIGHT // 3)) * 3
                if is_valid_move(board, user_move):
                    board[user_move] = "x"
                    if is_winner(board, "x"):
                        print("You win!")
                        pygame.time.wait(2000)
                        pygame.quit()
                        return
                    ai_move_index = ai_move(board)
                    board[ai_move_index] = "o"
                    if is_winner(board, "o"):
                        print("AI wins!")
                        pygame.time.wait(2000)
                        pygame.quit()
                        return
        print_board(board)
        pygame.display.flip()

game_loop()