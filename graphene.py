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
    
class Line:
    def __init__(self, glyph, vector, initPoint):
        self.glyph = glyph 
        self.mod = -0.5 if vector[0] > 0 else 0.5 
        self.vector = (vector[0], vector[1] * -1)
        self.initPoint = initPoint
        self.destPoint = self.get_dest_point()
        self.initPoint = Point((initPoint.x + self.mod, initPoint.y), self.glyph) 
        self.draw_self()

    def get_dest_point(self):
        dest = (self.initPoint.x + self.vector[0] + self.mod, self.initPoint.y + self.vector[1])
        destPoint = Point(dest, self.glyph)
        return destPoint

    def draw_self(self):
        self.initPoint.drawTo(self.destPoint)

class Glyph:
    def __init__(self, filename='test.svg', size=15):
        s = str(size) + "px"
        self.filename = filename
        self.size = (s, s)
        self.g = svgwrite.Drawing(self.filename, self.size)
        center_num = (size / 2)
        self.lines = []
        self.last_point = Point((center_num, center_num), self)

    def get_glyph_dimensions(self, lines):
        height = 0
        width = 0
        for line in lines:
            if line.vector[1] > 0 and line.vector[1] > height:
                height = line.vector[1]
            if line.vector[0] > 0 and line.vector[0] > width: 
                width = line.vector[0]
        return (width, height)
        
    def stroke(self, vector, origin=None):
        origin = self.last_point if origin == None else origin 
        line = Line(self, vector, origin)
        self.lines.append(line)
        self.last_point = line.destPoint 

    def end(self):
        #glyph_dims = self.get_glyph_dimensions(self.lines)
        #for line in self.lines:
            #    line.draw_self()

        #print(glyph_dims, self.filename)

        self.g.save()

    ## Not integrated yet ##
    def cirlce(self):
         c = self.g.circle(center=(15*cm, 8*cm), r='2.5cm', stroke='black', stroke_width=3)
         self.g.add(c)

# class GlyphBlock(Glyph):
#     def __init__(self, glyphs=2, gFilename='test.svg', gSize=('50px', '50px')):
#         Glyph.__init__(self, gFilename, gSize)
#         self.glyphs = glyphs

#     def create_quadrants(self):
#         print('work in progress')
