# main.py

from src.point import Point
from src.line import Line
from src.window import Window

def main():
    # Create a Window instance
    window = Window(400, 400)

    # Define your lines with Points
    line1 = Line(Point(0, 0), Point(600, 600))
    line2 = Line(Point(150, 15), Point(750, 75))
    line3 = Line(Point(30, 70), Point(500, 100))

    # Draw the lines on the window's canvas
    window.draw_line(line1, "black")
    window.draw_line(line2, "red")
    window.draw_line(line3, "blue")

    # Wait for the window to close
    window.wait_for_close()

if __name__ == "__main__":
    main()