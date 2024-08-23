# Chess Game

## Overview

This project is a chess game built using Python and the Pygame library. It provides a fully functional, two-player chess experience with a graphical interface. The game follows standard chess rules and includes basic features such as move validation, piece highlighting, and a turn-based system.

## Features

- **Graphical Interface**: The game features a simple and intuitive graphical interface built with Pygame.
- **Standard Chess Rules**: Supports all standard chess rules, including castling, en passant, and pawn promotion.
- **Two-Player Mode**: Play chess locally with a friend.
- **Move Validation**: Prevents illegal moves based on chess rules.
- **Highlight Moves**: Highlights possible moves for the selected piece.

## Requirements

- Python 3.x
- Pygame library

## Installation


2. **Install Dependencies**

   Make sure you have Python 3.x installed. Install the Pygame library if you haven't already:

   ```bash
   pip install pygame
   ```

## Game Controls

- **Mouse Click**: Select and move pieces.
- **Escape Key**: Exit the game.

## How to Play

1. **Select a Piece**: Click on a piece to select it. Possible moves will be highlighted.
2. **Move a Piece**: Click on a highlighted square to move the selected piece.
3. **Game Rules**: The game follows standard chess rules. Each player takes turns to make a move. The game ends when one player checkmates the other, resigns, or there is a stalemate.

## Folder Structure

```
chess-game/
│
├── assets/                  # Images and other assets
│   ├── pieces/              # Chess piece images
│   └── board/               # Board images
│
├── src/                     # Source code files
│   ├── chess.py             # Main game file
│   ├── board.py             # Board logic and representation
│   ├── pieces.py            # Piece classes and move logic
│   └── game.py              # Game loop and control logic
│
├── README.md                # Project README file
└── requirements.txt         # Project dependencies
```

## Future Enhancements

- **Single-Player Mode**: Add AI opponent for single-player mode.
- **Multiplayer Mode**: Enable online multiplayer functionality.
- **Undo/Redo Moves**: Add an option to undo/redo moves.
- **Save and Load Games**: Implement save and load functionality to continue games later.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any features, bug fixes, or improvements.


## Acknowledgments

- [Pygame](https://www.pygame.org/) for the game development framework.
- Special thanks to all contributors and supporters!

---

Feel free to customize this README to better suit your specific project details and requirements.
