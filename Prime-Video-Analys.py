import PySimpleGUI as sg

sg.Theme = 'Reddit'

# GUI Layout
layout = [
    [sg.Text('Användardata över Amazon Prime Video användare')],
    [sg.Button('Information', expand_x = True), sg.Button('Grafer', expand_x = True), sg.Button('Tabeller', expand_x = True)],
    [sg.Image('Small-img.png', expand_x = True)]
]

# Öppnar GUI
window = sg.Window('Prime Video Användardata', layout)


while True:
    event, values = window.read()

    # Om användaren trycker om close stängs GUI ner
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

window.close()