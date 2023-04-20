from comandos.interface import janela_menu, janela_dificuldade
import PySimpleGUI as sg

# Janela_Menu:
janela_menu = janela_menu()

while True:
    event, values = janela_menu.read()

    if event == sg.WIN_CLOSED or event == 'Sair':
      break

    elif event == 'Dificuldade':
      janela_dificuldade = janela_dificuldade()

      while True:
        event, values = janela_dificuldade.read()

        if event == sg.WIN_CLOSED or event == 'Voltar':
          break    

janela_menu.close()

