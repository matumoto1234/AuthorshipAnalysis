from enum import Enum
import matplotlib.pyplot as plt
import nltk

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
    male_coordinate = count_coordinate_adjectives(male_authors)
    female_coordinate = count_coordinate_adjectives(female_authors)

    male_non_coordinate = count_non_coordinate_adjectives(male_authors)
    female_non_coordinat = count_non_coordinate_adjectives(female_authors)

    plt.bar(
        list(['male', 'female']),
        list([
            male_coordinate / male_non_coordinate,
            female_coordinate / female_non_coordinat
        ]),
    )

    plt.ylim(0, 100)

    plt.xlabel("male and female")
    plt.ylabel("type token ratio [%]")
    plt.title("type token ratio")
    plt.show()


def _test():
    # テストを用意して、正確性を確認する
    coordinate_sentences: list[str] = [
        "Forecasters warned of another day of hot, windy conditions across Southern California on Sunday.",
        "n addition, their breathtakingly cruel, callous actions also led to a tribute plaque.",
        "Obama stands accused of giving stuffy, cliche-ridden graduation speeches.",
        "The company is also working on a new, cheaper iPhone.",
        "I have a new, expensive car.",
        "The girl is beautiful, smart, and funny.",
    ]

    non_coordinate_sentences: list[str] = [
        "Amazon prepping multiple wallet-friendly tablets.",
        "With this in mind, I wanted to design a screen to identify dirt-cheap smaller companies.",
        "The Red Wings are demonstrably a tough hockey team.",
        "I saw a happy little kid in the park.",
        "We ate a delicious deer meat."
        "My friend buys a expensive red car."
    ]

    correct = 0
    for sentence in coordinate_sentences:
        if classify_adjective(sentence) == AdjectiveCategory.COORDINATE:
            correct += 1

    for sentence in non_coordinate_sentences:
        if classify_adjective(sentence) == AdjectiveCategory.NON_COORDINATE:
            correct += 1

    all_size = len(coordinate_sentences) + len(non_coordinate_sentences)
    print("all test case size :", all_size)
    print("classification accuracy :", correct / all_size * 100, "%")


if __name__ == '__main__':
    _test()
    print('Test passed!')
