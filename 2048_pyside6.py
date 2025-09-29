import sys
import random
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QVBoxLayout
from PySide6.QtGui import QFont, QKeyEvent
from PySide6.QtCore import Qt

class Game2048(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("2048 Puzzle Game")

        # Main layout (vertical: score + grid)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Initialize score
        self.score = 0
        self.score_label = QLabel(f"Score: {self.score}")
        self.score_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.layout.addWidget(self.score_label)

        # Create grid layout for 4x4 board
        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        # Initialize 4x4 board with zeros
        self.board = [[0 for _ in range(4)] for _ in range(4)]

        # Dictionary of labels for GUI (to update tiles)
        self.labels = [[QLabel() for _ in range(4)] for _ in range(4)]

        # Set styles for each cell
        for row in range(4):
            for col in range(4):
                label = self.labels[row][col]
                label.setFixedSize(100, 100)  # Set tile size
                label.setAlignment(Qt.AlignCenter)  # Center text
                label.setFont(QFont("Arial", 20, QFont.Bold))
                label.setStyleSheet("background-color: lightgray; border: 2px solid gray;")
                self.grid_layout.addWidget(label, row, col)

        # Start game with 2 random tiles
        self.add_random_tile()
        self.add_random_tile()
        self.update_board()

    # Function to add a random tile (2 or 4) in empty spot
    def add_random_tile(self):
        empty_cells = [(r, c) for r in range(4) for c in range(4) if self.board[r][c] == 0]
        if empty_cells:
            r, c = random.choice(empty_cells)
            self.board[r][c] = random.choice([2, 4])

    # Function to update GUI board
    def update_board(self):
        for row in range(4):
            for col in range(4):
                value = self.board[row][col]
                label = self.labels[row][col]
                if value == 0:
                    label.setText("")  # Empty cell
                    label.setStyleSheet("background-color: lightgray; border: 2px solid gray;")
                else:
                    label.setText(str(value))
                    label.setStyleSheet(f"background-color: {self.get_color(value)}; border: 2px solid gray;")

        # Update score label
        self.score_label.setText(f"Score: {self.score}")

    # Function to get tile color based on value
    def get_color(self, value):
        colors = {
            2: "#eee4da",
            4: "#ede0c8",
            8: "#f2b179",
            16: "#f59563",
            32: "#f67c5f",
            64: "#f65e3b",
            128: "#edcf72",
            256: "#edcc61",
            512: "#edc850",
            1024: "#edc53f",
            2048: "#edc22e"
        }
        return colors.get(value, "#3c3a32")  # Default dark color

    # Function to handle key presses (arrow keys)
    def keyPressEvent(self, event: QKeyEvent):
        moved = False
        if event.key() == Qt.Key_Left:
            moved = self.move_left()
        elif event.key() == Qt.Key_Right:
            moved = self.move_right()
        elif event.key() == Qt.Key_Up:
            moved = self.move_up()
        elif event.key() == Qt.Key_Down:
            moved = self.move_down()

        # If move was valid → add new random tile
        if moved:
            self.add_random_tile()
            self.update_board()

    # Helper: compress tiles (remove zeros)
    def compress(self, row):
        new_row = [i for i in row if i != 0]  # remove zeros
        new_row += [0] * (4 - len(new_row))  # fill remaining with zeros
        return new_row

    # Helper: merge row tiles
    def merge(self, row):
        for i in range(3):
            if row[i] != 0 and row[i] == row[i + 1]:
                row[i] *= 2
                self.score += row[i]  # add score
                row[i + 1] = 0
        return row

    # Move left
    def move_left(self):
        moved = False
        new_board = []
        for row in self.board:
            compressed = self.compress(row)
            merged = self.merge(compressed)
            new_row = self.compress(merged)
            new_board.append(new_row)
            if new_row != row:
                moved = True
        self.board = new_board
        return moved

    # Move right
    def move_right(self):
        moved = False
        new_board = []
        for row in self.board:
            reversed_row = row[::-1]
            compressed = self.compress(reversed_row)
            merged = self.merge(compressed)
            new_row = self.compress(merged)[::-1]
            new_board.append(new_row)
            if new_row != row:
                moved = True
        self.board = new_board
        return moved

    # Move up
    def move_up(self):
        moved = False
        self.board = list(map(list, zip(*self.board)))  # transpose
        moved = self.move_left()
        self.board = list(map(list, zip(*self.board)))  # transpose back
        return moved

    # Move down
    def move_down(self):
        moved = False
        self.board = list(map(list, zip(*self.board)))  # transpose
        moved = self.move_right()
        self.board = list(map(list, zip(*self.board)))  # transpose back
        return moved



# Run the game
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Game2048()
    window.show()
    sys.exit(app.exec())
