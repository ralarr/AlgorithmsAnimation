import time
from point import Point2 as Point

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

def bfs(maze, x, y, queue, path, visited, draw_maze):
    root = Point(x, y, None)
    set_roots_children(root, maze, visited)
    
    queue.append(root)

    while queue:
        p = queue.popleft()
        if p.x == len(maze)-1 and p.y == len(maze[0])-1:
            path.append(p)
            draw_maze(maze, path, visited, ['red' for x in range(len(maze))])
            time.sleep(0.6)
            break
        visited.add(p)
        
        draw_maze(maze, path, visited, ['red' for x in range(len(maze))])
        time.sleep(0.6)
        
        if p != root:
            set_children(p, maze, visited)
        p.visited = True

        if dead_end(p) and (p.x != len(maze)-1 or p.y != len(maze[0])-1):
            p.dead_end = True
            while p.parent != root and parent_has_all_dead_ends(p.parent):
                if p.parent in path:
                    path.remove(p.parent)
                p.parent.dead_end = True
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
