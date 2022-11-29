class gameState():
    def __init__(self):
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]
        self.white_to_move = True
        self.movelog = []
        self.valid_moves = []
        self.check = False
        self.check_w = False
        self.check_b = False 
        self.check_colour = ""
        self.block_moves = []
        self.checkmate_moves = []
        self.game_state = True
        self.rook_moved_black_right = False
        self.rook_moved_black_left = False
        self.rook_moved_white_right = False
        self.rook_moved_white_left = False
        self.castled_right_black = False
        self.castled_left_black = False
        self.castled_right_white = False
        self.castled_left_white = False
        self.can_move = ""
        self.empassant = []
        self.finished = False
    
    def check_for_check(self, colour):
        self.checkmate_moves.clear()
    
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                
                turn = self.board[row][col][0]
                if turn == colour:
                    piece = self.board[row][col][1]
        
                    if piece == 'P':
                        self.can_move = True                          
                        self.get_pawn_moves(row, col)
                        self.can_move = False
                    elif piece == 'R':
                        self.can_move = True 
                        self.get_rook_moves(row, col)
                        self.can_move = False
                    elif piece == 'N':
                        self.can_move = True 
                        self.get_knight_moves(row, col)
                        self.can_move = False
                    elif piece == 'B':
                        self.can_move = True 
                        self.get_bishop_moves(row, col)
                        self.can_move = False
                    elif piece == 'K':
                        self.can_move = True 
                        self.get_king_moves(row, col)
                        self.can_move = False
                    elif piece == 'Q':
                        self.can_move = True
                        self.get_queen_moves(row, col)
                        self.can_move = False
                    else:
                        self.can_move = False


    def make_move(self, move, board):
        
        piece = self.board[move.start_row][move.start_col][1]

        colour = self.board[move.start_row][move.start_col][0]
        
        if colour == "w":
            factor = 1
            op_colour = "b"
        else:
            factor = -1
            op_colour = "w"
        
        if piece == "P":
            if self.board[move.start_row][move.start_col] == self.board[move.end_row + 2*(factor)][move.end_col]:
                self.empassant.append((move.end_row, move.end_col, colour))


        if self.board[move.start_row][move.start_col] == "wK" and move.start_col == move.end_col + 2:
            self.board[move.start_row][move.start_col - 1] = "wR"
            self.board[7][0] = "--"
        if self.board[move.start_row][move.start_col] == "bK" and move.start_col == move.end_col + 2:
            self.board[move.start_row][move.start_col - 1] = "bR"
            self.board[0][0] = "--"
        if self.board[move.start_row][move.start_col] == "wK" and move.start_col == move.end_col - 2:
            self.board[move.start_row][move.start_col + 1] = "wR"
            self.board[7][7] = "--"
        if self.board[move.start_row][move.start_col] == "bK" and move.start_col == move.end_col - 2:
            self.board[move.start_row][move.start_col + 1] = "bR"
            self.board[0][7] = "--"


        if self.board[move.start_row][move.start_col][1] == "P" and (move.start_row, move.start_col, colour) in self.empassant:
            for i in range(len(self.empassant)):
                if self.empassant[i] == (move.start_row, move.start_col, colour):
                    self.empassant.pop(i)
                    break

        if self.board[move.start_row][move.start_col][1] == "P" and ((move.end_row + factor, move.end_col, op_colour) in self.empassant):
            for i in range(len(self.empassant)):
                if self.empassant[i] == (move.end_row + factor, move.end_col, op_colour):
                    self.board[self.empassant[i][0]][self.empassant[i][1]] = "--"
                    self.empassant.pop(i)
                    break
                        

        board[move.start_row][move.start_col] = "--"   
        board[move.end_row][move.end_col] = move.piece_moved
        note= move.get_chess_notation()
        self.movelog.append(note)

                       

    def get_valid_moves(self, r, c):
        turn = self.board[r][c][0]
        self.can_move = False
        if (turn == "w" and self.white_to_move) or (turn == "b" and self.white_to_move == False):            
            piece = self.board[r][c][1]
                     
            if piece == 'P':
                self.get_pawn_moves(r, c)
            elif piece == 'R':
                self.get_rook_moves(r, c)
            elif piece == 'N':
                self.get_knight_moves(r, c)
            elif piece == 'B':
                self.get_bishop_moves(r, c)
            elif piece == 'K':
                self.get_king_moves(r, c)
            elif piece == 'Q':
                self.get_queen_moves(r, c)
            else:
                pass

    def checkmate(self, colour):
        self.valid_moves.clear()
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                turn = self.board[row][col][0]
                if turn == colour:
                    piece = self.board[row][col][1]

                    if piece == 'P':     
                        self.get_pawn_moves(row, col)
                    elif piece == 'R':
                        self.get_rook_moves(row, col)
                    elif piece == 'N':
                        self.get_knight_moves(row, col)
                    elif piece == 'B':
                        self.get_bishop_moves(row, col)
                    elif piece == 'K':
                        self.get_king_moves(row, col)
                    elif piece == 'Q':
                        self.get_queen_moves(row, col)
        
        if len(self.valid_moves) == 0:
            self.game_state = False


    def move(self, op_colour, self_colour, reached_end, r, c, name):
        rook_moves = []
        check_move_temp = []
        for j in range(len(reached_end)):
            check_move_temp = []
            for i in range(1, 9):
                if name == "rook":
                    rook_moves = [((r + i), c),
                                    ((r - i), c),
                                    (r, (c + i)),
                                    (r, (c - i))]
                elif name == "bishop":
                    rook_moves = [((r + i), (c + i)),
                                    ((r - i), (c - i)),
                                    ((r - i), (c + i)),
                                    ((r + i), (c - i))]
                else:
                    rook_moves = [
                    ((r + i), (c + i)),
                    ((r - i), (c - i)),
                    ((r - i), (c + i)),
                    ((r + i), (c - i)),
                    ((r + i), c),
                    ((r - i), c),
                    (r, (c + i)),
                    (r, (c - i))]
                
                if 0 <= rook_moves[j][0] < 8 and 0 <= rook_moves[j][1] < 8:                   
                    if (self.board[rook_moves[j][0]][rook_moves[j][1]][0] == op_colour or self.board[rook_moves[j][0]][rook_moves[j][1]][0] == self_colour) and not reached_end[j]:                   
                        if self.board[rook_moves[j][0]][rook_moves[j][1]][0] == op_colour and (rook_moves[j] in self.block_moves or not self.check):
                            if self.board[rook_moves[j][0]][rook_moves[j][1]][1] == "K" :
                                self.check = True
                                if op_colour == "w":
                                    self.check_w = True
                                if op_colour == "b":
                                    self.check_b = True
                                self.block_moves = check_move_temp
                                self.block_moves.append((r, c))
                             
                            if not self.can_move:
                                self.valid_moves.append(rook_moves[j])
                            check_move_temp.append(rook_moves[j])
                        reached_end[j] = True

                if 0 <= rook_moves[j][0] < 8 and 0 <= rook_moves[j][1] < 8 and not reached_end[j]:
                    if self.board[rook_moves[j][0]][rook_moves[j][1]][0] == "-" and (rook_moves[j] in self.block_moves or not self.check):
                        check_move_temp.append(rook_moves[j])
                        if not self.can_move:
                            self.valid_moves.append(rook_moves[j])

    def get_pawn_moves(self, r, c):    
        if self.board[r][c][0] == "w":
            factor = 1
            op_colour = "b"
            line = 6
        else:
            factor = -1
            op_colour = "w"
            line = 1

        if self.board[r-factor][c] == "--" and ((r - factor, c) in self.block_moves or not self.check):
            if not self.can_move:
                self.valid_moves.append((r-factor, c))
            if self.board[r-2*(factor)][c] == "--" and r == line and ((r - 2*factor, c) in self.block_moves or not self.check):
                if not self.can_move:
                    self.valid_moves.append((r-2*(factor), c))
        if 0 <= (c - factor) < 8:
            if self.board[r-factor][c-factor][0] == op_colour and ((r - factor, c - factor) in self.block_moves or not self.check) or ((r, c - factor, op_colour) in self.empassant):
                if not self.can_move:
                    self.valid_moves.append(((r-factor), (c-factor)))
        if 8 > (c + factor) >= 0:
            if self.board[r-factor][c+factor][0] == op_colour and ((r - factor, c + factor) in self.block_moves or not self.check) or ((r, c + factor, op_colour) in self.empassant):
                if not self.can_move:
                    self.valid_moves.append(((r-factor), (c+factor)))

    def get_rook_moves(self, r, c):
        if self.board[r][c][0] == "w":
            op_colour = "b"
            self_colour = "w"
        else:
            op_colour = "w"
            self_colour = "b"
        reached_end = [
            False,
            False,
            False,
            False
        ]
        self.move( op_colour, self_colour, reached_end, r, c, "rook")

    def get_knight_moves(self, r, c):

        if self.board[r][c][0] == "w":
            op_colour = "w"
        else:
            op_colour = "b"
        
        knight_moves = [((r - 2), (c + 1)),
        ((r - 2), (c - 1)),
        ((r + 1), (c - 2)),
        ((r - 1), (c - 2)),
        ((r + 2), (c + 1)),
        ((r + 2), (c - 1)),
        ((r + 1), (c + 2)),
        ((r - 1), (c + 2))]

        for i in range(len(knight_moves)):
            if 8 > knight_moves[i][0] >= 0 and 8 > knight_moves[i][1] >= 0:
                if self.board[knight_moves[i][0]][knight_moves[i][1]][0] != op_colour and (knight_moves[i] in self.block_moves or not self.check):                            
                    if self.board[knight_moves[i][0]][knight_moves[i][1]][1] == "K":
                        self.check = True
                        self.block_moves.append((r, c))
                        self.block_moves.append(knight_moves[i])
                    if not self.can_move:
                        self.valid_moves.append(knight_moves[i])
        
    def get_king_moves(self, r, c):
        if self.board[r][c][0] == "w":
            self_colour = "w"
        else:
            self_colour = "b"
        king_moves = [((r + 1), c),
        ((r - 1), c),
        (r, (c + 1)),
        (r, (c - 1)),
        ((r + 1), (c - 1)),
        ((r - 1), (c + 1)),
        ((r + 1), (c + 1)),
        ((r - 1), (c - 1))
        ]

        for i in range(len(king_moves)):
            if 8 > king_moves[i][0] >= 0 and 8 > king_moves[i][1] >= 0:
                if self.board[king_moves[i][0]][king_moves[i][1]][0] != self_colour and (king_moves[i] not in self.block_moves or not self.check):
                    if not self.can_move:
                        self.valid_moves.append(king_moves[i])
                    if i == 2:
                        if not self.rook_moved_black_right and self.board[0][6] == "--" and self.board[0][5] == "--" and not self.check and self_colour == "b":
                            if not self.can_move:
                                self.valid_moves.append((r, c + 2))
                        if not self.rook_moved_white_right and self.board[7][6] == "--" and self.board[7][5] == "--" and not self.check and self_colour == "w":
                            if not self.can_move:
                                self.valid_moves.append((r, c + 2))
                    elif i == 3:
                        if not self.rook_moved_white_right and self.board[7][1] == "--" and self.board[7][2] == "--" and self.board[7][3] and not self.check and self_colour == "w":
                            if not self.can_move:
                                self.valid_moves.append((r, c - 2))
                        if not self.rook_moved_black_left and self.board[0][1] == "--" and self.board[0][2] == "--" and self.board[0][3] and not self.check and self_colour == "b":
                            if not self.can_move:
                                self.valid_moves.append((r, c - 2))

    def get_queen_moves(self, r, c):

        if self.board[r][c][0] == "w":
            op_colour = "b"
            self_colour = "w"
        else:
            op_colour = "w"
            self_colour = "b"

        reached_end = [
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False
        ]
        self.move( op_colour, self_colour, reached_end, r, c, "queen")

    def get_bishop_moves(self, r, c):
        
        if self.board[r][c][0] == "w":
            op_colour = "b"
            self_colour = "w"
        else:
            op_colour = "w"
            self_colour = "b"

        reached_end = [
            False,
            False,
            False,
            False
        ]

        self.move(op_colour, self_colour, reached_end, r, c, "bishop")



class Move():

    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_cols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    cols_to_files = {v: k for k, v in files_to_cols.items()}

    def __init__(self, startSq, endSq, board):
        self.start_row = startSq[0]
        self.start_col = startSq[1]
        self.end_row = endSq[0]
        self. end_col = endSq[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]
    
    def get_chess_notation(self):
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

    def get_rank_file(self, r, c):
        return self.cols_to_files[c] + self.rows_to_ranks[r]