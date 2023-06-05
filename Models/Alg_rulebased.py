from Utils.extract_words import *

def identify_scope(text, End_sentence, End_word, negations_cues, uncertainty_cues):

    sentences_of_text = []
    sentence = []

    negation_found    = False
    uncertainti_found = False

    all_words = list(get_nextWord(text, End_word))
    for _, token in all_words:
        tag = (token, "other")

        if token in negations_cues:
            negation_found    = True
            tag = (token, "NEG")

        elif token in uncertainty_cues:
            uncertainti_found = True
            tag = (token, "UNC")

        sentence.append(tag)

        if any(char in token for char in End_sentence):  #Look if any char in the token contains an end of sentence character.

            if (negation_found):
              sentence = [(tag[0], "NSCO") if tag[1] == 'other' else tag for tag in sentence]

            elif (uncertainti_found):
              sentence = [(tag[0], "USCO") if tag[1] == 'other' else tag for tag in sentence]

            sentences_of_text.extend(sentence)

            sentence          = []
            negation_found    = False
            uncertainti_found = False
    # Devolver la lista de oraciones con la negación y su scope
    return sentences_of_text