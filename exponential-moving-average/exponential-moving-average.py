def exponential_moving_average(values: list, alpha: float) -> list:
    """
    Returns the exponential moving average at every position.
    """
    # Write code here
    ema = values.copy()

    for t in range(1, len(values)):
       ema[t] = alpha * ema[t] + (1 - alpha) * ema[t - 1]
    return ema