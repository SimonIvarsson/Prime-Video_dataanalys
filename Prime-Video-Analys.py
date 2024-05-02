import PySimpleGUI as sg
import numpy as np
import matplotlib as plt
import pandas as pd

# GUI Layout
sg.set_options(font= 'Consolas 14')
layout = [
    [sg.Text('Användardata över Amazon Prime Video användare.\nSkapad av Simon Ivarsson.')],
    [sg.Button('Information', expand_x = True)], 
    [sg.Button('Dataframes', expand_x = True)], 
    [sg.Button('Grafer', expand_x = True)],
    [sg.Image('Small-img2.png')]
]

# Öppnar GUI
window = sg.Window('Prime Video Användardata', layout)


while True:
    event, values  = window.read()

    # Om användaren trycker om close stängs GUI ner
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    
    if event == 'Information':
        window.close()

        sg.set_options(font= 'Consolas 14')

        layout = [
            [sg.Button('↩',font= 'Consolas 13')],
            [sg.Text('Infomation om datan och systemet.')],
            [sg.Text('Detta system är skapat av Simon Ivarsson med uppgiften att hantera data.\nSystemet bygger på en GUI som grafiskt visar datan.\nDatan som används är fiktiv.\nDet är påhittad data över 2500 Amazon Prime Video användare.\nDatan innehåller bland annat emailadresser, plats, kön och mycket mer.', text_color= "light grey")]
        ]

        window = sg.Window('Information', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
    
    if event == 'Dataframes':
        window.close()
        
        pd.options.display.max_rows = 20
        pd.options.display.max_columns = 6
        df = pd.read_csv("amazon_prime_users.csv")

        sg.set_options(font= 'Consolas 14')

        layout = [
            [sg.Button('↩',font= 'Consolas 13')],
            [sg.Text('Dataframes')],
            [sg.Text('Datan över våra användare', text_color= "light grey")],
            [sg.Table(values=df.values.tolist(), headings=df.columns.tolist(), display_row_numbers=True, auto_size_columns=False, col_widths=[20, 10], vertical_scroll_only=True)]
        ]

        window = sg.Window('Dataframes', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break


window.close()