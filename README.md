# 2048-pyside6-python

Project Overview

This is a 2048 Puzzle Game implemented in Python using the PySide6 GUI framework.
The objective of the game is simple: slide the tiles on a 4x4 grid to combine them and create the 2048 tile.

You can move tiles left, right, up, or down.

When two tiles with the same number collide, they merge into one tile.

After every move, a new tile (2 or 4) spawns in an empty spot.

The game ends when there are no valid moves left.

🎮 Features

4x4 game grid.

Arrow keys for movement.

Automatic merging of same-numbered tiles.

Score counter that updates after every merge.

Game over detection.

Smooth GUI built with PySide6.

🛠️ Tech Stack

Python 3.8+

PySide6 (Qt for Python) for GUI

Numpy (optional, for matrix operations)

📂 Project Structure
2048_pyside6.py    # Main game file
README.md          # Project documentation

🚀 How to Run the Project

Clone or download this repository.

Install required libraries:

pip install PySide6


Run the Python file:

python 2048_pyside6.py


Play the game using your arrow keys ⬅️ ⬆️ ➡️ ⬇️.

🎯 Game Rules

Use the arrow keys to slide tiles in one of the four directions.

Tiles with the same value merge together when they collide.

Example: 2 + 2 = 4, 4 + 4 = 8

After each move, a new tile (2 or 4) spawns randomly in an empty spot.

The game continues until:

You create the 2048 tile (You Win 🎉)

Or no more moves are possible (Game Over ❌).

🧠 Game Logic Explanation

Move Left/Right:

Compress numbers to remove gaps.

Merge adjacent equal numbers.

Compress again to fill empty spots.

Move Up/Down:

Use matrix transpose trick to convert columns into rows.

Apply left/right move logic.

Transpose back to restore the board.


📊 Future Improvements

Add restart button.

Save high score across sessions.

Add animations for tile movement.

Improve theme and colors (dark/light mode).
