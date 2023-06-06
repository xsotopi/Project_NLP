from Utils.labels import start_end_label
import nltk

def get_nextWord(text, End_word):
    """""
    Function that returns the next word, and the postion of the word in a given text each time it's called.
    text: A text where we need to exctract the words
    End_Word: Characters that specifiy what is consider the end of a word. Ex (!.,)
    """""
    i = 0
    word = ""              
    start = True
    while i < len(text):    #Iterate the text character by character
        if (i < len(text)) and (text[i] != ' ') and (text[i] not in End_word):  #If the character is either a space or and end of a word 
            if start:       
                pos = i         #Store the position of the firts character of the word
                start = False
            word += text[i]     #Store the characters contained in the word
        elif word != '':        #If the variable word is not empty
            yield (pos, word)   #Return the start position and the word
            word = ''           
            start = True       
        i += 1     
    yield (pos, word)           #These line is executed for the last word in the text


def label_text(df, number_row, End_word):
    """""
    df: Pandas dataframe
    number_row: Row containing the text we need to look into
    End_Word: Characters that specifiy what is consider the end of a word. Ex (!.,)
    """""
    text   = df["data"][number_row]["text"]     
    labels = sorted(start_end_label(df, number_row), key = lambda x: x[0])  #Calls star_end_label and sorts the result in order to have the annotations of a given text in order.

    if len(labels) == 0:    #If there are not annotations return
        return []
    pos = 0
    words_count = 0

    text_annotations = []
    
    all_words = list(get_nextWord(text, End_word))  #Obtention of all the words in the text separeted by the given punctuations in the variable End_word
    for index, word in all_words:   #Iterate for all the words
        if pos < len(labels):   
            start, end, text, num_words, label = labels[pos]    #Obtantion of tag information
        if ((index >= start) and (index <= end)): 
            words_count += 1                           #contador keeps track of the number of words seen between the range start and end
            text_annotations.append((word, label)) 
        else:
            text_annotations.append((word, 'other'))   
        if words_count == num_words:    
            pos += 1
            words_count = 0
    return text_annotations


def label_text_POS(df, number_row, End_word):
    """
    Function with the same behaviour as the label_text function but adds the POS tagging too, along with the tag for each of the words in the text.
    """
    text   = df["data"][number_row]["text"]
    labels = sorted(start_end_label(df, number_row), key=lambda x: x[0])

    if len(labels) == 0:
        return []
    pos = 0
    contador = 0

    text_annotations = []

    all_words = list(get_nextWord(text, End_word))
    all_words_pos = nltk.pos_tag([word for _, word in all_words])  # POS tagging

    for (index, word), (_, POS) in zip(all_words, all_words_pos):
        index = int(index)  # Convert index to integer
        if pos < len(labels):
            start, end, text, num_words, label = labels[pos]
            if (index >= start) and (index <= end):
                contador += 1
                text_annotations.append((word, POS, label))  # Include POS in the annotation
            else:
                text_annotations.append((word, POS, 'other'))
            if contador == num_words:
                pos += 1
                contador = 0
        else:
            text_annotations.append((word, POS, 'other'))

    return text_annotations
