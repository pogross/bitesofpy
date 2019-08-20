def countdown():
    """Write a generator that counts from 100 to 1"""
    cd = 100
    while cd > 0:
        yield cd
        cd -= 1
