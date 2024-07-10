class Line:
    def __init__(self, point_one, point_two):
        # Initialize the Line with two Point objects
        self.point_one = point_one  # Starting point of the line
        self.point_two = point_two  # Ending point of the line

    def draw(self, canvas, fill_color):
        # Draw the line on the given canvas
        canvas.create_line(
            self.point_one.x, self.point_one.y,  # Starting coordinates of the line
            self.point_two.x, self.point_two.y,  # Ending coordinates of the line
            fill=fill_color,  # Color of the line
            width=2  # Width of the line
        )
