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