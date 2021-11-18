import svgwrite

'''
from Graphene import draw_line, fin, Point

draw_line((0, 10))
draw_line((-10, 0), Point(0, -5, -1))
fin()
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tuple(self):
        return (self.x, self.y)

class Line:
    def __init__(self, vector, init):
        self.mod = -0.5 if vector[0] > 0 else 0.5 
        self.init = Point(init.x + self.mod, init.y) 
        self.vector = vector 
        self.final = self.get_final()

    def set_final(self, new_init):
        self.init = Point(new_init[0] + self.mod, init[1])
        self.final = Point(self.init.x + self.vector[0], self.init.y + self.vector[1])

    def get_final(self):
        final = Point(self.init.x + self.vector[0], self.init.y + self.vector[1])
        return final 

class Canvas:
    def __init__(self):
        self.filename = ""
        self.lines = []

    def get_dims(self):
        height = 1
        width = 1
        for line in self.lines:
            if abs(line.vector[0]) > width:
                width = abs(line.vector[0])
            if abs(line.vector[1] > height):
                height = abs(line.vector[1])
        return Point(width, height)

    def line(self, vector, point_change=(0, 0, 0)):
        last_point = Point(0, 0)
        if len(self.lines) != 0:
            p = self.lines[point_change[2]].final 
            new_point = Point(p.x + point_change[0], p.y + point_change[1])
            if point_change != (0, 0, 0): 
                print("point change != None")
                last_point = new_point
            else:
                print("point change == None")
                last_point = self.lines[-1].final 

        line = Line(vector, last_point)

        self.lines.append(line)

    def draw_line(self, glyph, vector, last_point):
        line = Line(vector, last_point)
        init = line.init.tuple()
        final = line.final.tuple()
        
        drawable = glyph.line(init, final, stroke=svgwrite.rgb(0, 0, 0))
        glyph.add(drawable)

        return line.final 

    def get_init_point(self, dims):
        frame_center = (dims.x / 2, dims.y / 2)
        init_point = Point(frame_center[0] - (dims.x / 2), frame_center[1] - (dims.y / 2))
        return init_point

    def fin(self, filename):
        size = self.get_dims()
        #size_str = (str(size.x) + "px", str(size.y) + "px")
        size_str = ("50px", "50px")
        
        self.filename = filename 
        glyph = svgwrite.Drawing(self.filename, size_str)
        #init_point = self.get_init_point(size)
        init_point = Point(25, 25)


        for line in self.lines:
            temp = self.draw_line(glyph, line.vector, init_point)
            init_point = temp
        glyph.save()

class Main:
    def __init__(self):
        self.cur_glyph = None 

m = Main()

def draw_line(vector, point_change=None):
    m.cur_glyph = m.cur_glyph if m.cur_glyph != None else Canvas()
        
    if point_change == None:
        m.cur_glyph.line(vector)
    else:
        m.cur_glyph.line(vector, point_change)

def fin(filename):
    m.cur_glyph.fin(filename)
        
    m.cur_glyph = None 
