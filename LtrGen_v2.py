from Graphene import draw_line, fin, Point   

draw_line((0, 10))
draw_line((-10, 0))
draw_line((0, -10))
draw_line((10, 0), (0, 5, -1))

fin("m.svg")
