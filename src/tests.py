import unittest  # Import the unittest module for creating and running tests

from maze import Maze  # Import the Maze class from the maze module


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        # Test case to check the creation of cells in the maze
        num_cols = 12  # Number of columns in the maze
        num_rows = 10  # Number of rows in the maze
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)  # Create a Maze object

        # Assert that the number of columns created is equal to num_cols
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )

        # Assert that the number of rows in the first column is equal to num_rows
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        # Test case to check the creation of cells in a larger maze
        num_cols = 16  # Number of columns in the maze
        num_rows = 12  # Number of rows in the maze
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)  # Create a Maze object

        # Assert that the number of columns created is equal to num_cols
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )

        # Assert that the number of rows in the first column is equal to num_rows
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )


if __name__ == "__main__":
    unittest.main()  # Run the tests when this script is executed
