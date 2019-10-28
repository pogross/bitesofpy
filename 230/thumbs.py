THUMBS_UP, THUMBS_DOWN = "👍", "👎"


class Thumbs:
    pass

    def __mul__(self, other):
        try:
            amount = int(other)
            if amount == 0:
                raise ValueError
        except ValueError:
            raise ValueError("Specify a number")

        thumb = THUMBS_UP if amount > 0 else THUMBS_DOWN
        amount = abs(amount)

        if amount >= 4:
            return f"{thumb} ({amount}x)"
        else:
            return f"{thumb * amount}"

    __rmul__ = __mul__
