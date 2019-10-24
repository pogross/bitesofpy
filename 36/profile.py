def get_profile(name, age, *sports, **awards):
    if not isinstance(age, int) or len(sports) > 5:
        raise ValueError

    profile = {"name": name, "age": age}
    if sports:
        profile["sports"] = sorted(sports)
    if awards:
        profile["awards"] = awards

    return profile
