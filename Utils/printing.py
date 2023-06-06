from rich import print
from rich.text import Text
from Utils.labels import *

# -*- coding: utf-8 -*-
"""
These file contains visualizations functions to be used if we want to print the texts along with the annotations in a colorful manner
"""

formatted_dict = {"NEG": "white on yellow", 
                  "NSCO": "white on green", 
                  "UNC": "white on blue", 
                  "USCO": "white on purple"}

def print_legend():
    # Find the maximum length of the keys in the formatted_dict
    max_key_length = max(len(key) for key in formatted_dict.keys())
    rich_text = Text()

    for key, value in formatted_dict.items():

        # Left-align the key to match the maximum length
        formatted_key = key.ljust(max_key_length)
        # Append the key in bold style
        rich_text.append(f"{formatted_key}: ", style="bold")
        # Append the value with the corresponding style
        rich_text.append(f"{value}\n", style=value)
    
    print(rich_text)


def subrayar_palabras(Dataframe, row, legend=True):
    rich_text = Text()
    posicion_actual = 0
    texto = Dataframe["data"][row]["text"]

    if legend:
        print_legend()
    
    for labels in start_end_label(Dataframe, row):
        inicio, final = labels[0], labels[1]
        rich_text.append(texto[posicion_actual:inicio])

        # Append the labeled text with the corresponding style from formatted_dict
        rich_text.append(texto[inicio:final], style=formatted_dict[labels[2]])
        posicion_actual = final
    
    # Append the remaining text after the last labeled segment
    rich_text.append(texto[posicion_actual:])
    return rich_text
