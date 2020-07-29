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

""" Point2 """
class Point2:
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