from main import extract_authors, make_author_to_texts
import matplotlib.pyplot as plt
import nltk
nltk.download('punkt', quiet=True)


def _type_token_count(text: str) -> tuple[int, int]:
    tokens: list[str] = nltk.word_tokenize(text)
    if tokens == []:
        return 0

    type_set: set[str] = set()
    for token in tokens:
        type_set.add(token)

    return len(type_set), len(tokens)


def _type_token_ratio(authors: list[str], author_to_texts: dict[str, list[list[str]]]) -> float:
    type_count_sum: int = 0
    token_count_sum: int = 0

    for author in authors:
        for text in author_to_texts[author]:
            type_count, token_count = _type_token_count(text)
            type_count_sum += type_count
            token_count_sum += token_count

    if token_count_sum == 0:
        return 0.0

    return type_count_sum / token_count_sum * 100


def token_analysis(male_authors: list[str], female_authors: list[str], author_to_texts: dict[str, list[list[str]]]):
    male_ttr: float = _type_token_ratio(male_authors, author_to_texts)
    female_ttr: float = _type_token_ratio(female_authors, author_to_texts)

    plt.bar(
        list(['male TTR', 'female TTR']),
        list([male_ttr, female_ttr])
    )

    # 100%をy軸目盛りの最大値にする
    plt.ylim(0, 100)

    plt.xlabel("male and female")
    plt.ylabel("type token ratio [%]")
    plt.title("type token ratio")
    plt.show()


def _test_token_analysis():
    import pandas

    csv = pandas.read_csv('~/Downloads/blogtext.csv', nrows=100)

    male_authors = extract_authors(csv, 'male')
    female_authors = extract_authors(csv, 'female')
    author_to_texts = make_author_to_texts(csv)

    token_analysis(male_authors, female_authors, author_to_texts)


if __name__ == '__main__':
    _test_token_analysis()
    print('Test passed!')
