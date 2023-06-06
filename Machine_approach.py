import string
import pandas as pd
from sklearn.model_selection import train_test_split
import pycrfsuite as crfs


from Models.CRF_with_POS import *
from Models.CRF_without_POS import *

from Utils.extract_words import label_text_POS, label_text
from Utils.evaluation import bio_classification_report

def Taggin_Files(Data_json, POS = True):
    if POS:
        tagged_files = [[(word, POS, label) for word, POS, label in label_text_POS(Data_json, i, string.punctuation)] 
                        for i in range(len(Data_json))]
    else:
        tagged_files = [[(word, label) for word, label in label_text(Data_json, i, string.punctuation)] 
                        for i in range(len(Data_json))]

    return tagged_files


def CRF_creation(X_train, y_train):
    trainer_crf = crfs.Trainer(verbose=False) # Instance a CRF trainer

    for xseq, yseq in zip(X_train, y_train):
        trainer_crf.append(xseq, yseq) # Stack the data
    
    trainer_crf.set_params({
    'c1': 1.0,   # coefficient for L1 penalty
    'c2': 1e-3,  # coefficient for L2 penalty
    'max_iterations': 100,

    # include transitions that are possible, but not observed
    'feature.possible_transitions': True
    })

    return trainer_crf

def Train_Test_Sets(Data, POS = True):
    train_sents, test_sents = train_test_split(Data, test_size=0.2, random_state=42)

    if POS:

        X_train = [get_sent_to_crf_features_POS(s) for s in train_sents]
        y_train = [sent2labels_POS(s) for s in train_sents]

        X_test = [get_sent_to_crf_features_POS(s) for s in test_sents]
        y_test = [sent2labels_POS(s) for s in test_sents]
    else:

        X_train = [get_sent_to_crf_features(s) for s in train_sents]
        y_train = [sent2labels(s) for s in train_sents]

        X_test = [get_sent_to_crf_features(s) for s in test_sents]
        y_test = [sent2labels(s) for s in test_sents]
    
    return X_train, y_train, X_test, y_test



path_json = '/Users/nbiescas/Desktop/Project_NLP/Data.json'

if __name__ == "__main__":
    POS = True
    Data_json    = pd.read_json(path_json)          
    Files_tagged = Taggin_Files(Data_json, POS=POS)

    X_train, y_train, X_test, y_test = Train_Test_Sets(Files_tagged, POS)

    trainer_crf = CRF_creation(X_train, y_train)

    trainer_crf.train('nlp_NEG_UNC_crf-improved.crfsuite') # Train the model and save it locally.
    tagger_crf = crfs.Tagger()
    tagger_crf.open('/Users/nbiescas/Desktop/Project_NLP/nlp_NEG_UNC_crf-improved.crfsuite') # Load the inference API

    y_pred_crf = [tagger_crf.tag(xseq) for xseq in X_test]
    CRF = bio_classification_report(y_test, y_pred_crf)         
    print('CRF')
    print(CRF)