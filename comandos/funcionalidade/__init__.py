def adicionar_palavras():
  from time import sleep
  while True:
    nova_palavra = str(input('Digite a palavra para ser adicionada: ')).upper().strip()


    for palavra in txt_file:
      txt_file = open('comandos/funcionalidade/banco_de_palavras.txt', 'r')
      if nova_palavra == palavra:
        print('[REPETIDO]: Essa palavra já estava adicionada!')
          
      else:      
        txt_file = open('comandos/funcionalidade/banco_de_palavras.txt', 'a')
        try:
          txt_file.write('\n' + nova_palavra)
          
        finally:
          txt_file.close()
    

    while True:
      continuar = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
     
      if continuar == 'N' or continuar == 'S':
        break
      
      else:
        print('[ERROR]: Por favor, Digite novamente!!')

    if continuar == 'N':
      break
    

