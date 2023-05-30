from main import extract_authors, make_author_to_texts
from enum import Enum
import matplotlib.pyplot as plt
import nltk
import functools
nltk.download('punkt', quiet=True)


# count_coordinate_adjectives(sentence: str) : count coordinate adjectives in sentence
#   sentenceを品詞に置き換えて、["JJ", ",", "JJ"] となっている箇所を数える
#   e.g.
#     "I have a new, expensive car." -> 1
def count_coordinate_adjectives(sentence: str) -> int:
    tokens: list[str] = nltk.word_tokenize(sentence)
    tagged: list[tuple[str, str]] = nltk.pos_tag(tokens)

    count = 0

    for i in range(len(tagged) - 2):
        tag = tagged[i][1]
        next_token = tagged[i + 1][0]
        after_next_tag = tagged[i + 2][1]

        if tag == "JJ" and next_token == "," and after_next_tag == "JJ":
            count += 1

    return count


# count_non_coordinate_adjectives(sentence: str) : count non-coordinate adjectives in sentence
#   sentenceを品詞に置き換えて、["JJ", "JJ"] となっている箇所を数える
#   e.g.
#     "I have a new expensive car." -> 1
#     "I have a new expensive nice car." -> 2
def count_non_coordinate_adjectives(sentence: str) -> int:
    tokens: list[str] = nltk.word_tokenize(sentence)
    tagged: list[tuple[str, str]] = nltk.pos_tag(tokens)

    count = 0

    for i in range(len(tagged) - 1):
        tag = tagged[i][1]
        next_tag = tagged[i + 1][1]

        if tag == "JJ" and next_tag == "JJ":
            count += 1

    return count


# is_coordinate(sentence: str) : return true if sentence is coordinate adjective
#   coordinate adjectivesの数がnon-coordinate adjectivesの数より多いならTrueとしてる
def is_coordinate(sentence: str) -> bool:
    return count_coordinate_adjectives(sentence) > count_non_coordinate_adjectives(sentence)


# AdjectiveCategory : category of adjective about one sentence
#   COORDINATE : その文がcoordinate adjectiveが使われていることを示す
#   NON_COORDINATE : その文がnon-coordinate adjectiveが使われていることを示す
class AdjectiveCategory(Enum):
    COORDINATE = 1
    NON_COORDINATE = 2


# classify_adjective(sentence: str) : classify adjective about one sentence
def classify_adjective(sentence: str) -> AdjectiveCategory:
    if is_coordinate(sentence):
        return AdjectiveCategory.COORDINATE

    return AdjectiveCategory.NON_COORDINATE


def adjective_analysis(
    male_authors: list[str],
    female_authors: list[str],
    author_to_texts: dict[str, list[list[str]]]
):
    male_coordinate_sum = 0

    for male_author in male_authors:
        for texts in author_to_texts[male_author]:
            for text in texts:
                male_coordinate = count_coordinate_adjectives(text)
                male_coordinate_sum += male_coordinate

    female_coordinate_sum = 0

    for female_author in female_authors:
        for texts in author_to_texts[female_author]:
            for text in texts:
                female_coordinate = count_coordinate_adjectives(text)
                female_coordinate_sum += female_coordinate

    male_non_coordinate_sum = 0

    for male_author in male_authors:
        for texts in author_to_texts[male_author]:
            for text in texts:
                male_non_coordinate = count_non_coordinate_adjectives(text)
                male_non_coordinate_sum += male_non_coordinate

    female_non_coordinate_sum = 0

    for female_author in female_authors:
        for texts in author_to_texts[female_author]:
            for text in texts:
                female_non_coordinate = count_non_coordinate_adjectives(text)
                female_non_coordinate_sum += female_non_coordinate

    plt.bar(
        list([
            'male coordinate adjectives',
            'male non-coordinate adjectives',
            'female coordinate adjectives',
            'female non-coordinate adjectives',
        ]),
        list([
            male_coordinate_sum,
            male_non_coordinate_sum,
            female_coordinate_sum,
            female_non_coordinate_sum,
        ]),
    )

    plt.xlabel("male and female")
    plt.ylabel("type token ratio [%]")
    plt.title("type token ratio")
    plt.show()


def _test():
    import pandas

    csv = pandas.read_csv('~/Downloads/blogtext.csv', nrows=1000)

    male_authors = extract_authors(csv, 'male')
    female_authors = extract_authors(csv, 'female')
    author_to_texts = make_author_to_texts(csv)

    adjective_analysis(male_authors, female_authors, author_to_texts)


if __name__ == '__main__':
    _test()
    print('Test passed!')
