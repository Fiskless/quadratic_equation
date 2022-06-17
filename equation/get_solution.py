def calculate_solution(a, b, c):
    if a == 0 and b == 0:
        return None, None
    if a == 0:
        return -c / b, None
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5)/(2 * a)
        x2 = (-b - discriminant ** 0.5)/(2 * a)
    elif discriminant == 0:
        x1 = -b / (2 * a)
        x2 = None
    else:
        x1 = None
        x2 = None
    return x1, x2