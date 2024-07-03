from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        # Initialize the main window
        self.__root = Tk()
        self.__root.title("Maze Solver")  # Set the window title
        
        # Create a canvas widget where drawing will be done
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)  # Expand canvas to fill the window
        
        self.__running = False  # Flag to indicate if the window is running
        self.__root.protocol("WM_DELETE_WINDOW", self.close)  # Handle window close event

    def redraw(self):
        # Update the GUI, ensuring changes are rendered
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        # Keep the window running until it's closed
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")  # Print a message when the window is closed

    def close(self):
        # Stop the running loop, effectively closing the window
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        # Draw a line on the canvas
        line.draw(self.__canvas, fill_color)
