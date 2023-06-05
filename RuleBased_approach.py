import pandas as pd
import string

import random
from sklearn.model_selection import train_test_split
from Models.Alg_rulebased import *

from Utils.labels import *
from Utils.extract_words import *
from Utils.evaluation import *
import nltk
from Models.Features_witouht_POS import sent2labels, sent2tokens

df = pd.read_json("Data.json")

def NEG_UNC_texts():
    with open('./Triggers_Cues/uncertainty.txt', 'r') as file:
        uncertainty_cues = [line.strip() for line in file]

    with open('./Triggers_Cues/negations.txt', 'r') as file:
        negations_cues = [line.strip() for line in file]

    return negations_cues, uncertainty_cues

def end_word_obtantion():
    End_sentence   = '!.?,;:'   #These are possible punctuations that can appear in the words return by get_nextWord
    Difference     = set(string.punctuation) - set(End_sentence)
    End_word = ''             #What we consider as a delimeter for defining what is a word
    for char in Difference:
        End_word += char
    
    return End_sentence, End_word

def padded_sentences(y_pred, y_true):
    y_pred_ext = []
    y_true_ext = []
    for pred, true in zip(y_pred, y_true):
        len_diff = len(true) - len(pred)
        if len_diff > 0:
            pred.extend([(' ', 'other')] * len_diff)
        if len_diff < 0:
            true.extend([(' ', 'other')] * (abs(len_diff)))
        y_pred_ext.append(pred)
        y_true_ext.append(true)
    
    return y_pred_ext, y_true_ext


if __name__ == "__main__":
    negations_cues, uncertainty_cues = NEG_UNC_texts()
    End_sentence, End_word = end_word_obtantion()

    X_train, X_test, y_train, y_test = train_test_split(range(len(df)), range(len(df)), test_size=0.3, random_state=42)

    y_pred = [identify_scope(df["data"][i]["text"], End_sentence, End_word) for i in y_train]
    y_true = [label_text(df, i, End_word) for i in y_train]

    y_true_ext, y_pred_ext = padded_sentences(y_pred, y_true)

    y_true_labels = [sent2labels(sent) for sent in y_true_ext]
    y_pred_labels = [sent2labels(sent) for sent in y_pred_ext]



    print(bio_classification_report(y_true_labels, y_pred_labels))
