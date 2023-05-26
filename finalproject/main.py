import pandas

# ここでcsvを読み込んで、pandasのDataFrame型にする
# 必要であれば色々前処理をする
def read_csv(nrows: int) -> pandas.DataFrame:
    csv = pandas.read_csv('/content/drive/MyDrive/UniversityOfAizu/2023-Q1/authorship-analysis-using-python/archive/blogtext.csv', nrows=nrows)
    return csv


def extract_authors(csv: pandas.DataFrame, target_gender: str) -> list[str]:
    authors: list[str] = []

    for i in range(len(csv)):
        author = csv[i:i+1]['sign'].values[0]
        gender = csv[i:i+1]['gender'].values[0]

        if gender == target_gender:
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


def main():
    csv = read_csv(nrows=500)

    male_authors = extract_authors(csv, 'male')
    female_authors = extract_authors(csv, 'female')
    author_to_texts = make_author_to_texts(csv)

    print(len(male_authors))
    print(len(female_authors))


if __name__ == '__main__':
    main()
