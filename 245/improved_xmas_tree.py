STAR = "+"
LEAF = "*"
TRUNK = "|"


def generate_improved_xmas_tree(rows=10):
    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
       for given rows of leafs (default 10).
       For more information see the test and the bite description"""
    max_leafs = rows * 2  # Width of the longest leave row
    tree = STAR.center(max_leafs) + "\n"

    for i in range(1, max_leafs + 1, 2):
        leaf_row = LEAF * i  # Color should be added in front of the line
        tree += leaf_row.center(max_leafs) + "\n"

    # To nicely center the stump we want it to be half of the max leaf width
    # but with even number of rows we need to add one stump width
    stump_width = max_leafs // 2 + 1 if rows % 2 == 0 else max_leafs // 2

    for _ in range(2):
        stump_row = TRUNK * stump_width
        tree += stump_row.center(max_leafs) + "\n"

    return tree
