import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_path(maze, path):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(maze, cmap='binary')

    ax.scatter(0, 0, color='green', s=100)
    ax.scatter(len(maze)-1, len(maze)-1, color='blue', s=100)

    line, = ax.plot([], [], color='red', linewidth=2)

    def update(i):
        if i == 0:
            return line,
        px, py = zip(*path[:i+1])
        line.set_data(py, px)
        return line,

    ani = animation.FuncAnimation(
        fig, update, frames=len(path), interval=200, blit=True, repeat=False
    )

    plt.xticks([]); plt.yticks([])
    plt.title("Maze Solver - BFS")

    ani.save("assets/maze_solution.gif", writer="pillow")
    plt.show()