import pandas as pd

def start_end_label(Dataframe, number_row): 
    """
    Function that returns in a list of tuples, the start, end, text, number of words in the tag and the tag itself.
    """
    data = Dataframe["predictions"][number_row][0]["result"]          #Data containing the prediction of that row
    text = Dataframe["data"][number_row]["text"]                      #Text related to the text of a specifc row
    return [(entry["value"]["start"],                                 
             entry["value"]["end"],
             text[entry["value"]["start"]:entry["value"]["end"]],
             len(text[entry["value"]["start"]:entry["value"]["end"]].rstrip().split()),
             entry["value"]["labels"][0]) for entry in data]

def get_label_in_text(Dataframe, number_row, Show=False):
    """
    Returns a dataframe, containing information of the tags of a given text.
    """
    Predictions = start_end_label(Dataframe, number_row)
    text = Dataframe["data"][number_row]["text"]

    if Show:
        print("{} {} {}".format("Text", "~~~" * 15, "Label"), end='/n')
        for pred in Predictions:
            print("{:<50} {}".format(text[pred[0]:pred[1]], pred[2]), end='/n')

    Text_and_Labels = pd.DataFrame([(number_row, pred[2], pred[0], pred[1], pred[4]) for pred in Predictions], columns=['File', 'Text','Start', 'End', 'Label'])

    return Text_and_Labels
