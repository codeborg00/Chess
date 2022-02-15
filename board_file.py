#bitboard implementation
import math

board = []
knight_moves = [
    [10, 17], [11, 16, 18], [8, 12, 17, 19], [9, 13, 18, 20], [10, 14, 19, 21], [11, 15, 20, 22], [12, 21, 23], [13, 22],
    [2, 18, 25], [3, 19, 24, 26], [0, 4, 16, 20, 25, 27], [1, 5, 17, 21, 26, 28], [2, 6, 18, 22, 27, 29], [3, 7, 19, 23, 28, 30], [4, 20, 29, 31], [5, 21, 30],
    [1, 10, 26, 33], [0, 2, 11, 27, 32, 34], [1, 3, 8, 12, 24, 28, 33, 35], [2, 4, 9, 13, 25, 29, 34, 36], [3, 5, 10, 14, 26, 30, 35, 37], [4, 6, 11, 15, 27, 31, 36, 38], [5, 7, 12, 28, 37, 39], [6, 13, 29, 38],
    [9, 18, 34, 41], [8, 10, 19, 35, 40, 42], [9, 11, 16, 20, 32, 36, 41, 43], [10, 12, 17, 21, 33, 37, 42, 44], [11, 13, 18, 22, 34, 38, 43, 45], [12, 14, 19, 23, 35, 39, 44, 46], [13, 15, 20, 36, 45, 47], [14, 46],
    [17, 26, 42, 49], [16, 18, 27, 43, 48, 50], [17, 19, 24, 28, 40, 44, 49, 51], [18, 20, 25, 29, 41, 45, 50, 52], [19, 21, 26, 30, 42, 46, 51, 53], [20, 22, 27, 31, 43, 47, 52, 54], [21, 23, 29, 44, 53, 55], [22, 29, 45, 54],
    [25, 34, 50, 57], [24, 26, 35, 51, 56, 58], [25, 27, 32, 36, 48, 52, 57, 58], [26, 28, 33, 37, 49, 53, 58, 60], [27, 29, 34, 38, 50, 54, 59, 61], [28, 30, 35, 39, 51, 55, 60, 62], [29, 31, 36, 52, 61, 63], [30, 37, 53, 62],
    [33, 42, 58], [32, 34, 43, 59], [33, 35, 40, 44, 56, 60], [34, 36, 41, 45, 57, 61], [35, 37, 42, 46, 58, 62], [36, 38, 43, 47, 59, 63], [37, 39, 44, 60], [38, 45, 61],
    [41, 50], [40, 42, 51], [41, 43, 48, 52], [42, 44, 49, 53], [43, 45, 50, 54], [44, 46, 51, 55], [45, 47, 52], [46, 53],
]

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
                board.append((-1, -1))

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
    king_dest = []
    move_list = []
    num_squares_to_edge = squares_to_edge()
    counter = 0
    for value in board:
        if value[1] == 1:
            move_list.append(((board[counter][0], counter), generate_pawn_moves(counter, num_squares_to_edge)))
        if value[1] == 2:
            move_list.append(((board[counter][0], counter), generate_knight_moves(counter)))
        if value[1] == 3:
            move_list.append(((board[counter][0], counter), generate_sliding_piece_moves(3, counter, num_squares_to_edge)))

        if value[1] == 4:
            move_list.append(((board[counter][0], counter), generate_sliding_piece_moves(4, counter, num_squares_to_edge)))

        if value[1] == 5:
            move_list.append(((board[counter][0], counter), generate_sliding_piece_moves(5, counter, num_squares_to_edge)))
        
        if value[1] == 6:
            move_list.append(((board[counter][0], counter), generate_king_moves(counter, num_squares_to_edge)))
            king_dest.append(generate_king_moves(counter, num_squares_to_edge))


        

        counter += 1


    
    white_false, black_false = check_move_validity(king_dest, move_list)
    for square in move_list:
        if board[square[0][1]][1] == 6 and board[square[0][1]][0] == 0:
            for deletable in white_false:
                print(deletable)
                move_list[move_list.index(square)][1].remove(deletable)


        if board[square[0][1]][1] == 6 and board[square[0][1]][0] == 1:
            for deletable in black_false:
                print(deletable)
                print(move_list[move_list.index(square)][1])
                move_list[move_list.index(square)][1].remove(deletable)



    return move_list

def generate_sliding_piece_moves(piece, position, num_square_to_edge):
    moves = []
    print(num_square_to_edge[position])

    if piece == 5:
        offsets = [-8, 1, 8, -1, -7, 9, 7, -9]
        extra_i = 0

    if piece == 4:
        offsets = [-8, 1, 8, -1]
        extra_i = 0

    if piece == 3:
        offsets = [-7, 9, 7, -9]
        extra_i = 4

    for i in range(len(offsets)):
        dest_square = position
        while num_square_to_edge[position][i + extra_i] > 0:
            dest_square = dest_square + offsets[i]
            num_square_to_edge[position][i + extra_i] = num_square_to_edge[position][i + extra_i] - 1

            print("\n")
            print(f"dest_square is: {dest_square}")
            print(f"position is: {position}")
            print(f"num squares to edge is: {num_square_to_edge[position][i+extra_i]}")

            if board[dest_square][0] == board[position][0]:
                break
            elif board[dest_square][0] == -1:
                moves.append(dest_square)

            elif board[dest_square][0] != board[position][0]:
                    moves.append(dest_square)
                    break


    return moves

def generate_knight_moves(position):
    moves = []
    for square in knight_moves[position]:
        if board[square][0] == board[position][0]:
            continue
        else:
            moves.append(square)

    return moves

def generate_pawn_moves(position, num_square_to_edge):
    y = math.floor(position / 8.0)
    moves = []
    if board[position][0] == 0:
        offsets = [-8, -7, -9, -16]
        num_square_to_edge = [num_square_to_edge[4], num_square_to_edge[7]]
    elif board[position][0] == 1:
        offsets = [8, 7, 9, 16]
        num_square_to_edge = [num_square_to_edge[6], num_square_to_edge[5]]

    if board[position + offsets[0]] == (-1, -1):
        moves.append(position + offsets[0])
    
    if board[position + offsets[0]] == (-1, -1) and y == 1 or board[position + offsets[0]] == (-1, -1) and y == 6:
        moves.append(position + offsets[3])

    if board[position + offsets[1]] != (-1, -1) and board[position + offsets[1]][0] != board[position][0] and num_square_to_edge[0] != 0:
        moves.append(position + offsets[1])

    if board[position + offsets[2]] != (-1, -1) and board[position + offsets[2]][0] != board[position][0] and num_square_to_edge[1] != 0:
        moves.append(position + offsets[2])

    return moves


def generate_king_moves(position, num_squares_to_edge):
    print(num_squares_to_edge)
    moves = []
    offsets = [-8, 1, 8, -1, -7, 9, 7, -9]
    for direction in range(len(offsets)):
        if board[position + offsets[direction]][0] != board[position][0] and num_squares_to_edge[position][direction] != 0:
            print("!!!!!!!!!!!!!!!!!!!!!")
            print(num_squares_to_edge[direction])
            print(offsets[direction])
            moves.append(position + offsets[direction])

    return moves
    
def check_move_validity(dest_squares, move_list):
    print(dest_squares)
    white_false = []
    black_false = []
    white_moves = []
    black_moves = []
    for square in move_list:
        if square[0][0] == 0:
            white_moves.append(i for i in square[1])
        elif square[0][0] == 1:
            black_moves.append([i for i in square[1]])

    for square in black_moves[0]:
        for square2 in dest_squares[0]:
            if square2 == square:
                white_false.append(square2)

    for square in white_moves[0]:
        for square2 in dest_squares[1]:
            if square2 == square:
                black_false.append(square2)

    print(white_false, black_false)

    return white_false, black_false