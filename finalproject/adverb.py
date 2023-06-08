import nltk
nltk.download('punkt', quiet=True)
from utility import *


def _count_adverb(text: str) -> tuple[int, int]:
    return (
        count_n_gram(text, ["RB"])
        + count_n_gram(text, ["RBR"])
        + count_n_gram(text, ["RBS"])
    )


def adverb_token_ratio(text: str):
    token_count = count_token(text)

    if token_count == 0:
        return 0

    return (_count_adverb(text) / count_token(text)) * 100


def _authors_adverb_token_ratio_average(authors: list[str], author_to_texts: dict[str, list[list[str]]]):
    ratio_sum = 0
    num_of_text = 0

    for author in authors:
        for text in author_to_texts[author]:
            ratio_sum += adverb_token_ratio(text)
            num_of_text += 1

    if num_of_text == 0:
        return 0

    return ratio_sum / num_of_text


def adverb_token_ratio_label(male_authors: list[str], female_authors: list[str], author_to_texts: dict[str, list[list[str]]]) -> tuple[float, float]:
    return (
        _authors_adverb_token_ratio_average(male_authors, author_to_texts),
        _authors_adverb_token_ratio_average(female_authors, author_to_texts)
    )

