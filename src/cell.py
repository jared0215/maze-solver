from point import Point  # Import the Point class
from line import Line  # Import the Line class

class Cell:
    def __init__(self, win):
        # Initialize the cell with walls and window reference
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None  # x-coordinate of the top-left corner
        self._x2 = None  # x-coordinate of the bottom-right corner
        self._y1 = None  # y-coordinate of the top-left corner
        self._y2 = None  # y-coordinate of the bottom-right corner
        self._win = win  # Reference to the window for drawing

        self.visited = False # Tracks which cells had theirs walls broken down

    def draw(self, x1, y1, x2, y2):
        # Draw the cell with walls
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        # Define background color based on the canvas background (adjust as needed)
        bg_color = self._win._Window__canvas["bg"]  # Getting the actual background color of the canvas

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)  # Draw left wall
        else:
            # Erase the left wall
            erase_line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(erase_line, fill_color=bg_color)  # Erase left wall

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)  # Draw top wall
        else:
            # Erase the top wall
            erase_line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(erase_line, fill_color=bg_color)  # Erase top wall

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)  # Draw right wall
        else:
            # Erase the right wall
            erase_line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(erase_line, fill_color=bg_color)  # Erase right wall

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)  # Draw bottom wall
        else:
            # Erase the bottom wall
            erase_line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(erase_line, fill_color=bg_color)  # Erase bottom wall

    def draw_move(self, to_cell, undo=False):
        # Draw the move from current cell to another cell
        line = Line(Point((self._x1 + self._x2)/2, (self._y1 + self._y2)/2), 
                    Point((to_cell._x1 + to_cell._x2)/2, (to_cell._y1 + to_cell._y2)/2))
        
        fill_color = "red" if not undo else "gray"  # Red for normal move, gray for undo move
        
        self._win.draw_line(line, fill_color=fill_color)  # Draw the move line
