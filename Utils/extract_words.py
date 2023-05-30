from Utils.labels import start_end_label

def get_nextWord(text, punctuations):
    i = 0
    word = ""
    start = True
    while i < len(text):
        if (i < len(text)) and (text[i] != ' ') and (text[i] not in punctuations):
            if start:
                pos = i
                start = False
            word += text[i]
        elif word != '':
            yield (pos, word)
            word = ""
            start = True
        i += 1
    yield (pos, word)


def label_text(df, number_row, punctuations):
    text   = df["data"][number_row]["text"]
    labels = sorted(start_end_label(df, number_row), key = lambda x: x[0])

    if len(labels) == 0:
        return []
    pos = 0
    contador = 0

    text_annotations = []
    
    all_words = list(get_nextWord(text, punctuations))
    for index, word in all_words:
        if pos < len(labels):
            start, end, text, num_words, label = labels[pos]
        if ((index >= start) and (index <= end)):
            contador += 1
            text_annotations.append((word, label))
        else:
            text_annotations.append((word, 'other'))   
        if contador == num_words:
            pos += 1
            contador = 0
    return text_annotations
