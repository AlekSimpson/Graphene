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
        print(type(self.g.g))

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
        #self.draw_self()

    def get_dest_point(self):
        dest = (self.initPoint.x + self.vector[0] + self.mod, self.initPoint.y + self.vector[1])
        destPoint = Point(dest, self.glyph)
        return destPoint

    def draw_self(self):
        self.initPoint.drawTo(self.destPoint)

class Vector:
    def __init__(self, x, y, origin=(0, 0)):
        self.x = x 
        self.y = y
        self.init  = origin
        self.final = self.get_final_point()  

    def get_final_point(self):
        dest = (self.initPoint.x + self.vector[0] + self.mod, self.initPoint.y + self.vector[1])
        return dest

class GlyphDrawable:
    def __init__(self, filename="test.svg", origin=(0, 0)):
        self.filename = filename 
        self.vectors = []
        self.origin = origin
        self.dimensions = self.get_dims()

    def get_dims(self):
        height = 1
        width = 1
        for vector in self.vectors:
            if abs(vector.x) > width:
                width = abs(vector.x)
            if abs(vector.y) > height:
                height = abs(vector.y)
        return (width, height)

class Glyph:
    def __init__(self, dims, vecs, filename='test.svg'):
        size = (str(dims[0]) + "px", str(dims[1]) + "px")
        # name of svg 
        self.filename = filename  
        self.g = svgwrite.Drawing(self.filename, size)
        print(type(self.g))
        self.lines = [] 
        self.dims = dims
        self.vectors = vecs
        
    def get_frame_center(self, dims):
        return (dims[0] / 2, dims[1] / 2)

    def center_self(self):
        frame_center = (self.dims[0] / 2, self.dims[1] / 2)
        self.last_point = Point((frame_center[0] - glyph_dims[0], frame_center[1] - glyph_dims[1]), self)

    def stroke(self, vector, origin): 
        line = Line(self, vector, origin)
        self.lines.append(line)
        self.last_point = line.destPoint 
    
    def convert_vectors(self):
        for vec in self.vectors:
            line = Line(self, (vec.x, vec.y), )

    def draw_self(self):
        for line in self.lines:
            line.draw_self()

    def end(self):
        glyph_dims = self.get_glyph_dimensions(self.lines)
        dims = (str(glyph_dims[0]) + "px", str(glyph_dims[1]) + "px")

        self.g = svgwrite.Drawing(self.filename, dims)


        frame_center = self.get_frame_center(glyph_dims)
        self.last_point = Point((frame_center[0] - glyph_dims[0], frame_center[1] - glyph_dims[1]), self)

        self.g = svgwrite.Drawing(self.filename, dims)
        for line in self.lines:
            line.draw_self()   
        
        self.g.save()

    ## Not integrated yet ##
    def cirlce(self):
         c = self.g.circle(center=(15*cm, 8*cm), r='2.5cm', stroke='black', stroke_width=3)
         self.g.add(c)

g = Glyph((2,2), (2,2))

### Pseudo code for glyph centering ###
#
# first find the center of the frame 
#
# then set the origin point of the glyph as:
#      x = frame_center.x - glyph_width
#      y = frame_center.y - glyph_height
#
#
#
#
#
#
#

# class GlyphBlock(Glyph):
#     def __init__(self, glyphs=2, gFilename='test.svg', gSize=('50px', '50px')):
#         Glyph.__init__(self, gFilename, gSize)
#         self.glyphs = glyphs

#     def create_quadrants(self):
#         print('work in progress')
