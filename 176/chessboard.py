WHITE, BLACK = " ", "#"


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    for row in range(size):
        if row % 2 == 0:
            print("".join([WHITE if field % 2 == 0 else BLACK for field in range(size)]))
        else:
            print("".join([BLACK if field % 2 == 0 else WHITE for field in range(size)]))


if __name__ == "__main__":
    create_chessboard()
