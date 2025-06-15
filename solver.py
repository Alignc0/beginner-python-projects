from collections import deque

def bfs(maze):
    n = maze.shape[0]
    visited = [[False] * n for _ in range(n)]
    prev = [[None] * n for _ in range(n)]

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        if (x, y) == (n - 1, n - 1):
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and maze[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    prev[nx][ny] = (x, y)

    if not visited[n - 1][n - 1]:
        return None

    path = []
    x, y = n - 1, n - 1
    while (x, y) != (0, 0):
        path.append((x, y))
        x, y = prev[x][y]
    path.append((0, 0))
    path.reverse()

    return path