import pygame
import random
import sys
import time

# init pygame
pygame.init()

# screen config
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Block automat")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# pygame configs
group_size = 2
cell_size = 10 # rectangle size 30
gap_size = 5  # gap between rectangles 15
left_margin = 20  # margin from the left 40
right_margin = 20  # margin from the right 40
top_margin = 20  # margin from the top 40
bottom_margin = 20  # margin from the bottom 40

# the grids rows and collomns - calculated assuming we fill the grid with as manny cells as possible
num_row = (screen_width - right_margin - left_margin + gap_size) // (cell_size + gap_size)
num_col = (screen_height - top_margin - bottom_margin + gap_size) // (cell_size + gap_size)

# initialize the board and print the lines
def initiate_board(board):
    # draw the squares and randomly choose filled or not. 50%
    for row in range(top_margin, screen_height - bottom_margin,
                     cell_size + gap_size):  # Adjusted for top margin and bottom margin
        for col in range(left_margin, screen_width - right_margin,
                         cell_size + gap_size):  # Adjusted for left and right margins
            if col + cell_size <= screen_width - right_margin and row+cell_size <= screen_height - bottom_margin:
                rand = random.randint(1,4)

                row_index = (row - top_margin) // (cell_size + gap_size)
                col_index = (col - left_margin) // (cell_size + gap_size)
                board[row_index][col_index] = 1 # can be 0 also

                if board[row_index][col_index] == 1:
                    pygame.draw.rect(screen, black, (col, row, cell_size, cell_size))  # filled rectangle
                else:
                    pygame.draw.rect(screen, black, (col, row, cell_size, cell_size), 1)

    # dashed row lines
    for row in range(top_margin + cell_size + int(gap_size / 2), screen_height - bottom_margin,
                     (cell_size + gap_size) * group_size):  # Horizontal lines
        for square in range(0, (screen_width - right_margin - left_margin + gap_size) // (cell_size + gap_size)):
            square_start = left_margin + square * (cell_size + gap_size)
            for dash in range(5):  # 4 dashes
                dash_start = square_start + dash * (cell_size // 4)
                dash_end = dash_start + cell_size // 8
                pygame.draw.line(screen, red, (dash_start, row), (min(dash_end, square_start + cell_size), row), 2)

    # dashed col lines
    for col in range(left_margin + cell_size + int(gap_size / 2), screen_width - right_margin,
                     (cell_size + gap_size) * group_size):  # Vertical lines
        for square in range(0, (screen_height - top_margin - bottom_margin + gap_size) // (cell_size + gap_size)):
            square_start = top_margin + square * (cell_size + gap_size)
            for dash in range(5):  # 4 dashes
                dash_start = square_start + dash * (cell_size // 4)
                dash_end = dash_start + cell_size // 8
                pygame.draw.line(screen, red, (col, dash_start), (col, min(dash_end, square_start + cell_size)), 2)

    # blue row lines
    for row in range(top_margin + 2 * cell_size + int(3 * gap_size / 2), screen_height - bottom_margin,
                     (cell_size + gap_size) * group_size):  # Horizontal lines
        pygame.draw.line(screen, blue, (left_margin, row), (screen_width - right_margin, row),
                         2)  # Horizontal blue line

    # blue col lines
    for col in range(left_margin + 2* cell_size + int(3 * gap_size / 2), screen_width - right_margin,
                     (cell_size + gap_size) * group_size):  # Vertical lines
        pygame.draw.line(screen, blue, (col, top_margin), (col, screen_height - bottom_margin),
                         2)  # Vertical blue line

# print the current board and lines
def print_board(board):
    # draw the squares and randomly choose filled or not. 50%
    for row in range(top_margin, screen_height - bottom_margin,
                     cell_size + gap_size):  # Adjusted for top margin and bottom margin
        for col in range(left_margin, screen_width - right_margin,
                         cell_size + gap_size):  # Adjusted for left and right margins
            if col + cell_size <= screen_width - right_margin and row+cell_size <= screen_height - bottom_margin:
                row_index = (row - top_margin) // (cell_size + gap_size)
                col_index = (col - left_margin) // (cell_size + gap_size)

                if board[row_index][col_index] == 1:
                    pygame.draw.rect(screen, black, (col, row, cell_size, cell_size))  # filled rectangle
                else:
                    pygame.draw.rect(screen, black, (col, row, cell_size, cell_size), 1)

    # dashed row lines
    for row in range(top_margin + cell_size + int(gap_size / 2), screen_height - bottom_margin,
                     (cell_size + gap_size) * group_size):  # Horizontal lines
        for square in range(0, (screen_width - right_margin - left_margin + gap_size) // (cell_size + gap_size)):
            square_start = left_margin + square * (cell_size + gap_size)
            for dash in range(5):  # 4 dashes
                dash_start = square_start + dash * (cell_size // 4)
                dash_end = dash_start + cell_size // 8
                pygame.draw.line(screen, red, (dash_start, row), (min(dash_end, square_start + cell_size), row), 2)

    # dashed col lines
    for col in range(left_margin + cell_size + int(gap_size / 2), screen_width - right_margin,
                     (cell_size + gap_size) * group_size):  # Vertical lines
        for square in range(0, (screen_height - top_margin - bottom_margin + gap_size) // (cell_size + gap_size)):
            square_start = top_margin + square * (cell_size + gap_size)
            for dash in range(5):  # 4 dashes
                dash_start = square_start + dash * (cell_size // 4)
                dash_end = dash_start + cell_size // 8
                pygame.draw.line(screen, red, (col, dash_start), (col, min(dash_end, square_start + cell_size)), 2)

    # blue row lines
    for row in range(top_margin + 2 * cell_size + int(3 * gap_size / 2), screen_height - bottom_margin,
                     (cell_size + gap_size) * group_size):  # Horizontal lines
        pygame.draw.line(screen, blue, (left_margin, row), (screen_width - right_margin, row),
                         2)  # Horizontal blue line

    # blue col lines
    for col in range(left_margin + 2* cell_size + int(3 * gap_size / 2), screen_width - right_margin,
                     (cell_size + gap_size) * group_size):  # Vertical lines
        pygame.draw.line(screen, blue, (col, top_margin), (col, screen_height - bottom_margin),
                         2)  # Vertical blue line

# handle odd gen - blue blocks
def handle_odd_gen(board):
    # go over the top left corner of the blue 2x2
    for row in range(0,num_row - 1, 2):
        for col in range(0, num_col - 1, 2):
            handle_block(board, row, col)

# handle even gen - red blocks and wraparound
def handle_even_gen(board):
    # go over the top left corner of the red 2x2 - no wrap part
    for row in range(1,num_row - 1, 2):
        for col in range(1, num_col - 1, 2):
            handle_block(board, row, col)

    # wrap
    if wraparound==1:
        # the 4 corners
        handle_block_pos(board, num_row - 1, num_col - 1, num_row-1, 0, 0, 0, 0, num_col - 1)

        # the top and bottom blocks: bottom left
        for col in range(1, num_col - 1, 2):
            handle_block_pos(board, num_row - 1, col, num_row - 1, col + 1, 0, col + 1, 0, col)

        # the left and right blocks:
        for row in range(1, num_row - 1, 2):
            handle_block_pos(board, row, num_col - 1, row, 0, row + 1, 0, row + 1, num_col - 1)


# gets a 2x2 block by its top left corner and handles it according to the rules
def handle_block(board, corner_row, corner_col):
    global changing
    num = board[corner_row][corner_col] + board[corner_row][corner_col + 1] + board[corner_row + 1][corner_col] + board[corner_row + 1][corner_col + 1]
    if num==2:
        return
    else:
        original =[[0 for _ in range(2)] for _ in range(2)]

        # not on every square
        for r in range(2):
            for c in range(2):
                original[r][c] = board[corner_row + r][corner_col + c]
                board[corner_row + r][corner_col + c] = board[corner_row + r][corner_col + c] ^ 1
        if num==3:
            # swap 180
            temp = board[corner_row][corner_col]
            board[corner_row][corner_col] = board[corner_row + 1][corner_col + 1]
            board[corner_row + 1][corner_col + 1]=temp

            temp = board[corner_row][corner_col + 1]
            board[corner_row][corner_col + 1] = board[corner_row + 1][corner_col]
            board[corner_row + 1][corner_col] = temp

        # update changing
        for r in range(2):
            for c in range(2):
                if  original[r][c] != board[corner_row + r][corner_col + c]:
                    changing = changing + 1


# gets a 2x2 block by all the 4 positions (top left and clockwise) and handles it according to the rules
def handle_block_pos(board, row1, col1, row2, col2, row3, col3, row4, col4):
    global changing
    num = board[row1][col1] + board[row2][col2] + board[row3][col3] + board[row4][col4]
    if num == 2:
        return
    else:
        original = [[0 for _ in range(2)] for _ in range(2)]

        original[0][0] = board[row1][col1]
        original[0][1] = board[row2][col2]
        original[1][0] = board[row3][col3]
        original[1][1] = board[row4][col4]

        # not on every square
        for r,c in [(row1, col1),(row2,col2),(row3,col3),(row4,col4)]:
            board[r][c] = board[r][c] ^ 1
        if num==3:
            # swap 180
            temp = board[row1][col1]
            board[row1][col1] = board[row3][col3]
            board[row3][col3]=temp

            temp = board[row2][col2]
            board[row2][col2] = board[row4][col4]
            board[row4][col4] = temp

        # update changing
        if original[0][0] != board[row1][col1]:
            changing = changing + 1
        if original[0][1] != board[row2][col2]:
            changing = changing + 1
        if original[1][1] != board[row3][col3]:
            changing = changing + 1
        if original[1][0] != board[row4][col4]:
            changing = changing + 1

# Main game loop
running = True

# initialize to 0 for now
board = [[0 for _ in range(num_col)] for _ in range(num_row)]

# config params
update_time = 0 # update frequency
counter = 0

gen = 0 # gen management
max_gen = 250

# wraparound, assumed to be 0 or 1
wraparound = int(input("Would you like to have wraparound:\n"
                       "Enter 0 or 1 accordingly\n"))

stability = [0 for _ in range(max_gen + 1)]
changing = 0

# initialize the board
screen.fill(white)
initiate_board(board)

# run the simulation
while running and gen <= max_gen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update with the current gen
    if counter == update_time or update_time == 0:
        changing = 0
        if gen % 2 == 1:
            handle_odd_gen(board)
        else:
            handle_even_gen(board)

        stability[gen] = changing / (num_row * num_col)
        gen = gen + 1
        counter = 0


    counter += 1

    # redraw
    screen.fill(white)
    print_board(board)

    # display
    pygame.display.flip()

    time.sleep(0.35) # for convenience
print(f"The stability table: {stability}")
pygame.quit()
sys.exit()
