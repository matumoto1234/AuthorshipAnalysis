import nltk
nltk.download('punkt', quiet=True)
import functools


def count_token(text: str) -> int:
    tokens: list[str] = nltk.word_tokenize(text)
    return len(tokens)


def count_n_gram(text: str, tags: list[str]) -> int:
    tokens: list[str] = nltk.word_tokenize(text)
    tagged: list[tuple[str, str]] = nltk.pos_tag(tokens)

    count = 0

    for i in range(len(tagged) - (len(tags) - 1)):
        found = functools.reduce(
            lambda acc, k: acc and tagged[i + k][1] == tags[k],
            range(len(tags)),
            True,
        )

        if found:
            count += 1

    return count
