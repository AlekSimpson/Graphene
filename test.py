from graphene import Glyph

def createGlyph():
    g = Glyph()
    
    g.stroke((0, 10))
    
    g.stroke((-15, 0))
    
    g.stroke((0, -10))
    
    g.stroke((15, 0))
 
    g.end()

createGlyph()
