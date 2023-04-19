def criar_arquivo(tamanho):
  try:
    file = open(f'comandos/funcionalidade/banco_de_palavras/tamanho_{tamanho}.txt', 'x')
    file.close()
    return 'Arquivo criado!'
    
  except FileExistsError:
    return 'Arquivo já existente!'


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def verifica_palavra(palavra, tamanho):
  lines = []
  with open(f'comandos/funcionalidade/banco_de_palavras/tamanho_{tamanho}.txt', 'r') as txt_file:
    lines = txt_file.readlines()

  for line in lines:
    if line == lines[-1]:
      if palavra in lines:
        return True
        break

      else:
        return False
        break

    else:
      if (palavra+'\n') in lines:
        return True
        break

      else:
        return False
        break


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def adicionar_palavras():
  while True:
    nova_palavra = str(input('Digite a palavra para ser adicionada: ')).lower().strip()
    
    tamanho = len(nova_palavra)

    criar_arquivo(tamanho)
    
    if not verifica_palavra(nova_palavra, tamanho):
      try:
        txt_file = open(f'comandos/funcionalidade/banco_de_palavras/tamanho_{tamanho}.txt', 'a')
        txt_file.write(nova_palavra+'\n')
          
      finally:
        txt_file.close()

    else:
      print('ERROR: palavra já adicionada anteriormente!')
    


    while True:
      continuar = str(input('Deseja continuar? [S/N] ')).lower().split()[0]
     
      if continuar == 'n' or continuar == 's':
        break
      
      else:
        print('[ERROR]: Por favor, Digite novamente!!')

    if continuar == 'n':
      break
    

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-




