import string
import pandas as pd
import re
from sklearn.model_selection import train_test_split
import pycrfsuite as crfs

#CRF Features
from CRF_Features.Features_POS import get_word_to_crf_features_POS

from Utils.extract_words import *
from Utils.labels import *


def get_sent_to_crf_features(sent):
    return [get_word_to_crf_features_POS(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [label for _, _, label in sent]

def sent2tokens(sent):
    return [token for token, _, _ in sent]



def CRF_creation(X_train, y_train):
    trainer_crf = crfs.Trainer(verbose=False) # Instance a CRF trainer

    for xseq, yseq in zip(X_train, y_train):
        trainer_crf.append(xseq, yseq) # Stack the data

def Train_Test_Sets(Data):
    train_sents, test_sents = train_test_split(Data, test_size=0.2, random_state=42)

    X_train = [get_sent_to_crf_features(s) for s in train_sents]
    y_train = [sent2labels(s) for s in train_sents]

    X_test = [get_sent_to_crf_features(s) for s in test_sents]
    y_test = [sent2labels(s) for s in test_sents]

def Taggin_Files(Data_json, with_POS = True):
    if with_POS:
        tagged_files = [[(word, POS, label) for word, POS, label in label_text(Data_json, i)] 
                        for i in range(len(Data_json))]
    else:
        tagged_files = [[(word, label) for word, label in label_text(Data_json, i, string.punctuation)] 
                        for i in range(len(Data_json))]

    return tagged_files

path_json = r'C:\Users\34644\Desktop\Second Semester\Natural Language\Project_NLP\Data.json'



if __name__ == "__main__":
    Data_json = pd.read_json(path_json)
    Files_tagged = Taggin_Files(Data_json, with_POS=False)
    train_data, test_data = train_test_split(Files_tagged, test_size=0.2, random_state=42)

