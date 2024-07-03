# main.py

from src.point import Point
from src.line import Line
from src.window import Window
from src.cell import Cell

def main():
    # Create a Window instance
    window = Window(800, 600)

    # # Define your lines with Points
    # line1 = Line(Point(0, 0), Point(600, 600))
    # line2 = Line(Point(150, 15), Point(750, 75))
    # line3 = Line(Point(30, 70), Point(500, 100))

    # # Draw the lines on the window's canvas
    # window.draw_line(line1, "black")
    # window.draw_line(line2, "red")
    # window.draw_line(line3, "blue")

    # # Draw the cells on the window's canvas
    c1 = Cell(window)
    c1.has_right_wall = False
    c1.draw(50, 50, 100, 100)

    c2 = Cell(window)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw(100, 50, 150, 100)

    c1.draw_move(c2)

    c3 = Cell(window)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.draw(100, 100, 150, 150)

    c2.draw_move(c3)

    c4 = Cell(window)
    c4.has_left_wall = False
    c4.draw(150, 100, 200, 150)

    c3.draw_move(c4, True)

    # Wait for the window to close
    window.wait_for_close()

if __name__ == "__main__":
    main()