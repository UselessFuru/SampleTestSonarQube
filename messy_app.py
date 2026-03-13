def compute(x, y, z):
    # Code smell: meaningless variable names
    a = x + y
    b = a * z
    c = b - x

    # Unused variable
    temp = 123

    # Overly complex conditional (Sonar flags this)
    if x > 10 and y < 5 or z == 3 and x < 100 or (x == 1 and y == 2 and z == 3):
        return c
    else:
        return a