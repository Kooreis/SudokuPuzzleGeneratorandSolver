```java
import java.util.*;

public class Sudoku {
    int[][] board;
    public static final int EMPTY = 0;
    public static final int SIZE = 9;

    public Sudoku(int[][] board) {
        this.board = new int[SIZE][SIZE];
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                this.board[i][j] = board[i][j];
            }
        }
    }
```