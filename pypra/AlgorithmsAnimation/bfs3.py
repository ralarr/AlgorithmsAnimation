import tkinter as tk
import random
import time
from collections import deque

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
    def __init__(self, xx, yy, pp):
        self.x = xx
        self.y = yy
        self.parent = pp
        self.visited = False
        self.dead_end = False
        self.right = None
        self.down = None
        self.left = None
        self.up = None

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ") parent: " + str(self.parent)


    def __hash__(self):
        return self.x
""""""""""""

maze = []
path = []
visited = {}
visited = set()
def draw_maze(maze, visited, path, colors):
    canvas.delete("all")

    square_size = 40
    x1 = 20
    y1 = 20
    x2 = x1+square_size
    y2 = x2+square_size

    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):    
            if Point(i, j, None) in path:
                color = 'blue'
            elif Point(i, j, None) in visited:
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

    draw_maze(maze, visited, path, ['white' for x in range(len(maze))])

maze_button = tk.Button(UI, text="Make maze", bg='pink', command=make_maze)
maze_button.grid(row=0, column=100, padx=5, pady=5)

def dead_end(p):
    return not p.right and not p.down and not p.left and not p.up

def set_roots_children(parent, maze, visited):
    if parent.y+1 < len(maze[0]) and maze[parent.x][parent.y+1] != False:
        parent.right = Point(parent.x, parent.y+1, parent)
        visited.add(parent.right)
    if parent.x+1 < len(maze) and maze[parent.x+1][parent.y] != False:
        parent.down = Point(parent.x+1, parent.y, parent)
        visited.add(parent.down)
    if parent.y-1 >= 0 and maze[parent.x][parent.y-1] != False:
        parent.left = Point(parent.x, parent.y-1, parent)
        visited.add(parent.left)
    if parent.x-1 >= 0 and maze[parent.x-1][parent.y] != False:
        parent.up = Point(parent.x-1, parent.y, parent)
        visited.add(parent.up)

def set_children(parent, maze, visited):
    if parent.y+1 < len(maze[0]) and maze[parent.x][parent.y+1] != False:
        if parent.parent and (parent.parent.x != parent.x or parent.parent.y != parent.y+1) and Point(parent.x, parent.y+1, parent) not in visited:
            parent.right = Point(parent.x, parent.y+1, parent)
            visited.add(parent.right)
    if parent.x+1 < len(maze) and maze[parent.x+1][parent.y] != False:
        if parent.parent and (parent.parent.x != parent.x+1 or parent.parent.y != parent.y) and Point(parent.x+1, parent.y, parent) not in visited:
            parent.down = Point(parent.x+1, parent.y, parent)
            visited.add(parent.down)
    if parent.y-1 >= 0 and maze[parent.x][parent.y-1] != False:
        if parent.parent and (parent.parent.x != parent.x or parent.parent.y != parent.y-1) and Point(parent.x, parent.y-1, parent) not in visited:
            parent.left = Point(parent.x, parent.y-1, parent)
            visited.add(parent.left)
    if parent.x-1 >= 0 and maze[parent.x-1][parent.y] != False:
        if parent.parent and (parent.parent.x != parent.x-1 or parent.parent.y != parent.y) and Point(parent.x-1, parent.y, parent) not in visited:
            parent.up = Point(parent.x-1, parent.y, parent)
            visited.add(parent.up)

def parent_has_all_dead_ends(parent):
    return (not parent.right or parent.right.dead_end == True) and\
            (not parent.down or parent.down.dead_end == True) and\
            (not parent.left or parent.left.dead_end == True) and\
            (not parent.up or parent.up.dead_end == True)

def bfs(maze, x, y, queue, visited, path, draw_maze):
    root = Point(x, y, None)
    set_roots_children(root, maze, visited)
    
    queue.append(root)

    while queue:
        p = queue.popleft()
        if p.x == len(maze)-1 and p.y == len(maze[0])-1:
            path.append(p)
            draw_maze(maze, visited, path, ['red' for x in range(len(maze))])
            time.sleep(0.6)
            break
        print("pp ", p)
        visited.add(p)
        
        draw_maze(maze, visited, path, ['red' for x in range(len(maze))])
        time.sleep(0.6)
        
        if p != root:
            set_children(p, maze, visited)
        p.visited = True

        if dead_end(p) and (p.x != len(maze)-1 or p.y != len(maze[0])-1):
            print("pppp ", p)
            p.dead_end = True
            while p.parent != root and parent_has_all_dead_ends(p.parent):
                print("removing ", p.parent)
                if p.parent in path:
                    path.remove(p.parent)
                p.parent.dead_end = True
                print(p, "dead end")
                p = p.parent

        if p.dead_end != True:    
            path.append(p)

        if p.right and p.right.visited == False and p.y+1 < len(maze[0]) and maze[p.x][p.y+1] == True:
            queue.append(p.right)
        if p.down and p.down.visited == False and p.x+1 < len(maze) and maze[p.x+1][p.y] == True:
            queue.append(p.down)
        if p.left and p.left.visited == False and p.y-1 >= 0 and maze[p.x][p.y-1] == True:
            queue.append(p.left)
        if p.up and p.up.visited == False and p.x-1 >= 0 and maze[p.x-1][p.y] == True:
            queue.append(p.up)

    return path[-1].x == len(maze)-1 and path[-1].y == len(maze[0])-1

def get_bfs():
    queue = deque()
    if (bfs(maze, 0, 0, queue, visited, path, draw_maze) == False):
        canvas.create_text(100, 100, font=("Times New Roman", 20, "bold"), fill='pink', text="no solution")

bfs_button = tk.Button(UI, text="BFS", bg='pink', command=get_bfs)
bfs_button.grid(row=0, column=200, padx=5, pady=5)

window.mainloop()