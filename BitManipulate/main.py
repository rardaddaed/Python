def setbit(x, j)
    return x | (1 << j)

def clearbit(x, j)
    return x & ~(1 << j)

def fliptbit(x, j)
    return x ^ (1 << j)

def testbit(x, j)
    return x & (1 << j) != 0

