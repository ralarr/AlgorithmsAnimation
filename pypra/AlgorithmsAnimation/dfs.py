import time
from point import Point

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
