def compute_intersecting_squares(starting_point, ending_point):
    dx = ending_point[0] - starting_point[0]
    dy = ending_point[1] - starting_point[1]
    points = []
    if dx == 0 or dy == 0 or abs(dx) == abs(dy):
        step_x = 1 if dx > 0 else -1 if dx < 0 else 0
        step_y = 1 if dy > 0 else -1 if dy < 0 else 0
        for i in range(1, max(abs(dx), abs(dy)) + 1):
            points.append((starting_point[0] + i * step_x, starting_point[1] + i * step_y))
    else:
        x = starting_point[0]
        y = starting_point[1]
        end_x = ending_point[0]
        end_y = ending_point[1]
        points.append((x, y))
        while x != end_x or y != end_y:
            if abs(dx) > abs(dy):
                x += 1 if dx > 0 else -1
                y = round(starting_point[1] + (dy/dx) * (x - starting_point[0]))
            else:
                y += 1 if dy > 0 else -1
                x = round(starting_point[0] + (dx/dy) * (y - starting_point[1]))
            if (x, y) != (end_x, end_y):
                points.append((x, y))
    return points