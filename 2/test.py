from regex import (
    extract_course_times,
    get_all_hashtags_and_links,
    match_first_paragraph,
)


def test_extract_course_times():
    expected = ["01:47", "32:03", "41:51", "27:48", "05:02"]
    assert extract_course_times() == expected


def test_get_all_hashtags_and_links():
    expected = ["http://pybit.es/requests-cache.html", "#python", "#APIs"]
    assert get_all_hashtags_and_links() == expected


def test_match_first_paragraph():
    expected = "pybites != greedy"
    assert match_first_paragraph() == expected
