import svgwrite

center = (0, 0)

class Point:
    def __init__(self, coords, glyph):
        self.coords = coords
        self.g = glyph
        self.x = coords[0]
        self.y = coords[1]

    def drawTo(self, point):
        line = self.g.g.line(self.coords, point.coords, stroke=svgwrite.rgb(0, 0, 0))
        self.g.g.add(line)

    def printSelf(self):
        print(self.coords)
    
class Glyph:
    def __init__(self, filename='test.svg', size=('50px', '50px')):
        self.g = svgwrite.Drawing(filename, size)
        self.origin = self.get_center(size)
        self.points = [self.origin]

    def parse_size(self, size):
        n = size[0].replace('p', '')
        new_string = n.replace('x', '')
        return new_string

    def get_center(self, size):
        width = self.parse_size(size)
        width = int(width)
        half = width / 2

        center = (half, half)
        center_point = Point(center, self)
        return center_point

    def create_point(self, coords): 
        p = Point(coords, self)
        self.points.append(p)

    def stroke(self, line):
        initPoint = self.points[-1]
        index = self.points.index(initPoint)

        n = ((initPoint.x + line[0]), initPoint.y + line[1])
        self.create_point(n)

        initPoint.drawTo(self.points[index + 1]) 

    def end(self):
        self.g.save()

    # def cirlce(self):
    #     c = self.g.circle(center=(15*cm, 8*cm), r='2.5cm', stroke='blue', stroke_width=3)
    #     self.g.add(c)
    
    def printPoints(self):
        for p in self.points:
            p.printSelf()

