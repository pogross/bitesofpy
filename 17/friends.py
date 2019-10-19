from itertools import permutations, combinations


def friends_teams(
    list_of_friends: list, team_size: int = 2, order_does_matter: bool = False
):

    if order_does_matter:
        return list(permutations(list_of_friends, team_size))
    else:
        return list(combinations(list_of_friends, team_size))
