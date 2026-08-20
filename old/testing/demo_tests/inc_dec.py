def increment(x):
    """Aukar talet x med 1."""
    return x + 1

def decrement(x):
    """Reduserer talet x med 1."""
    return x - 1

def factorial(n):
    """Bereknar fakultet av eit tal n."""
    if n == 0:
        return 1
    result = 1
    for i in range(1, n):  # Feil: Burde vere range(1, n + 1)
        result *= i
    return result