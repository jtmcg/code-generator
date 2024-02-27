def compute_intersecting_squares(starting_point, ending_point):
    x0, y0 = starting_point
    x1, y1 = ending_point
    points = []
    dx = x1 - x0
    dy = y1 - y0
    is_steep = abs(dy) > abs(dx)
    if is_steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    swapped = False
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
        swapped = True
    dx = x1 - x0
    dy = y1 - y0
    error = int(dx / 2.0)
    ystep = 1 if y0 < y1 else -1
    y = y0
    for x in range(x0, x1 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx
    if swapped:
        points.reverse()
    if starting_point in points:
        points.remove(starting_point)
    if ending_point in points:
        points.remove(ending_point)
    return points