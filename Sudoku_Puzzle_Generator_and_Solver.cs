static int[,] GeneratePuzzle()
{
    int[,] puzzle = new int[9, 9];
    Random rand = new Random();
    for (int i = 0; i < 9; i++)
        for (int j = 0; j < 9; j++)
            puzzle[i, j] = rand.Next(0, 10);
    return puzzle;
}