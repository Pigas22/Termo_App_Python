import PySimpleGUI as sg      


def janela_menu():
  # Tema:
  sg.theme('LightBlue1')
  
  # Layout Menu: 
  menu = [
    [sg.Text('TERMO APP - Python')], 
    [sg.Button('Iniciar')], 
    [sg.Button('Dificuldade')],
    [sg.Cancel('Sair')]
  ]

  return sg.Window('Termo App v1', layout=menu, finalize=True )
  

def janela_dificuldade():
  
  # Tema:
  sg.theme('LightBlue1')

  # Layout Dificuldade:
  botao = [
    [sg.Button()]
  ]

  dificuldades = [
    [sg.Frame('Dificuldades:', layout=botao, key='container')],
    [sg.Cancel('Voltar')]
  ]

  return sg.Window('Dificuldades', layout=dificuldades, finalize=True)