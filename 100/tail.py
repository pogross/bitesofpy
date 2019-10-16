def tail(filepath: str, n: int):
    """Simulate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    with open(filepath, "r") as f:
        return f.read().splitlines()[-n:]
