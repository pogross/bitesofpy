from itertools import zip_longest
import textwrap

COL_WIDTH = 20


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    paragraphs = [
        textwrap.wrap(paragraph.strip(), width=COL_WIDTH)
        for paragraph in text.split("\n\n")
    ]
    rows = [" ".join(row).strip() for row in zip_longest(*paragraphs, fillvalue=" ")]

    return "\n".join(rows)
