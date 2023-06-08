import pandas
import re


def read_csv(nrows: int) -> pandas.DataFrame:
    csv = pandas.read_csv('/home/matumoto/code_box/lecture/AuthorshipAnalysis/AuthorshipAnalysis/finalproject/blogtext.csv', nrows=nrows)
    return csv


# csvのテキストを前処理
def cleaning(csv: pandas.DataFrame):
    # [^A-Za-z]+を空白に置換する
    csv['clean_text'] = csv['text'].apply(lambda x: re.sub(r'[^A-Za-z]+',' ',x))

    # 小文字に変換する
    csv['clean_text'] = csv['clean_text'].apply(lambda x: x.lower())

    # 前後の空白を削除する
    csv['clean_text'] = csv['clean_text'].apply(lambda x: x.strip())
    csv['text'] = csv['clean_text']


def authors_by_gender(csv: pandas.DataFrame, target: str) -> list[str]:
    authors: list[str] = []

    for i in range(len(csv)):
        author = csv[i:i+1]['sign'].values[0]
        gender = csv[i:i+1]['gender'].values[0]

        if gender == target:
            authors.append(author)

    return authors


def make_author_to_texts(csv: pandas.DataFrame) -> dict[str, list[list[str]]]:
    author_to_texts: dict[str, list[list[str]]] = {}

    for i in range(len(csv)):
        author = csv[i:i+1]['sign'].values[0]
        text = csv[i:i+1]['text'].values[0]

        if author in author_to_texts:
            author_to_texts[author].append(text)
        else:
            author_to_texts[author] = [text]

    return author_to_texts


def get_text_and_gender(csv: pandas.DataFrame) -> list[tuple[str, str]]:
    return list(map(
        lambda i: (csv[i:i+1]['text'].values[0], csv[i:i+1]['gender'].values[0]),
        range(len(csv))
    ))