#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 5
#define INF 1000

typedef struct
{
    int x, y;
    int g, h, f;
    struct Node *parent;
} Node;

int heuristic(int x1, int y1, int x2, int y2)
{
    return abs(x1 - x2) + abs(y1 - y2);
}

int isValid(int x, int y, int grid[N][N])
{
    return (x >= 0 && x < N && y >= 0 && y < N && grid[x][y] == 0);
}

void printPath(Node *node)
{
    if (node == NULL)
        return;
    printPath(node->parent);
    printf("(%d, %d) -> ", node->x, node->y);
}

void robotNavigate(int grid[N][N], int sx, int sy, int gx, int gy)
{
    Node *openList[N * N];
    int openCount = 0, closedList[N][N] = {0};

    Node *start = (Node *)malloc(sizeof(Node));
    start->x = sx;
    start->y = sy;
    start->g = 0;
    start->h = heuristic(sx, sy, gx, gy);
    start->f = start->g + start->h;
    start->parent = NULL;

    openList[openCount++] = start;

    int moves[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    while (openCount > 0)
    {
        int bestIndex = 0;
        for (int i = 1; i < openCount; i++)
        {
            if (openList[i]->f < openList[bestIndex]->f)
                bestIndex = i;
        }

        Node *current = openList[bestIndex];
        openList[bestIndex] = openList[--openCount];

        if (current->x == gx && current->y == gy)
        {
            printf("Path found: ");
            printPath(current);
            printf("Goal\n");
            return;
        }

        closedList[current->x][current->y] = 1;

        for (int i = 0; i < 4; i++)
        {
            int nx = current->x + moves[i][0];
            int ny = current->y + moves[i][1];

            if (!isValid(nx, ny, grid) || closedList[nx][ny])
                continue;

            int newG = current->g + 1;
            int newH = heuristic(nx, ny, gx, gy);
            int newF = newG + newH;

            int found = 0;
            for (int j = 0; j < openCount; j++)
            {
                if (openList[j]->x == nx && openList[j]->y == ny)
                {
                    if (openList[j]->g > newG)
                    {
                        openList[j]->g = newG;
                        openList[j]->f = newF;
                        openList[j]->parent = current;
                    }
                    found = 1;
                    break;
                }
            }

            if (!found)
            {
                Node *newNode = (Node *)malloc(sizeof(Node));
                newNode->x = nx;
                newNode->y = ny;
                newNode->g = newG;
                newNode->h = newH;
                newNode->f = newF;
                newNode->parent = current;
                openList[openCount++] = newNode;
            }
        }
    }

    printf("No path found\n");
}

int main()
{
    int grid[N][N] = {
        {0, 0, 0, 0, 0},
        {0, 1, 1, 1, 0},
        {0, 0, 0, 1, 0},
        {0, 1, 0, 1, 0},
        {0, 0, 0, 0, 0}};

    printf("Finding path from (0,0) to (4,4)...\n");
    robotNavigate(grid, 0, 0, 4, 4);

    return 0;
}
