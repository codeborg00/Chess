#bitboard implementation
import math

board = []

def import_FEN(fen_string, board):
    piece_dict = {
        "P" : 1,
        "N" : 2,
        "B" : 3,
        "R" : 4,
        "Q" : 5,
        "K" : 6,
    }

    fen_string = fen_string.split(" ")[0]

    x = 0
    y = 0
    for character in fen_string:
        if character == "/":
            continue
            

        elif character.isdigit():
            for i in range(int(character)):
                board.append((3, 3))

        else:
            if character.isupper():
                board.append((0, piece_dict[character]))
            else:
                character = character.upper()
                board.append((1, piece_dict[character]))
            

    return board



def squares_to_edge():
    num_squares_to_edge = [None] * 64
    for x in range(8):
        for y in range(8):
            north = y
            east = 7 - x
            south = 7 - y
            west = x

            north_east = min(north, east)
            south_east = min(south, east)
            south_west = min(south, west)
            north_west = min(north, west)
            

            list_index = x + y*8
            num_squares_to_edge[list_index] = [north, east, south, west, north_east, south_east, south_west, north_west]

    return num_squares_to_edge


    
def generate_moves2(board):
    move_list = []
    num_squares_to_edge = squares_to_edge()
    counter = 0
    for value in board:
        if value[1] == 4:
            move_list.append((counter, generate_rook_moves(counter, num_squares_to_edge)))

        if value[1] == 5:
            move_list.append((counter, generate_queen_moves(counter, num_squares_to_edge)))

        counter += 1

    return move_list

def generate_queen_moves(position, num_square_to_edge):
    moves = []

    #Test Code
    queen_moves =  (7, -7, 9, -9)

    if (position / 8 - math.floor(position / 8)) * 8 == 0:
        queen_moves = (-7, 9)
    if (position / 8 - math.floor(position / 8)) * 8 == 7:
        queen_moves = (-7, 7)

    
    for direction in range(len(queen_moves)):
        y, x = math.floor(position / 8.0), (position / 8 - math.floor(position / 8)) * 8
        dest_square = position

        while x <= 8 and x >= 0 and y >= 0 and y <= 8:
            y, x = math.floor(dest_square / 8.0) + 1, (dest_square / 8 - math.floor(dest_square / 8)) * 8 + 1
            dest_square = dest_square + queen_moves[direction]

            if dest_square > 63 or dest_square < 0 or x > 8 or y > 8:
                break
            if num_square_to_edge[dest_square][0] == 0 or num_square_to_edge[dest_square][1] == 0 or num_square_to_edge[dest_square][2] == 0 or num_square_to_edge[dest_square][3] == 0:
                if board[dest_square][0] == 3:
                    moves.append(dest_square)
                elif board[dest_square][0] != board[position][0]:
                    moves.append(dest_square)
                break
                    
                    
            if board[dest_square][0] == board[position][0]:
                break
            elif board[dest_square][0] == 3:
                moves.append(dest_square)
            elif board[dest_square][0] != board[position][0]:
                moves.append(dest_square)
                break
                    


    #End of Test Code

    queen_moves = [-8, 1, 8, -1]
    for i in range(4):
        dest_square = position
        while num_square_to_edge[position][i] > 0:
            dest_square = dest_square + queen_moves[i]
            num_square_to_edge[position][i] = num_square_to_edge[position][i] - 1

            if board[dest_square][0] == board[position][0]:
                break
            elif board[dest_square][0] == 3:
                moves.append(dest_square)

            elif board[dest_square][0] != board[position][0]:
                    moves.append(dest_square)
                    break


    return moves

def generate_rook_moves(position, num_square_to_edge):
    rook_moves = [-8, 1, 8, -1]
    moves = []
    for i in range(4):
        dest_square = position
        while num_square_to_edge[position][i] > 0:
            dest_square = dest_square + rook_moves[i]
            num_square_to_edge[position][i] = num_square_to_edge[position][i] - 1

            if board[dest_square][0] == board[position][0]:
                break
            elif board[dest_square][0] == 3:
                moves.append(dest_square)

            elif board[dest_square][0] != board[position][0]:
                    moves.append(dest_square)
                    break


    return moves

def generate_bishop_moves(position, num_square_to_edge):
    moves = []

    #Test Code
    bishop_moves =  (7, -7, 9, -9)

    if (position / 8 - math.floor(position / 8)) * 8 == 0:
        bishop_moves = (-7, 9)
    if (position / 8 - math.floor(position / 8)) * 8 == 7:
        bishop_moves = (-7, 7)

    
    for direction in range(len(bishop_moves)):
        y, x = math.floor(position / 8.0), (position / 8 - math.floor(position / 8)) * 8
        dest_square = position

        while x <= 8 and x >= 0 and y >= 0 and y <= 8:
            y, x = math.floor(dest_square / 8.0) + 1, (dest_square / 8 - math.floor(dest_square / 8)) * 8 + 1
            dest_square = dest_square + bishop_moves[direction]

            if dest_square > 63 or dest_square < 0 or x > 8 or y > 8:
                break
            if num_square_to_edge[dest_square][0] == 0 or num_square_to_edge[dest_square][1] == 0 or num_square_to_edge[dest_square][2] == 0 or num_square_to_edge[dest_square][3] == 0:
                if board[dest_square][0] == 3:
                    moves.append(dest_square)
                elif board[dest_square][0] != board[position][0]:
                    moves.append(dest_square)
                break
                    
                    
            if board[dest_square][0] == board[position][0]:
                break
            elif board[dest_square][0] == 3:
                moves.append(dest_square)
            elif board[dest_square][0] != board[position][0]:
                moves.append(dest_square)
                break
                    


    #End of Test Code
    print("Hello")
    print(moves)
    return moves



