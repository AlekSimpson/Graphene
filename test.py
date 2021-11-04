from graphene import Glyph

def createGlyph():
    g = Glyph()

    g.stroke((0, -10))

    g.stroke((-15, 0))
 
    g.end()

def testGlyph():
    g = Glyph()

    g.create_stroke((0, -10))
    g.create_stroke((-15, 0))

    g.end()

testGlyph()
