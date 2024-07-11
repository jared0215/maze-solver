import unittest  # Import the unittest module for creating and running tests
from maze import Maze  # Import the Maze class from the maze module

class Tests(unittest.TestCase):
    def setUp(self):
        # Create a small 2x2 maze for testing purposes
        self.maze = Maze(0, 0, 2, 2, 10, 10, None)  # Adjust constructor parameters as needed
        self.maze._break_entrance_and_exit()

    def test_maze_create_cells(self):
        # Test case to check the creation of cells in the maze
        num_cols = 12  # Number of columns in the maze
        num_rows = 10  # Number of rows in the maze
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)  # Create a Maze object

        # Assert that the number of columns created is equal to num_cols
        self.assertEqual(len(m1._cells), num_cols)

        # Assert that the number of rows in the first column is equal to num_rows
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells_large(self):
        # Test case to check the creation of cells in a larger maze
        num_cols = 16  # Number of columns in the maze
        num_rows = 12  # Number of rows in the maze
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)  # Create a Maze object

        # Assert that the number of columns created is equal to num_cols
        self.assertEqual(len(m1._cells), num_cols)

        # Assert that the number of rows in the first column is equal to num_rows
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_entrance(self):
        # Check the top wall of the top-left cell is removed
        self.assertFalse(self.maze._cells[0][0].has_top_wall, "Entrance wall should be removed")

    def test_exit(self):
        # Check the bottom wall of the bottom-right cell is removed
        self.assertFalse(self.maze._cells[-1][-1].has_bottom_wall, "Exit wall should be removed")

    
    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )


if __name__ == '__main__':
    unittest.main()