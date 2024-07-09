from cell import Cell  # Import the Cell class
import random
import time


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        # Initialize the Maze with the provided parameters
        self._cells = []  # List to hold the cells of the maze
        self._x1 = x1  # Starting x-coordinate of the maze
        self._y1 = y1  # Starting y-coordinate of the maze
        self._num_rows = num_rows  # Number of rows in the maze
        self._num_cols = num_cols  # Number of columns in the maze
        self._cell_size_x = cell_size_x  # Width of each cell
        self._cell_size_y = cell_size_y  # Height of each cell
        self._win = win  # Reference to the window for drawing

        self._create_cells()  # Create and draw the cells of the maze

    def _create_cells(self):
        # Create the cells of the maze and draw them
        for i in range(self._num_cols):
            col_cells = []  # List to hold the cells in the current column
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))  # Create a new cell and add it to the column
            self._cells.append(col_cells)  # Add the column of cells to the maze
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)  # Draw each cell

    def _draw_cell(self, i, j):
        # Draw a cell at the specified row and column
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x  # Calculate the top-left x-coordinate of the cell
        y1 = self._y1 + j * self._cell_size_y  # Calculate the top-left y-coordinate of the cell
        x2 = x1 + self._cell_size_x  # Calculate the bottom-right x-coordinate of the cell
        y2 = y1 + self._cell_size_y  # Calculate the bottom-right y-coordinate of the cell
        self._cells[i][j].draw(x1, y1, x2, y2)  # Draw the cell
        self._animate()  # Animate the drawing

    def _animate(self):
        # Animate the drawing process by redrawing the window and pausing
        if self._win is None:
            return
        self._win.redraw()  # Redraw the window to update the drawing
        # time.sleep(0.05)  # Pause for a short duration to create an animation effect
