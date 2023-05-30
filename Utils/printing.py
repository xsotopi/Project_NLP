from rich import print
from rich.text import Text
from labels import *

formatted_dict = {"NEG": "white on yellow", 
                  "NSCO": "white on green", 
                  "UNC": "white on blue", 
                  "USCO":"white on purple"}


def print_legend(): 
  max_key_length = max(len(key) for key in formatted_dict.keys())
  rich_text = Text()

  for key, value in formatted_dict.items():
      formatted_key = key.ljust(max_key_length)
      rich_text.append(f"{formatted_key}: ", style="bold")
      rich_text.append(f"{value}\n", style=value)
  print(rich_text)


def subrayar_palabras(Dataframe, row, legend = True):
    
    rich_text = Text()
    posicion_actual = 0
    texto = Dataframe["data"][row]["text"]

    if (legend):
      print_legend()
    for labels in start_end_label(Dataframe, row):
      inicio, final = labels[0], labels[1]
      rich_text.append(texto[posicion_actual:inicio])
      rich_text.append(texto[inicio:final], style = formatted_dict[labels[2]])
      posicion_actual = final
    rich_text.append(texto[posicion_actual:])
    return rich_text

formatted_dict = {"NEG": "white on yellow", 
                  "NSCO": "white on green", 
                  "UNC": "white on blue", 
                  "USCO":"white on purple"}
