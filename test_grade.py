import pytest

from grade import average, letter_grade


@pytest.mark.parametrize(
    "score, expected",
    [
        (95, ____),
        (80, ____),
        (60, ____),
        (59, ____),
    ],
)
def test_letter_grade_valid_scores(score, expected):
    assert letter_grade(score) == ____


@pytest.mark.parametrize("score", [____, ____])
def test_letter_grade_invalid_scores(score):
    with pytest.raises(____):
        letter_grade(score)


def test_average_scores():
    assert average([80, 90, 100]) == ____


def test_average_empty_list_raises_error():
    with pytest.raises(____):
        average([])
