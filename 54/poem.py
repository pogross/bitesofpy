import textwrap

INDENTS = 4


def print_hanging_indents(poem):

    for block in textwrap.dedent(poem).split("\n\n"):
        for i, line in enumerate(block.strip().splitlines()):
            if i == 0:
                print(line)
            else:
                print(" " * INDENTS + line)
