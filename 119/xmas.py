def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    spaces = rows * 2 - 1
    tree = ""

    for i in range(1, rows + 1):
        stars = "*" * (i * 2 - 1)
        tree += stars.center(spaces) + "\n"

    return tree.rstrip()
