import tkinter as tk
import random
import time
from selection import selection_sort
from insertion import insertion_sort
from quick import quick_sort
from point import Point
from dfs import dfs
from collections import deque
from bfs import bfs

window = tk.Tk()
window.title("Python Algorithms Animation")

array = []
def draw_array(array, colors):
    canvas.delete("all")

    space = 10
    common_width = 30
    offset = 20
    ground = 350
    curr_width = offset+common_width

    for x in range(0, len(array)):
        curr_height = ground-array[x]
        canvas.create_rectangle(offset, ground, curr_width, curr_height, fill=colors[x])
        canvas.create_text(offset+13, ground+20, text=str(array[x]))
        offset = space+curr_width
        curr_width = offset+common_width

    window.update_idletasks()

def make_array():
    global array
    array = []
    for _ in range(0, 20):
        array.append(random.randrange(10, 300))

    draw_array(array, ['red' for x in range(len(array))])


canvas = tk.Canvas(window, width=830, height=400, bg='pink')
canvas.grid(row=1, column=0, padx=5, pady=5)

UI = tk.Frame(window, width=830, height=100, bg='orange')
UI.grid(row=0, column=0, padx=5, pady=5)

def make_sorting_UI():    
    array_button = tk.Button(UI, text="Get a new array", bg='pink', command=make_array)
    array_button.grid(row=0, column=0, padx=5, pady=5)

    sorting_algorithms = ["Selection Sort", "Insertion Sort", "Quicksort"]
    var = tk.StringVar(window)
    var.set(sorting_algorithms[0])
    sorting_opts = tk.OptionMenu(UI, var, *sorting_algorithms)
    sorting_opts.config(width=15, font=('Helvetica', 10))
    sorting_opts.grid(row=0, column=50, padx=5, pady=5)

    def select_sort():
        global array
        if var.get() == "Selection Sort":
            selection_sort(array, draw_array)
        elif var.get() == "Insertion Sort":
            insertion_sort(array, draw_array)
        elif var.get() == "Quicksort":
            quick_sort(array, 0, len(array)-1, draw_array)

    sort_button = tk.Button(UI, text="Sort", bg='purple', command=select_sort)
    sort_button.grid(row=0, column=100, padx=5, pady=5)
    return UI

make_sorting_UI()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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


def get_dfs():
    if (dfs(maze, 0, 0, path, visited, draw_maze) == False):
        canvas.create_text(100, 100, font=("Times New Roman", 20, "bold"), fill='pink', text="no solution")

def get_bfs():
    queue = deque()
    if (bfs(maze, 0, 0, queue, path, visited, draw_maze) == False):
        canvas.create_text(100, 100, font=("Times New Roman", 20, "bold"), fill='pink', text="no solution")


def make_pf_UI():
    global spin1
    spin1 = tk.Spinbox(UI2, from_=4, to=9, width=5, justify="center")
    spin1.grid(row=0, column=0, padx=5, pady=5)

    global spin2
    spin2 = tk.Spinbox(UI2, from_=4, to=9, width=5, justify="center")
    spin2.grid(row=0, column=50, padx=5, pady=5)

    maze_button = tk.Button(UI2, text="Make maze", bg='pink', command=make_maze)
    maze_button.grid(row=0, column=100, padx=5, pady=5)

    pf_algorithms = ["DFS", "BFS"]
    var = tk.StringVar(window)
    var.set(pf_algorithms[0])
    pf_opts = tk.OptionMenu(UI2, var, *pf_algorithms)
    pf_opts.config(width=15, font=('Helvetica', 10))
    pf_opts.grid(row=0, column=150, padx=5, pady=5)

    def select_pf():
        global maze
        if var.get() == "DFS":
            get_dfs()
        elif var.get() == "BFS":
            get_bfs()

    pf_button = tk.Button(UI2, text="Find Path", bg='purple', command=select_pf)
    pf_button.grid(row=0, column=200, padx=5, pady=5)
    return UI2


pf_UI = False

def clear_canvas():
    global pf_UI
    global UI
    global UI2
    if pf_UI == False:
        canvas.delete('all')
        UI.destroy()
        UI2 = tk.Frame(window, width=830, height=100, bg='orange')
        UI2.grid(row=0, column=0, padx=5, pady=5)
        make_pf_UI()
        pf_UI = not pf_UI
    else:
        canvas.delete('all')
        UI2.destroy()
        UI = tk.Frame(window, width=830, height=100, bg='orange')
        UI.grid(row=0, column=0, padx=5, pady=5)
        make_sorting_UI()
        pf_UI = not pf_UI

UI3 = tk.Frame(window, width=0, height=0, bg='orange')
UI3.grid(row=5, column=0, padx=5, pady=5)

switch_screen_button = tk.Button(UI3, text="Switch", bg='red', command=clear_canvas)
switch_screen_button.grid(row=0, column=0)

window.mainloop()
