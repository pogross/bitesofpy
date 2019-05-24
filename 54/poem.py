import textwrap

INDENTS = 4

rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """


def print_hanging_indents(poem):

    for block in textwrap.dedent(poem).split("\n\n"):
        for i, line in enumerate(block.strip().splitlines()):
            if i == 0:
                print(line)
            else:
                print(" " * INDENTS + line)
