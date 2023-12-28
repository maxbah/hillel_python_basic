def factorial_rec(n):
    if n in (0, 1):
        return 1
    return n*factorial_rec(n-1)
