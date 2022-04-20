# Python Documentation

# Sudoku Solver

This Python script is a Sudoku puzzle generator and solver. It first generates a random Sudoku puzzle and then solves it using a backtracking algorithm.

## Libraries Used

- `random`: This library is used to generate random numbers. It is used in this script to generate a random Sudoku puzzle.

## Functions

- `generate_board()`: This function generates a random Sudoku puzzle. It first creates a list of numbers from 1 to 9, then arranges them in a 9x9 grid in a way that follows the rules of Sudoku. It then randomly removes about 3/4 of the numbers to create the puzzle.

- `print_board(board)`: This function prints the Sudoku board to the console. It formats the board in a way that is easy to read.

- `solve(board)`: This function solves the Sudoku puzzle using a backtracking algorithm. It first finds an empty space on the board, then tries to fill it with a number from 1 to 9 that doesn't violate the rules of Sudoku. If it can't find a number that works, it backtracks and tries a different number for the previous space.

- `valid(board, num, pos)`: This function checks if a number can be placed at a certain position on the board without violating the rules of Sudoku.

- `find_empty(board)`: This function finds an empty space on the board.

- `main()`: This function generates a Sudoku puzzle, prints it, solves it, and then prints the solution.

## Usage

To use this script, simply run it with Python. It will automatically generate a Sudoku puzzle, print it, solve it, and then print the solution.

```bash
python sudoku_solver.py
```

## Example Output

The script will output something like this:

```
[.][.][.][.][.][.][.][.][.]
[.][.][.][.][.][.][.][.][.]
[.][.][.][.][.][.][.][.][.]
[.][.][.][.][.][.][.][.][.]
[.][.][.][.][.][.][.][.][.]
[.][.][.][.][.][.][.][.][.]
[.][.][.][.][.][.][.][.][.]
[.][.][.][.][.][.][.][.][.]
[.][.][.][.][.][.][.][.][.]
___________________
[1][2][3][4][5][6][7][8][9]
[4][5][6][7][8][9][1][2][3]
[7][8][9][1][2][3][4][5][6]
[2][3][4][5][6][7][8][9][1]
[5][6][7][8][9][1][2][3][4]
[8][9][1][2][3][4][5][6][7]
[3][4][5][6][7][8][9][1][2]
[6][7][8][9][1][2][3][4][5]
[9][1][2][3][4][5][6][7][8]
```

The first grid is the generated Sudoku puzzle, and the second grid is the solved puzzle.

---

# C# Documentation

# Sudoku Solver in C#

This repository contains a simple Sudoku solver written in C#. The script generates a random 9x9 Sudoku puzzle and attempts to solve it. If a solution is found, it prints the solved puzzle to the console. If no solution is found, it prints a message indicating that no solution was found.

## Script Explanation

The script is composed of a single class, `Program`, which contains the `Main` method and several helper methods.

### Main Method

The `Main` method is the entry point of the script. It generates a random puzzle, prints it, attempts to solve it, and then either prints the solved puzzle or a message indicating that no solution was found.

### GeneratePuzzle Method

The `GeneratePuzzle` method creates a new 9x9 array of integers and fills it with random numbers between 0 and 9. This array represents the Sudoku puzzle.

### PrintPuzzle Method

The `PrintPuzzle` method prints the puzzle to the console. It iterates over each row and column of the puzzle and prints each number, followed by a space. After each row, it prints a newline.

### SolvePuzzle Method

The `SolvePuzzle` method attempts to solve the puzzle using a recursive backtracking algorithm. It iterates over each cell in the puzzle. If a cell is empty (represented by a 0), it tries each number from 1 to 9. If a number is valid (i.e., it doesn't violate the Sudoku rules), it places the number in the cell and recursively attempts to solve the rest of the puzzle. If no valid number can be found for a cell, it backtracks by setting the cell back to 0 and returning false.

### IsValid Method

The `IsValid` method checks whether a given number can be placed in a given cell without violating the Sudoku rules. It checks the row, column, and 3x3 box that the cell belongs to. If the number already exists in any of these, it returns false. Otherwise, it returns true.

## Imported Libraries

The script uses the `System` namespace, which is a fundamental namespace in C#. It provides classes and interfaces that support a wide range of system programming tasks such as input/output, exceptions handling, garbage collection, and random number generation. In this script, it is used for console input/output and random number generation.

---

# Java Documentation

# Sudoku Solver in Java

This repository contains a simple Sudoku solver implemented in Java. The solver uses a backtracking algorithm to fill the Sudoku grid.

## Script Explanation

The script takes a 2D array representing a Sudoku grid as input. The grid is a 9x9 matrix, where 0 represents an empty cell. The script then attempts to solve the Sudoku puzzle by filling the empty cells with numbers from 1 to 9, following the rules of Sudoku.

The script uses several helper methods to check if a number can be placed in a certain cell. If the number can be placed, it is placed in the cell and the script recursively attempts to fill the rest of the grid. If the grid cannot be filled, the cell is emptied and the next number is tried. If no number can be placed in a cell, the script backtracks and returns false. If all cells are filled, the script returns true, indicating that the Sudoku puzzle has been solved.

## Imported Libraries

The script imports the `java.util.*` package, which is a part of the Java Standard Edition library and provides the framework for working with data structures. However, in this script, it is not used and can be removed.

## Usage

To use the script, create a new instance of the `Sudoku` class with a 2D array representing the Sudoku grid to be solved. Then, call the `solve()` method on the instance. If the Sudoku puzzle can be solved, the method will return true and the solved grid can be displayed using the `display()` method. If the puzzle cannot be solved, the `solve()` method will return false.

```java
int[][] board = {
    {8, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 3, 6, 0, 0, 0, 0, 0},
    {0, 7, 0, 0, 9, 0, 2, 0, 0},
    {0, 5, 0, 0, 0, 7, 0, 0, 0},
    {0, 0, 0, 0, 4, 5, 7, 0, 0},
    {0, 0, 0, 1, 0, 0, 0, 3, 0},
    {0, 0, 1, 0, 0, 0, 0, 6, 8},
    {0, 0, 8, 5, 0, 0, 0, 1, 0},
    {0, 9, 0, 0, 0, 0, 4, 0, 0}
};
Sudoku sudoku = new Sudoku(board);
if (sudoku.solve()) {
    sudoku.display();
} else {
    System.out.println("Unsolvable");
}
```

This will display the solved Sudoku grid if it can be solved, or print "Unsolvable" if it cannot.

---
