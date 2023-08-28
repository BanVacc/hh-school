
from collections import deque

rows_count, col_count = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

# Ввод лабиринта
maze = []
for _ in range(rows_count):
    row = list(map(int, input().split()))
    maze.append(row)


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class queueNode:
    def __init__(self, point: Point, distance: int):
        self.point = point
        self.distance = distance


def isValid(row: int, col: int):
    return (0 <= row < rows_count) and (0 <= col < col_count)


def BFS(maze, src: Point, dest: Point):
    if maze[src.x][src.y] != 0 or maze[dest.x][dest.y] != 0:
        return -1

    explored = [[False for c in range(col_count)] for r in range(rows_count)]

    # Помечаем исходную точку как изученную
    explored[src.x][src.y] = True

    queue = deque()

    s = queueNode(src, 0)
    queue.append(s)

    while len(queue) != 0:
        cur_q = queue.popleft()

        cur_point = cur_q.point

        # Если нашли выход
        if cur_point.x == dest.x and cur_point.y == dest.y:
            return cur_q.distance

        # Массивы для перемещения в соседние клетки
        row_adj = [-1, 0, 0, 1]
        col_adj = [0, -1, 1, 0]

        # Выполнение шагов для поиска        
        for i in range(4):

            # Координаты смежных ячеек
            row = cur_point.x + row_adj[i]
            col = cur_point.y + col_adj[i]

            if isValid(row, col) and (maze[row][col] == 0) and not explored[row][col]:
                explored[row][col] = True
                Adjcell = queueNode(Point(row, col), cur_q.distance + 1)
                queue.append(Adjcell)

    return -1


def main():
    dist = BFS(maze, Point(y1, x1), Point(y2, x2))

    if dist != -1:
        print(dist)
    else:
        print(0)


main()
