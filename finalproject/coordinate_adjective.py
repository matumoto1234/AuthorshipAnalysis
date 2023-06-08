import nltk
nltk.download('punkt', quiet=True)
from utility import *


def _count_coordinate_adjective(text: str) -> tuple[int, int]:
    return count_n_gram(text, ["JJ", ",", "JJ"])


def _count_non_coordinate_adjective(text: str) -> tuple[int, int]:
    return count_n_gram(text, ["JJ", "JJ"])


def coordinate_adjective_token_ratio(text: str):
    non_coordinate_adjective_count = _count_non_coordinate_adjective(text)

    if non_coordinate_adjective_count == 0:
        return 0

    return (_count_coordinate_adjective(text) / _count_non_coordinate_adjective(text)) * 100


def _authors_coordinate_adjective_token_ratio_average(authors: list[str], author_to_texts: dict[str, list[list[str]]]):
    ratio_sum = 0
    num_of_text = 0

    for author in authors:
        for text in author_to_texts[author]:
            ratio_sum += coordinate_adjective_token_ratio(text)
            num_of_text += 1

    if num_of_text == 0:
        return 0

    return ratio_sum / num_of_text


def coordinate_adjective_token_ratio_label(male_authors: list[str], female_authors: list[str], author_to_texts: dict[str, list[list[str]]]) -> tuple[float, float]:
    return (
        _authors_coordinate_adjective_token_ratio_average(male_authors, author_to_texts),
        _authors_coordinate_adjective_token_ratio_average(female_authors, author_to_texts)
    )
