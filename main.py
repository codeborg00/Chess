import board_file, view, pygame

board= board_file.board

board = board_file.import_FEN("8/8/5k2/8/8/2K5/8/8 w - - 0 1", board)



view.draw_board()
view.render_pieces(board)


move_list = board_file.generate_moves2(board)
print(move_list)



view.highlight_square(board, move_list)


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False