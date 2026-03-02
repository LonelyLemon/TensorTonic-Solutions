def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    i = 1
    while(i <= steps):
        i += 1
        der = 2*a*x0 + b
        x0 = x0 - lr*der

    return x0