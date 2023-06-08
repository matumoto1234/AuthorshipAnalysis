from utility import *
import nltk
nltk.download('punkt', quiet=True)


def _count_type(text: str) -> tuple[int, int]:
    type_set: set[str] = set()

    for token in nltk.word_tokenize(text):
        type_set.add(token)

    return len(type_set)


def type_token_ratio(text: str) -> float:
    token_count = count_token(text)
    if token_count == 0:
        return 0

    return _count_type(text) / count_token(text) * 100


def _authors_type_token_ratio_average(authors: list[str], author_to_texts: dict[str, list[list[str]]]) -> float:
    ratio_sum = 0
    num_of_text = 0

    for author in authors:
        for text in author_to_texts[author]:
            ratio_sum += type_token_ratio(text)
            num_of_text += 1

    if num_of_text == 0:
        return 0.0

    return ratio_sum / num_of_text


def type_token_analysis(male_authors: list[str], female_authors: list[str], author_to_texts: dict[str, list[list[str]]]):
    return (
        _authors_type_token_ratio_average(male_authors, author_to_texts),
        _authors_type_token_ratio_average(female_authors, author_to_texts)
    )
