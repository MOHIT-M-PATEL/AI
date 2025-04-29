#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define N 6     // Grid size
#define WORDS 3 // Number of words

// Define the crossword grid
char grid[N][N] = {
    {'#', '#', '#', '#', '#', '#'},
    {'#', '-', '-', '-', '-', '#'},
    {'#', '-', '#', '-', '-', '#'},
    {'#', '-', '-', '-', '-', '#'},
    {'#', '#', '#', '-', '-', '#'},
    {'#', '#', '#', '#', '#', '#'}};

// List of words to place
char words[WORDS][N] = {"RAT", "LOG", "BAT"};

// Function to check if a word can be placed horizontally
bool canPlaceHorizontally(int row, int col, char *word)
{
    int len = strlen(word);
    if (col + len > N)
        return false; // Out of bounds

    for (int i = 0; i < len; i++)
    {
        if (grid[row][col + i] != '-' && grid[row][col + i] != word[i])
            return false;
    }
    return true;
}

// Function to check if a word can be placed vertically
bool canPlaceVertically(int row, int col, char *word)
{
    int len = strlen(word);
    if (row + len > N)
        return false; // Out of bounds

    for (int i = 0; i < len; i++)
    {
        if (grid[row + i][col] != '-' && grid[row + i][col] != word[i])
            return false;
    }
    return true;
}

// Place the word horizontally and store the original characters for backtracking
void placeWordHorizontally(int row, int col, char *word, char backup[])
{
    int len = strlen(word);
    for (int i = 0; i < len; i++)
    {
        backup[i] = grid[row][col + i]; // Save backup
        grid[row][col + i] = word[i];   // Place word
    }
}

// Place the word vertically and store the original characters for backtracking
void placeWordVertically(int row, int col, char *word, char backup[])
{
    int len = strlen(word);
    for (int i = 0; i < len; i++)
    {
        backup[i] = grid[row + i][col]; // Save backup
        grid[row + i][col] = word[i];   // Place word
    }
}

// Restore horizontal word placement (backtracking)
void restoreWordHorizontally(int row, int col, char *word, char backup[])
{
    int len = strlen(word);
    for (int i = 0; i < len; i++)
    {
        grid[row][col + i] = backup[i]; // Restore original
    }
}

// Restore vertical word placement (backtracking)
void restoreWordVertically(int row, int col, char *word, char backup[])
{
    int len = strlen(word);
    for (int i = 0; i < len; i++)
    {
        grid[row + i][col] = backup[i]; // Restore original
    }
}

// Recursive function to place words in the crossword
bool solve(int index)
{
    if (index == WORDS)
        return true; // All words placed

    char backup[N]; // Backup for backtracking

    for (int row = 0; row < N; row++)
    {
        for (int col = 0; col < N; col++)
        {
            // Try placing the word horizontally
            if (canPlaceHorizontally(row, col, words[index]))
            {
                placeWordHorizontally(row, col, words[index], backup);
                if (solve(index + 1))
                    return true;
                restoreWordHorizontally(row, col, words[index], backup);
            }

            // Try placing the word vertically
            if (canPlaceVertically(row, col, words[index]))
            {
                placeWordVertically(row, col, words[index], backup);
                if (solve(index + 1))
                    return true;
                restoreWordVertically(row, col, words[index], backup);
            }
        }
    }
    return false; // No valid placement found
}

// Function to print the crossword grid
void printGrid()
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            printf("%c ", grid[i][j]);
        }
        printf("\n");
    }
}

int main()
{
    if (solve(0))
    {
        printf(" Crossword Solution Found:\n");
        printGrid();
    }
    else
    {
        printf(" No solution found. Try increasing grid size or modifying word list.\n");
    }
    return 0;
}
