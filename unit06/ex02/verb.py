import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


from enum import Enum
import nltk

# count_modalized_verbs(sentence: str) : count modalized verbs in sentence
#   sentenceを品詞に置き換えて、["MD", "VB"] となっている箇所を数える
def count_modalized_verbs(sentence: str) -> int:
    tokens: list[str] = nltk.word_tokenize(sentence)
    tagged: list[tuple[str, str]] = nltk.pos_tag(tokens)

    count = 0

    for i in range(len(tagged)-1):
        tag = tagged[i]
        next_tag = tagged[i+1]

        if tag == "MD" and next_tag == "VB":
            count += 1

    return count


# count_tensed_verbs(sentence: str) : count tensed verbs in sentence
#   sentenceを品詞に置き換えて、["VBD" | "VBG" | "VBN" | "VBP" | "VBZ"] となっている箇所を数える
def count_tensed_verbs(sentence: str) -> int:
    tokens: list[str] = nltk.word_tokenize(sentence)
    tagged: list[tuple[str, str]] = nltk.pos_tag(tokens)

    count = 0

    for i in range(len(tagged)):
        tag = tagged[i]

        if tag in ["VBD", "VBG", "VBN", "VBP", "VBZ"]:
            count += 1

    return count


# is_tensed(sentence: str) : return true if sentence is "tensed sentence"
#.  "tensed sentence" means using many times tensed verb in the sentence (I created the word)
#   tensed verbの数がmodalized verbの数より多いならTrueとしてる
def is_tensed(sentence: str) -> bool:
    return count_tensed_verbs(sentence) > count_modalized_verbs(sentence)


# VerbCategory : category of verb about one sentence
#   TENSED : その文がtensed verbが多く使われていることを示す
#   MODALIZED : その文がmodalized verbが多く使われていることを示す
class VerbCategory(Enum):
    TENSED = 1
    MODALIZED = 2


# classify_adjective(sentence: str) : classify adjective about one sentence
def classify_verb(sentence: str) -> VerbCategory:
    if is_tensed(sentence):
        return VerbCategory.TENSED

    return VerbCategory.MODALIZED


def main():
    # テストを用意して、正確性を確認する
    tensed_sentences: list[str] = [
        "The police found it.",
        "I ate a cake.",
        "She has a nice bag.",
        "We want to go to aizu."
    ]

    modalized_sentences: list[str] = [
        "The police may have found it.",
        "You can do it.",
        "I will eat the dinner.",
        "I should buy a milk.",
        "Would you like something to drink?",
        "Can I visit that place?",
        "I have to finish this homework."
    ]

    correct = 0
    for sentence in tensed_sentences:
        if classify_verb(sentence) == VerbCategory.TENSED:
            correct += 1

    for sentence in modalized_sentences:
        if classify_verb(sentence) == VerbCategory.MODALIZED:
            correct += 1


    all_size = len(tensed_sentences) + len(modalized_sentences)

    print("all test case size :", all_size)
    print("classification accuracy :", correct / all_size * 100, "%")


main()
