import pandas

# ここでcsvを読み込んで、pandasのDataFrame型にする
# 必要であれば色々前処理をする
def read_csv() -> pandas.DataFrame:
    # google drive path
    csv = pandas.read_csv('/content/drive/MyDrive/UniversityOfAizu/2023-Q1/authorship-analysis-using-python/archive/blogtext.csv', nrows = 10000)
    return csv


def main():
    csv = read_csv()

    # male_authors, female_authorsの構築
    male_authors: list[str] = []
    female_authors: list[str] = []

    for i in range(len(csv)):
        author = csv[i:i+1]['sign'].values[0]
        gender = csv[i:i+1]['gender'].values[0]

        if gender == 'male':
            male_authors.append(author)
        elif gender == 'female':
            female_authors.append(author)

    # author_to_textsの構築
    author_to_texts: dict[str, list[list[str]]] = {}

    for i in range(len(csv)):
        author = csv[i:i+1]['sign'].values[0]
        text = csv[i:i+1]['text'].values[0]

        if author in author_to_texts:
            author_to_texts[author].append(text)
        else:
            author_to_texts[author] = [text]

    print(len(male_authors))
    print(len(female_authors))


main()
