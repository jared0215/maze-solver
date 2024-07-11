from cell import Cell  # Import the Cell class
import random
import time


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        # Initialize the Maze with the provided parameters
        self._cells = []  # List to hold the cells of the maze
        self._x1 = x1  # Starting x-coordinate of the maze
        self._y1 = y1  # Starting y-coordinate of the maze
        self._num_rows = num_rows  # Number of rows in the maze
        self._num_cols = num_cols  # Number of columns in the maze
        self._cell_size_x = cell_size_x  # Width of each cell
        self._cell_size_y = cell_size_y  # Height of each cell
        self._win = win  # Reference to the window for drawing

        if seed:
            random.seed(seed)

        self._create_cells()  # Create and draw the cells of the maze
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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

    def _break_entrance_and_exit(self):
        # Remove the top wall of the top-left cell
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)  # Update drawing for top-left cell

        # Remove the bottom wall of the bottom-right cell
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(len(self._cells) - 1, len(self._cells[0]) - 1)  # Update drawing for bottom-right cell


    def _break_walls_r(self, i, j):
        # Mark the current cell as visited
        self._cells[i][j].visited = True
        
        # Define possible directions to move: (di, dj, wall_current, wall_next)
        directions = [
            (-1, 0, 'left', 'right'),   # Move left
            (1, 0, 'right', 'left'),    # Move right
            (0, -1, 'top', 'bottom'),   # Move up
            (0, 1, 'bottom', 'top')     # Move down
        ]

        while True:
            next_index_list = []

            # Determine which cells to visit next
            for di, dj, wall_current, wall_next in directions:
                ni, nj = i + di, j + dj  # Calculate new indices
                if 0 <= ni < self._num_cols and 0 <= nj < self._num_rows and not self._cells[ni][nj].visited:
                    next_index_list.append((ni, nj, wall_current, wall_next))  # Add valid cells to list

            # If there are no unvisited cells to move to, draw the current cell and return
            if not next_index_list:
                self._draw_cell(i, j)
                return

            # Randomly choose the next cell to visit
            next_index = random.choice(next_index_list)
            ni, nj, wall_current, wall_next = next_index  # Unpack the selected direction

            # Knock out walls between the current cell and the next cell
            setattr(self._cells[i][j], f'has_{wall_current}_wall', False)
            setattr(self._cells[ni][nj], f'has_{wall_next}_wall', False)

            # Recursively visit the next cell
            self._break_walls_r(ni, nj)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
        