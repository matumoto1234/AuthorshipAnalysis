# Team I
# Hibiki Matsumoto(Team Leader) : contribution 30%
# Yuto Takamune : contribution 20%
# Syunsuke Suzuki : contribtion 30%
# Takeshi Kato : contribution 20%



# The pseudocode of classification verbs in a sentence.
# This code classify a given sentence is "tensed sentence" or "modalized sentence"
# "tensed sentence" means appearing many times tensed verbs in a sentence.
# "modalized sentence" means appearing many times modalized verbs in a sentence.

def is_tensed_sentence(sentence):
    return count_tensed_verbs(sentence) > count_modalized_verbs(sentence)


def main():

    tensed_sentences = get_tensed_sentences()

    tensed_sentence_count = 0

    for sentence in tensed_sentences:
        if is_tensed_sentence(sentence):
          tensed_sentence_count += 1

    modalized_sentences = get_modalized_sentences()

    modalized_sentence_count = 0

    for sentence in modalized_sentences:
        if not is_tensed_sentence(sentence):
            modalized_sntence_count += 1

    all_len = len(tensed_sentences) + len(modalized_sntences)
    accuracy = (tensed_sentence_count + modalized_sentence_count) / all_len

    print(accuracy)
