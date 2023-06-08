import nltk
nltk.download('punkt', quiet=True)
from utility import *


def _count_tensed_verb(text: str) -> tuple[int, int]:
    return (
        count_n_gram(text, ["VBD"])
        + count_n_gram(text, ["VBG"])
        + count_n_gram(text, ["VBN"])
        + count_n_gram(text, ["VBP"])
        + count_n_gram(text, ["VBZ"])
    )


def _count_modalized_verb(text: str) -> tuple[int, int]:
    return count_n_gram(text, ["MD"])


def tensed_verb_token_ratio(text: str):
    modalized_verb_count = _count_modalized_verb(text)
    if modalized_verb_count == 0:
        return 0
    return (_count_tensed_verb(text) / _count_modalized_verb(text)) * 100


def _authors_tensed_verb_token_ratio_average(authors: list[str], author_to_texts: dict[str, list[list[str]]]):
    ratio_sum = 0
    num_of_text = 0

    for author in authors:
        for text in author_to_texts[author]:
            ratio_sum += tensed_verb_token_ratio(text)
            num_of_text += 1

    if num_of_text == 0:
        return 0

    return ratio_sum / num_of_text


def tensed_verb_token_ratio_label(male_authors: list[str], female_authors: list[str], author_to_texts: dict[str, list[list[str]]]) -> tuple[float, float]:
    return (
        _authors_tensed_verb_token_ratio_average(male_authors, author_to_texts),
        _authors_tensed_verb_token_ratio_average(female_authors, author_to_texts)
    )
