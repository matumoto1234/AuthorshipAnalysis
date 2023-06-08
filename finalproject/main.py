from adjective import *
from adverb import *
from conjunction import *
from coordinate_adjective import *
from determiner import *
from mycsv import *
from noun import *
from tensed_modalized_verb_ratio import *
from to import *
from type_token import *
from verb import *


MALE = "male"
FEMALE = "female"


def classify(text: str, training_result: dict[str, tuple[float, float]]) -> str:
    male_diff = 0
    male_diff += abs(adjective_token_ratio(text) - training_result["adjective"][0])
    male_diff += abs(adverb_token_ratio(text) - training_result["adverb"][0])
    male_diff += abs(conjunction_token_ratio(text) - training_result["conjunction"][0])
    male_diff += abs(coordinate_adjective_token_ratio(text) - training_result["coordinate_adjective"][0])
    male_diff += abs(determiner_token_ratio(text) - training_result["determiner"][0])
    male_diff += abs(noun_token_ratio(text) - training_result["noun"][0])
    male_diff += abs(tensed_verb_token_ratio(text) - training_result["tensed_modalized_verb_ratio"][0])
    male_diff += abs(to_token_ratio(text) - training_result["to"][0])
    male_diff += abs(type_token_ratio(text) - training_result["type_token"][0])
    male_diff += abs(verb_token_ratio(text) - training_result["verb"][0])

    female_diff = 0
    female_diff += abs(adjective_token_ratio(text) - training_result["adjective"][1])
    female_diff += abs(adverb_token_ratio(text) - training_result["adverb"][1])
    female_diff += abs(conjunction_token_ratio(text) - training_result["conjunction"][1])
    female_diff += abs(coordinate_adjective_token_ratio(text) - training_result["coordinate_adjective"][1])
    female_diff += abs(determiner_token_ratio(text) - training_result["determiner"][1])
    female_diff += abs(noun_token_ratio(text) - training_result["noun"][1])
    female_diff += abs(tensed_verb_token_ratio(text) - training_result["tensed_modalized_verb_ratio"][1])
    female_diff += abs(to_token_ratio(text) - training_result["to"][1])
    female_diff += abs(type_token_ratio(text) - training_result["type_token"][1])
    female_diff += abs(verb_token_ratio(text) - training_result["verb"][1])

    if male_diff > female_diff:
        return FEMALE
    else:
        return MALE


def main():
    csv = read_csv(nrows=10000)

    # トレーニング用のデータを50個選ぶ
    train_csv = csv.sample(frac=1)[:50]

    male_authors = authors_by_gender(train_csv, 'male')
    female_authors = authors_by_gender(train_csv, 'female')
    author_to_texts = make_author_to_texts(train_csv)

    training_result = {
        "adjective": adjective_token_ratio_label(male_authors, female_authors, author_to_texts),
        "adverb": adverb_token_ratio_label(male_authors, female_authors, author_to_texts),
        "conjunction": conjunction_token_ratio_label(male_authors, female_authors, author_to_texts),
        "coordinate_adjective": coordinate_adjective_token_ratio_label(male_authors, female_authors, author_to_texts),
        "determiner": determiner_token_ratio_label(male_authors, female_authors, author_to_texts),
        "noun": noun_token_ratio_label(male_authors, female_authors, author_to_texts),
        "tensed_modalized_verb_ratio": tensed_verb_token_ratio_label(male_authors, female_authors, author_to_texts),
        "to": to_token_ratio_label(male_authors, female_authors, author_to_texts),
        "type_token": type_token_analysis(male_authors, female_authors, author_to_texts),
        "verb": verb_token_ratio_label(male_authors, female_authors, author_to_texts),
    }

    # テスト用のデータをランダムに50個選ぶ
    test_csv = csv.sample(frac=1)[:50]

    text_and_gender_list = get_text_and_gender(test_csv)
    correct_count = 0
    for [text, gender] in text_and_gender_list:
        if classify(text, training_result) == gender:
            correct_count += 1

    print(f"accuracy : {correct_count / len(text_and_gender_list) * 100} [%]")

    return


if __name__ == '__main__':
    main()
