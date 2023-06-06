# File containing the features considering the Pos taggin information

import re

def get_word_to_crf_features_POS(sentence, word_idx):
    word, POS, _ = sentence[word_idx]

    def word_shape(word):
        return re.sub('[a-z]', 'x', re.sub('[A-Z]', 'X', re.sub('[0-9]', 'd', word)))

    features = [
        'bias',
        'word.lower=' + word.lower(),
        'word.isdigit=%s' % word.isdigit(),
        'word.length=%d' % len(word),
        'word.shape=' + word_shape(word),
        'word.prefix_2=' + word[:2],
        'word.prefix_3=' + word[:3],
        'word.suffix_2=' + word[-2:],
        'word.suffix_3=' + word[-3:],
        'word.POS=' + POS
    ]

    if word_idx > 2:
        prev_word2, prev_POS2, _ = sentence[word_idx-2]
        prev_word1, prev_POS1, _ = sentence[word_idx-1]
        features.extend([
            'prev_word2.lower=' + prev_word2.lower(),
            'prev_word2.isdigit=%s' % prev_word2.isdigit(),
            'prev_word2.POS=' + prev_POS2,
            'prev_word1.lower=' + prev_word1.lower(),
            'prev_word1.isdigit=%s' % prev_word1.isdigit(),
            'prev_word1.POS=' + prev_POS1
        ])
    else:
        features.extend(['bos', 'bos', 'bos'])

    if word_idx < len(sentence) - 3:
        next_word1, next_POS1, _ = sentence[word_idx+1]
        next_word2, next_POS2, _ = sentence[word_idx+2]
        features.extend([
            'next_word1.lower=' + next_word1.lower(),
            'next_word1.isdigit=%s' % next_word1.isdigit(),
            'next_word1.POS=' + next_POS1,
            'next_word2.lower=' + next_word2.lower(),
            'next_word2.isdigit=%s' % next_word2.isdigit(),
            'next_word2.POS=' + next_POS2,
 
        ])
    else:
        features.extend(['eos', 'eos', 'eos'])

    return features


def get_sent_to_crf_features_POS(sent):
    return [get_word_to_crf_features_POS(sent, i) for i in range(len(sent))]

def sent2labels_POS(sent):
    return [label for _, _, label in sent]

def sent2tokens_POS(sent):
    return [token for token, _, _ in sent]


