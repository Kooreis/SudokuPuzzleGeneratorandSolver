```CSharp
using System;

class Program
{
    static void Main(string[] args)
    {
        int[,] puzzle = GeneratePuzzle();
        PrintPuzzle(puzzle);
        Console.WriteLine();
        if (SolvePuzzle(puzzle))
            PrintPuzzle(puzzle);
        else
            Console.WriteLine("No solution found.");
    }

    static int[,] GeneratePuzzle()
    {
        int[,] puzzle = new int[9, 9];
        Random rand = new Random();
        for (int i = 0; i < 9; i++)
            for (int j = 0; j < 9; j++)
                puzzle[i, j] = rand.Next(0, 10);
        return puzzle;
    }

    static void PrintPuzzle(int[,] puzzle)
    {
        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
                Console.Write(puzzle[i, j] + " ");
            Console.WriteLine();
        }
    }

    static bool SolvePuzzle(int[,] puzzle)
    {
        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
            {
                if (puzzle[i, j] == 0)
                {
                    for (int k = 1; k <= 9; k++)
                    {
                        if (IsValid(puzzle, i, j, k))
                        {
                            puzzle[i, j] = k;
                            if (SolvePuzzle(puzzle))
                                return true;
                            else
                                puzzle[i, j] = 0;
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    static bool IsValid(int[,] puzzle, int row, int col, int num)
    {
        for (int i = 0; i < 9; i++)
            if (puzzle[row, i] == num || puzzle[i, col] == num)
                return false;
        int startRow = row - row % 3, startCol = col - col % 3;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (puzzle[i + startRow, j + startCol] == num)
                    return false;
        return true;
    }
}
```