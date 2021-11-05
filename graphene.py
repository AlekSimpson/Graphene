import svgwrite

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
        self.last_point = self.get_center(size)

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

    def init_point(self, coords):
        p = Point(coords, self)
        return p 

    def invert_stroke_vector(self, vector):
        new = (vector[0], vector[1] * -1)
        return new

    def stroke(self, vector):
        new_vec = self.invert_stroke_vector(vector)
        init_point = self.init_point((self.last_point.x + 0.5, self.last_point.y))
        if new_vec[0] > 0:
            init_point = self.init_point((self.last_point.y + 0.5, self.last_point.y))

        n = (init_point.x + new_vec[0], init_point.y + new_vec[1])
        new_point = Point(n, self)

        init_point.drawTo(new_point)
        self.last_point = new_point

    def end(self):
        self.g.save()

    # def cirlce(self):
    #     c = self.g.circle(center=(15*cm, 8*cm), r='2.5cm', stroke='blue', stroke_width=3)
    #     self.g.add(c)
    
    def printPoints(self):
        for p in self.points:
            p.printSelf()

class GlyphBlock(Glyph):
    def __init__(self, glyphs=2, gFilename='test.svg', gSize=('50px', '50px')):
        Glyph.__init__(self, gFilename, gSize)
        self.glyphs = glyphs

    def create_quadrants(self):
        print('work in progress')
