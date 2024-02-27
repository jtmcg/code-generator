def compute_intersecting_squares(starting_point, ending_point):
    x0, y0 = starting_point
    x1, y1 = ending_point
    dx = x1 - x0
    dy = y1 - y0
    points = []
    if dx == 0 or dy == 0 or abs(dx) == abs(dy):
        step_x = 1 if dx > 0 else -1
        step_y = 1 if dy > 0 else -1
        for x in range(x0 + step_x, x1, step_x):
            for y in range(y0 + step_y, y1, step_y):
                if abs(x - x0) == abs(y - y0):
                    points.append((x, y))
    else:
        slope = dy / dx
        if abs(slope) < 1:
            step = 1 if dx > 0 else -1
            for x in range(x0 + step, x1, step):
                y = y0 + round(slope * (x - x0))
                if x != x1:
                    points.append((x, y))
        else:
            step = 1 if dy > 0 else -1
            for y in range(y0 + step, y1, step):
                x = x0 + round((y - y0) / slope)
                if y != y1:
                    points.append((x, y))
    return points