import PySimpleGUI as sg      

sg.theme("LightBlue1")

layout = [[sg.Text("PySimpleGUI Example")], [sg.InputText()], [sg.Submit(), sg.Cancel()]]

window = sg.Window("Window Title", layout)    

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Quit": break
    
    text_input = values[0]
    sg.popup("You entered", text_input)

window.close()