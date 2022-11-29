import pygame as py
import engine

py.font.init()
width = height = 560
dimension = 8
sq_size = height//dimension
max_fps = 15
images = {}
width_log = 150
my_font = py.font.SysFont('Times New Roman', 24)
text_suface = []
icon = py.image.load("images/icon.png")
rematch = py.image.load("images/rematch.png")

py.display.set_icon(icon)
def load_images():
    pieces = ["wR","wN","wB","wQ","wK","wP","bR","bN","bB","bQ","bK","bP"]
    for piece in pieces:
        images[piece] = py.image.load("images/" + piece + ".png")

def main():
    py.init()
    clock = py.time.Clock()
    win = py.display.set_mode((width, height))
    py.display.set_caption("AA Chess")
    win.fill(py.Color("BLACK"))
    gs = engine.gameState()
    load_images()
    running = True
    sqSelected = ()
    player_clicks = []
    move_made = False
    
    while running:

        for e in py.event.get():

            if e.type == py.QUIT:
                running = False

            elif e.type == py.MOUSEBUTTONDOWN:
                location = py.mouse.get_pos()
                col = location[0]//sq_size
                row = location[1]//sq_size


                if gs.finished and (180 < location[0] < 380 and 400 < location[1] < 450):
                    gs = engine.gameState()

                else:

                    if sqSelected == (row, col):
                        sqSelected = ()
                        player_clicks = []
                        gs.valid_moves.clear()

                    else:
                        sqSelected = (row, col)
                        player_clicks.append(sqSelected)

                    if len(player_clicks) == 1:
                        gs.check = False
                        gs.can_move = False
                        gs.get_valid_moves(player_clicks[0][0], player_clicks[0][1])

                        for type in range(len(gs.valid_moves)):
                            piece = gs.board[gs.valid_moves[type][0]][gs.valid_moves[type][1]]
                            gs.board[gs.valid_moves[type][0]][gs.valid_moves[type][1]] = gs.board[player_clicks[0][0]][player_clicks[0][1]]
                            gs.board[player_clicks[0][0]][player_clicks[0][1]] = "--"
                            if gs.board[gs.valid_moves[type][0]][gs.valid_moves[type][1]][0] == "w":
                                colour = "b"
                            else:
                                colour = "w"
                            gs.check_b = False
                            gs.check_w = False
                            gs.check_for_check(colour)

                            gs.board[player_clicks[0][0]][player_clicks[0][1]] = gs.board[gs.valid_moves[type][0]][gs.valid_moves[type][1]]
                            gs.board[gs.valid_moves[type][0]][gs.valid_moves[type][1]] = piece

                            if (colour == "w" and gs.check_b) or (colour == "b" and gs.check_w):
                                gs.valid_moves[type] = ()


                    elif len(player_clicks) == 2:

                        move = engine.Move(player_clicks[0], player_clicks[1], gs.board)
                        if sqSelected in gs.valid_moves:
                            gs.block_moves.clear()
                            gs.make_move(move, gs.board)

                            if gs.board[sqSelected[0]][sqSelected[1]][1] == "R" or gs.board[sqSelected[0]][sqSelected[1]] == "K":
                                if gs.board[sqSelected[0]][sqSelected[1]][0] == "w" or gs.board[sqSelected[0]][sqSelected[1]][1] == "wK":
                                    if gs.board[7][0][1] != "R" or gs.board[sqSelected[0]][sqSelected[1]][1] == "wK":
                                        gs.rook_moved_white_left = True
                                    if gs.board[7][7][1] != "R" or gs.board[sqSelected[0]][sqSelected[1]][1] == "wK":
                                        gs.rook_moved_white_right = True
                                if gs.board[sqSelected[0]][sqSelected[1]][0] == "b" or gs.board[sqSelected[0]][sqSelected[1]] == "bK":
                                    if gs.board[0][0][1] != "R" or gs.board[sqSelected[0]][sqSelected[1]][1] == "bK":
                                        gs.rook_moved_white_left = True
                                    if gs.board[0][7][1] != "R" or gs.board[sqSelected[0]][sqSelected[1]][1] == "bK":
                                        gs.rook_moved_white_right = True

                            gs.check = False
                            gs.check_b = False
                            gs.check_w = False

                            gs.get_valid_moves(sqSelected[0], sqSelected[1])
                            if gs.check:
                                if(gs.board[sqSelected[0]][sqSelected[1]][0] == "w"):
                                    colour = "b"
                                elif(gs.board[sqSelected[0]][sqSelected[1]][0] == "b"):
                                    colour = "w"
                                elif(gs.board[sqSelected[0]][sqSelected[1]][0] == "-"):
                                    colour = "-"
                                gs.check_colour = colour
                                gs.checkmate(colour)

                                if not gs.game_state:
                                    gs.finished = True

                            gs.white_to_move = not gs.white_to_move

                        gs.valid_moves.clear()
                        sqSelected = ()
                        player_clicks = []
        if move_made:
            move_made = False
        
        drawGameState(win, gs, sqSelected, rematch)
        clock.tick(max_fps)
        py.display.flip()

def drawGameState(win, gs, sqSelected, rematch):
    drawBoard(win, sqSelected, gs)
    drawPieces(win, gs.board, gs, rematch)

def drawBoard(win, sqSelected, gs):
    win.fill((255, 240, 220))
    colours = [py.Color(255, 240, 220), py.Color(180, 140, 90)]
    colours_selected = [py.Color(255, 250, 160), py.Color(180, 150, 30)]

    for r in range(dimension):
        for c in range(dimension):
            colour = colours[((r+c) % 2)]
            if gs.check and gs.board[r][c][1] == "K" and gs.board[r][c][0] == gs.check_colour:
                colour = py.Color(250, 120, 120)
            if sqSelected == (r, c):   
                colour = colours_selected[((r+c) % 2)]

            py.draw.rect(win, colour, py.Rect((c)*sq_size, (r)*sq_size, sq_size, sq_size))
            if (r, c) in gs.valid_moves:
                win.blit(py.image.load("images/dot.png"), ((c)*sq_size , (r)*sq_size))
                if gs.board[r][c][0] == "w" or gs.board[r][c][0] == "b":
                    colour = py.Color(235, 255, 180)
                    py.draw.rect(win, colour, py.Rect((c)*sq_size, (r)*sq_size, sq_size, sq_size))

def drawPieces(win, board, gs, rematch):
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if piece != "--":
                win.blit(images[piece], py.Rect(c*sq_size, r*sq_size, sq_size, sq_size))
    if gs.finished:
        
        win.blit(rematch, (180, 400))
        win.blit(py.image.load("images/checkmate.png"), (0, 0))

if __name__ == "__main__":
    main()