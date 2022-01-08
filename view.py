import pygame, math, os

WIDTH = 800
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (232, 235, 239)
BLACK = (125, 135, 150)
RED = (255, 0, 0)

WHITE_PAWN = pygame.image.load(os.path.join('Assets', 'white_pawn.png'))
BLACK_PAWN = pygame.image.load(os.path.join('Assets', 'black_pawn.png'))
WHITE_KNIGHT = pygame.image.load(os.path.join('Assets', 'white_knight.png'))
BLACK_KNIGHT = pygame.image.load(os.path.join('Assets', 'black_knight.png'))
WHITE_BISHOP = pygame.image.load(os.path.join('Assets', 'white_bishop.png'))
BLACK_BISHOP = pygame.image.load(os.path.join('Assets', 'black_bishop.png'))
WHITE_ROOK = pygame.image.load(os.path.join('Assets', 'white_rook.png'))
BLACK_ROOK = pygame.image.load(os.path.join('Assets', 'black_rook.png'))
WHITE_QUEEN = pygame.image.load(os.path.join('Assets', 'white_queen.png'))
BLACK_QUEEN = pygame.image.load(os.path.join('Assets', 'black_queen.png'))
WHITE_KING = pygame.image.load(os.path.join('Assets', 'white_king.png'))
BLACK_KING = pygame.image.load(os.path.join('Assets', 'black_king.png'))
WHITE_ATTACKED = pygame.image.load(os.path.join('Assets', 'white_attacked.png'))
BLACK_ATTACKED = pygame.image.load(os.path.join('Assets', 'black_attacked.png'))


def draw_board():

    px_column = 0
    px_row = 0

    for x in range(8):
        for y in range(8):
            if (x + y) % 2 != 0:
                pygame.draw.rect(SCREEN, BLACK, (px_column, px_row, 100, 100))
            
            else:
                pygame.draw.rect(SCREEN, WHITE, (px_column, px_row, 100, 100))
                   
            px_row += 100

        px_column += 100
        px_row = 0
    pygame.display.update()

def render_pieces(board):
    counter = 0
    for value in board:
        if value[0] == 0 and value[1] == 1:
            position = (math.floor(counter / 8.0), (counter / 8 - math.floor(counter / 8)) * 8)
            SCREEN.blit(WHITE_PAWN, (position[1]*100, position[0]*100))

        if value[0] == 1 and value[1] == 1:
            position = (math.floor(counter / 8.0), (counter / 8 - math.floor(counter / 8)) * 8)
            SCREEN.blit(BLACK_PAWN, (position[1]*100, position[0]*100))

        if value[0] == 0 and value[1] == 2:
            position = (math.floor(counter / 8.0), (counter / 8 - math.floor(counter / 8)) * 8)
            SCREEN.blit(WHITE_KNIGHT, (position[1]*100, position[0]*100))

        if value[0] == 1 and value[1] == 2:
            position = (math.floor(counter / 8.0), (counter / 8 - math.floor(counter / 8)) * 8)
            SCREEN.blit(BLACK_KNIGHT, (position[1]*100, position[0]*100))
    
        if value[0] == 0 and value[1] == 3:
            position = (math.floor(counter / 8.0), (counter / 8 - math.floor(counter / 8)) * 8)
            SCREEN.blit(WHITE_BISHOP, (position[1]*100, position[0]*100))

        if value[0] == 1 and value[1] == 3:
            position = (math.floor(counter / 8.0), (counter / 8 - math.floor(counter / 8)) * 8)
            SCREEN.blit(BLACK_BISHOP, (position[1]*100, position[0]*100))

        if value[0] == 0 and value[1] == 4:
            position = (math.floor(counter / 8.0), (counter / 8 - math.floor(counter / 8)) * 8)
            SCREEN.blit(WHITE_ROOK, (position[1]*100, position[0]*100))

        if value[0] == 1 and value[1] == 4:
            position = (math.floor(counter / 8.0), (counter / 8 - math.floor(counter / 8)) * 8)
            SCREEN.blit(BLACK_ROOK, (position[1]*100, position[0]*100))

        if value[0] == 0 and value[1] == 5:
            position = (math.floor(counter / 8.0), (counter / 8 - math.floor(counter / 8)) * 8)
            SCREEN.blit(WHITE_QUEEN, (position[1]*100, position[0]*100))

        if value[0] == 1 and value[1] == 5:
            position = (math.floor(counter / 8.0), (counter / 8 - math.floor(counter / 8)) * 8)
            SCREEN.blit(BLACK_QUEEN, (position[1]*100, position[0]*100))



        if value[0] == 0 and value[1] == 6:
            position = (math.floor(counter / 8.0), (counter / 8 - math.floor(counter / 8)) * 8)
            SCREEN.blit(WHITE_KING, (position[1]*100, position[0]*100))


        if value[0] == 1 and value[1] == 6:
            position = (math.floor(counter / 8.0), (counter / 8 - math.floor(counter / 8)) * 8)
            SCREEN.blit((BLACK_KING), (position[1]*100, position[0]*100))

        counter += 1


    pygame.display.update()



def highlight_square(board, move_list):
    for i in range(64):
        for index in range(len(move_list)):
            for value2 in move_list[index][1]:
                if i == value2:
                    y, x = math.floor(i / 8.0), (i / 8 - math.floor(i / 8)) * 8
                    if (x + y) % 2 != 0:
                        SCREEN.blit((BLACK_ATTACKED), (x*100, y*100))
            
                    else:
                        SCREEN.blit((WHITE_ATTACKED), (x*100, y*100))



    pygame.display.update()


