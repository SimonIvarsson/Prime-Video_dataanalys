import PySimpleGUI as sg

# GUI Layout
layout = [
    [sg.Text('Användardata över Amazon Prime Video användare.\nSkapad av Simon Ivarsson.')],
    [sg.Button('Information', expand_x = True)], 
    [sg.Button('Tabeller', expand_x = True)], 
    [sg.Button('Grafer', expand_x = True)],
    [sg.Image('Small-img2.png')]
]

# Öppnar GUI
window = sg.Window('Prime Video Användardata', layout)


while True:
    event, values = window.read()

    # Om användaren trycker om close stängs GUI ner
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    
    if event == 'Information':
        window.close()

        layout = [
            [sg.Text('Infomation om datan och systemet.')],
            [sg.Text('Detta system är skapat av Simon Ivarsson med uppgiften att hantera data. Detta system bygger på en GUI som grafiskt visar datan.\nDatan som används är fiktiv. Det är påhittad data över 2500 Amazon Prime Video användare.\nDatan innehåller bland annat emailadresser, plats, kön och mycket mer.')]
        ]

        window = sg.Window('Information', layout)

        while True:
            event, values = window.read()
        if event == sg.WIN_CLOSED:
            break


window.close()