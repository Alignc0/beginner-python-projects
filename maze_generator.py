import numpy as np
import matplotlib.pyplot as plt
from solver import bfs
from animate_solver import animate_path

def create_maze(size=10, wall_prob=0.3):
    maze = np.random.choice([0, 1], size=(size, size), p=[1 - wall_prob, wall_prob])
    maze[0, 0] = 0
    maze[size - 1, size - 1] = 0
    return maze

def draw_maze(maze, path=None):
    size = maze.shape[0]
    plt.figure(figsize=(6, 6))
    plt.imshow(maze, cmap='binary')

    if path:
        px, py = zip(*path)
        plt.plot(py, px, color='red', linewidth=2)

    plt.scatter(0, 0, color='green', s=100, label='Başlangıç')
    plt.scatter(size - 1, size - 1, color='blue', s=100, label='Hedef')

    plt.xticks([]); plt.yticks([])
    plt.legend()
    plt.show()

if __name__ == "__main__":
    maze = create_maze(size=10)
    path = bfs(maze)

    if path:
        print("Yol bulundu, adım sayısı:", len(path))
        animate_path(maze, path)
    else:
        print("Çıkış bulunamadı.")

    draw_maze(maze, path)