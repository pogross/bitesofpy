import sys

INTERNAL_LINKS = ("pybit.es", "codechalleng.es")


def make_html_links():
    for line in sys.stdin:
        if "http" in line and line.count(",") == 1:
            link, text = line.split(",")

            blank = ' target="_blank"'
            if any(il in link for il in INTERNAL_LINKS):
                blank = ""

            print(f'<a href="{link.strip()}"{blank}>{text.strip()}</a>')


if __name__ == "__main__":
    make_html_links()
