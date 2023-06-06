from Utils.extract_words import get_nextWord

def identify_scope(text, End_sentence, End_word, negations_cues, uncertainty_cues):

    sentences_of_text = []  #List that will contain all the (word, tag) tuples
    sentence = []           #List that we will use to store the sentences we will find while traversing the text

    #Boolean variables to control the negations and unvertainties found in a given sentence
    negation_found    = False 
    uncertainti_found = False

    all_words = list(get_nextWord(text, End_word))    #Obtantion of all the words in the text
    for _, token in all_words:  
        tag = (token, "other")  #Start assuming that the class of the token is other, then changed it depending if it is in the list of negations or uncertanties

        if token in negations_cues:
            negation_found    = True
            tag = (token, "NEG")

        elif token in uncertainty_cues:
            uncertainti_found = True
            tag = (token, "UNC")

        sentence.append(tag)  #Add the word with the tag to the sentence list

        if any(char in token for char in End_sentence):  #Look if any char in the token contains an end of sentence character.  For example ("afebril,", "paciente.", "enfermero!" 

            if (negation_found):  #If we have found a negation in the sentece, conver to the other tags to NSCO tags
              sentence = [(tag[0], "NSCO") if tag[1] == 'other' else tag for tag in sentence]

            elif (uncertainti_found): #The same here, if we have found a uncertainti convert all the other tags to USCO tags
              sentence = [(tag[0], "USCO") if tag[1] == 'other' else tag for tag in sentence]

            sentences_of_text.extend(sentence)  #Add all the words with their tags to the list sentences_of_text

            #Reset all the variables used at each iteration
            sentence          = []  
            negation_found    = False
            uncertainti_found = False

    return sentences_of_text

import string