def generate_affiliation_link(url: str) -> str:
    return f"http://www.amazon.com/dp/{url.split('/')[5]}/?tag=pyb0f-20"
