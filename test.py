from graphene import Glyph

def createGlyph():
    g = Glyph()

    g.stroke((0, -10))

    g.stroke((-15, 0))

    # need to figure out how to have the glyph auto call save at the end of the glyph 
    g.end()

createGlyph()
