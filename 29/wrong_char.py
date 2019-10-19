ALPHANUMERIC = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def get_index_different_char(chars: list) -> int:
    alpha_count = 0
    non_alpha_count = 0

    for index, char in enumerate(chars):
        if str(char) in ALPHANUMERIC and str(char) != "":
            alpha_count = alpha_count + 1
            alpha_index = index
        else:
            non_alpha_count = non_alpha_count + 1
            non_index = index

        if alpha_count > 1 and non_alpha_count == 1:
            return non_index
        elif non_alpha_count > 1 and alpha_count == 1:
            return alpha_index
