# File containing the features without considering the Pos taggin information

import re

def get_word_to_crf_features(sentence, word_idx):
    word, _ = sentence[word_idx]

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
        'word.suffix_3=' + word[-3:]
    ]

    if word_idx > 0:
        prev_word, _ = sentence[word_idx-1]
        features.extend([
            'prev_word.lower=' + prev_word.lower(),
            'prev_word.isdigit=%s' % prev_word.isdigit(),
            'prev_word.prefix_2=' + prev_word[:2],
            'prev_word.prefix_3=' + prev_word[:3],
            'prev_word.suffix_2=' + prev_word[-2:],
            'prev_word.suffix_3=' + prev_word[-3:]
        ])
    else:
        features.append('bos')

    if word_idx < len(sentence) - 1:
        next_word, _ = sentence[word_idx+1]
        features.extend([
            'next_word.lower=' + next_word.lower(),
            'next_word.isdigit=%s' % next_word.isdigit(),
            'next_word.prefix_2=' + next_word[:2],
            'next_word.prefix_3=' + next_word[:3],
            'next_word.suffix_2=' + next_word[-2:],
            'next_word.suffix_3=' + next_word[-3:]
            
        ])
    else:
        features.append('eos')

    return features

def get_sent_to_crf_features(sent):
    return [get_word_to_crf_features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [label for _, label in sent]

def sent2tokens(sent):
    return [token for token, _, in sent]
