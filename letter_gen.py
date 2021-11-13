from graphene import Glyph, Point 

def draw_m():
    g = Glyph('m.svg')

    g.stroke((0, 10))
    g.stroke((-10, 0))
    g.stroke((0, -10))
    g.stroke((10, 0))

    g.end()

draw_m()

def draw_a():
    g = Glyph('a.svg')

    g.stroke((0, 10))
    p = Point((g.last_point.x, g.last_point.y + 5), g)
    g.stroke((2, 0), p)

    g.end()

draw_a()

def draw_u():
    g = Glyph('u.svg')

    g.stroke((0, 10))
    p = Point((g.last_point.x, g.last_point.y + 5), g)
    g.stroke((-2, 0), p)

    g.end()

draw_u()

def draw_g():
    g = Glyph('g.svg')

    g.stroke((0, 4))
    g.stroke((-10, 0))

    g.end()

draw_g()

def draw_n():
    g = Glyph('n.svg')

    g.stroke((-10, 0))
    g.stroke((0, 4))

    g.end()

draw_n()

def draw_d():
    g = Glyph('d.svg')

    g.stroke((-10, 0))
    g.stroke((0, 8))
    g.stroke((10, 0))

    g.end()

draw_d()

# need a way to change focus between lines

def draw_t():
    g = Glyph('t.svg')

    # stroke 0
    g.stroke((-10, 0))
    # stroke 1
    g.stroke((0, 8))
    # stroke 2
    p = Point((g.last_point.x, g.last_point.y + 4), g)
    g.stroke((10, 0), p)
    # stroke 4
    p = g.lines[1].destPoint
    g.stroke((10, 0), p)

    g.end()

draw_t()

def draw_b():
    g = Glyph('b.svg')

    g.stroke((0, -10))
    g.stroke((-5, 0))
    g.stroke((0, 10))
    p = Point((g.last_point.x, g.last_point.y + 7), g)
    g.stroke((5, 0), p)

    g.end()

draw_b()

def draw_s():
    g = Glyph('s.svg')

    g.stroke((5, 5))
    g.stroke((5, -5))

    g.end()

draw_s()

def draw_l():
    g = Glyph('l.svg')

    g.stroke((-10, 0))
    g.stroke((0, 5))
    g.stroke((10, 0))
    g.stroke((0, 5))
    g.stroke((-10, 0))

    g.end()

draw_l()

def draw_o():
    g = Glyph('o.svg')

    g.stroke((-10, 0))
    p = Point((g.last_point.x + 4.5, g.last_point.y), g)
    g.stroke((0, 4), p)

    g.end()

draw_o()

def draw_uu():
    g = Glyph('uu.svg')

    g.stroke((-10, 0))
    p = Point((g.last_point.x + 4.5, g.last_point.y), g)
    g.stroke((0, -4), p)

    g.end()

draw_uu()

def draw_i():
    g = Glyph('i.svg')

    g.stroke((0, 10))
    
    g.end()

draw_i()

def draw_eu():
    g = Glyph('eu.svg')

    g.stroke((-10, 0))

    g.end()

draw_eu()

def draw_e():
    g = Glyph('e.svg')

    g.stroke(())

    g.end()

#draw_e()
