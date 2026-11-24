def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here

    x = x0
    for _ in range(steps):

        gradient = 2 * a * x + b
        x -= lr * gradient

    return x
        
        # compute the function
        # compute the gradient of the function
        # update the weights by applying:
        # x = x - lr * gradient