import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# GUI Layout
sg.set_options(font= 'Consolas 14')
layout = [
    [sg.Text('Användardata över Amazon Prime Video användare.\nSkapad av Simon Ivarsson.')],
    [sg.Button('Information', expand_x = True)], 
    [sg.Button('Dataframes', expand_x = True)], 
    [sg.Button('Diagram', expand_x = True)],
    [sg.Image('tests.png')]
]

# Öppnar GUI
window = sg.Window('Prime Video Användardata', layout)


while True:
    event, values  = window.read()

    # Om användaren trycker om close stängs GUI ner
    if event == sg.WIN_CLOSED:
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
        df.pop('Customer Support Interactions')
        df.pop('Feedback/Ratings')
        df.pop('Engagement Metrics')
        df.pop('Devices Used')
        df.pop('Favorite Genres')
        df.pop('Purchase History')
        df.pop('Usage Frequency')
        df.pop('Renewal Status')
        df.pop('Payment Information')
        df.pop('Subscription Plan')
        df.pop('Membership End Date')
        df.pop('Membership Start Date')
        sg.set_options(font= 'Consolas 14')

        layout = [
            [sg.Button('↩',font= 'Consolas 13')],
            [sg.Text('Dataframes')],
            [sg.Text('Datan över våra användare', text_color= "light grey")],
            [sg.Table(values=df.values.tolist(), headings=df.columns.tolist(), display_row_numbers=False, auto_size_columns=True, vertical_scroll_only=True)]
        ]

        window = sg.Window('Dataframes', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

    if event == 'Diagram':
        window.close()

        sg.set_options(font= 'Consolas 14')

        layout = [
            [sg.Button('↩',font= 'Consolas 13')],
            [sg.Text('Visualiserad data.')],
            [sg.Text('Här är datan visualiserad i olika tabeller / diagram.\nTryck på den information du vill se!', text_color= "light grey")],
            [sg.Button('Kön', expand_x= True), sg.Button('Device Usage Patterns', expand_x= True), sg.Button('Favorit genrer', expand_x= True)]
        ]

        window = sg.Window('Diagram', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == 'Kön':
                df = pd.read_csv('amazon_prime_users.csv')
            # Step 2: Create Bar Chart
            def create_bar_chart(Gender):
                plt.figure(figsize=(6, 4))
                df[Gender].value_counts().plot(kind='bar')
                plt.title('Number of Men and Women')
                plt.xlabel('Gender')
                plt.ylabel('Count')

            # Step 3: Integrate with PySimpleGUI
            layout = [
                    [sg.Text('Andel män respektive kvinnor som använder Prime Video:')],
                    [sg.Combo(df.columns, key='-COLUMN-', size=(20, 1))],
                    [sg.Canvas(key='-CANVAS-')],
                    [sg.Button('Plot Chart')]]

            window = sg.Window('Gender Comparison Chart', layout, finalize=True)
            canvas_elem = window['-CANVAS-'].TKCanvas

            while True:
                event, values = window.read()
                if event in (sg.WINDOW_CLOSED, 'Exit'):
                    break
                elif event == 'Plot Chart':
                    Gender = values['-COLUMN-']
                    create_bar_chart(Gender)
                    # Embed Matplotlib plot into PySimpleGUI window
                    figure_canvas_agg = FigureCanvasTkAgg(plt.gcf(), master=canvas_elem)
                    figure_canvas_agg.draw()
                    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)


window.close()