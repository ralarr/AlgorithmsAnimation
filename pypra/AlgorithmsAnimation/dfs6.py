import tkinter as tk
import random
import time

window = tk.Tk()
window.title("Python Algorithm Visualizer")


canvas = tk.Canvas(window, width=830, height=400, bg='pink')
canvas.grid(row=1, column=0, padx=5, pady=5)

UI = tk.Frame(window, width=830, height=100, bg='orange')
UI.grid(row=0, column=0, padx=5, pady=5)

spin1 = tk.Spinbox(UI, from_=4, to=9, width=5, justify="center")
spin1.grid(row=0, column=0, padx=5, pady=5)

spin2 = tk.Spinbox(UI, from_=4, to=9, width=5, justify="center")
spin2.grid(row=0, column=50, padx=5, pady=5)

""" Point """
class Point:
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __hash__(self):
        return self.x
""""""""""""

maze = []
path = []
visited = {}
visited = set()
def draw_maze(maze, path, visited, colors):
    canvas.delete("all")

    square_size = 40
    x1 = 20
    y1 = 20
    x2 = x1+square_size
    y2 = x2+square_size

    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):    
            if Point(i, j) in path:
                color = 'blue'
            elif Point(i, j) in visited:
                color = 'green'
            elif maze[i][j] == True:
                color = 'white'
            else:
                color = 'grey'
                
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)
            x1 += square_size
            x2 += square_size

            if j == len(maze[0])-1:
                x1 = 20
                y1 += square_size
                x2 = x1+square_size
                y2 = y1+square_size

    window.update_idletasks()

def get_maze():
    global maze
    maze = [[None]*int(spin1.get()) for _ in range(int(spin2.get()))]
    i = 0
    while i < int(spin2.get()):
        j = 0
        while j < int(spin1.get()):
            maze[i][j] = random.randint(0, 1)
            j += 1
        i += 1

def make_maze():
    path.clear()
    visited.clear()
    while True:
        get_maze()
        if maze[0][0] == True and maze[-1][-1] == True:
            break

    draw_maze(maze, path, visited, ['white' for x in range(len(maze))])

maze_button = tk.Button(UI, text="Make maze", bg='pink', command=make_maze)
maze_button.grid(row=0, column=100, padx=5, pady=5)


def dead_end(x, y, maze, visited):
    if (y+1 >= len(maze[0]) or maze[x][y+1] == False or Point(x, y+1) in visited) and\
        (x+1 >= len(maze) or maze[x+1][y] == False or Point(x+1, y) in visited) and\
        (y-1 < 0 or maze[x][y-1] == False or Point(x, y-1) in visited) and\
        (x-1 < 0 or maze[x-1][y] == False or Point(x-1, y) in visited):
        return True

    return False

def dfs(maze, x, y, path, visited, draw_maze):
    if y >= len(maze[0]) or x >= len(maze) or y < 0 or x < 0:
        return False
    if Point(x, y) in visited or maze[x][y] == False:
        return False
    visited.add(Point(x, y))
    
    draw_maze(maze, path, visited, ['red' for x in range(len(maze))])
    time.sleep(0.5)

    if dead_end(x, y, maze, visited) == True and (x != len(maze)-1 or y != len(maze[0])-1):
        return False

    at_end = x == len(maze)-1 and y == len(maze[0])-1

    if (at_end == True or dfs(maze, x, y+1, path, visited, draw_maze) or dfs(maze, x+1, y, path, visited, draw_maze) or
        dfs(maze, x, y-1, path, visited, draw_maze) or dfs(maze, x-1, y, path, visited, draw_maze)):
        p = Point(x, y)
        path.append(p)
        
        if path[-1] == Point(0, 0):
            draw_maze(maze, path, visited, ['red' for x in range(len(maze))])
            time.sleep(0.5)

        return True

    return False

def get_dfs():
    if (dfs(maze, 0, 0, path, visited, draw_maze) == False):
        canvas.create_text(100, 100, font=("Times New Roman", 20, "bold"), fill='pink', text="no solution")

dfs_button = tk.Button(UI, text="DFS", bg='pink', command=get_dfs)
dfs_button.grid(row=0, column=200, padx=5, pady=5)

window.mainloop()