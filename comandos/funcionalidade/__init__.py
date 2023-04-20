def criar_arquivo(tamanho):
  try:
    file = open(f'comandos/funcionalidade/banco_de_palavras/tamanho_{tamanho}.txt', 'x')
    file.close()
    return 'Arquivo criado!'
    
  except FileExistsError:
    return 'Arquivo já existente!'


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def verifica_palavra(palavra, tamanho, jogo=False):
  lines = []
  with open(f'comandos/funcionalidade/banco_de_palavras/tamanho_{tamanho}.txt', 'r') as txt_file:
    lines = txt_file.readlines()
  
  for line in lines:
    if palavra in lines:
      if jogo:
        return lines.index(palavra)
      else:
        return True
      break

    elif (palavra+'\n') in lines:
      if jogo:
        return lines.index(palavra)
      else:
        return True
      break

    else:
      return False


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def adicionar_palavras():
  while True:
    nova_palavra = str(input('Digite a palavra para ser adicionada: ')).lower().strip()
    
    tamanho = len(nova_palavra)

    criar_arquivo(tamanho)
    
    if not verifica_palavra(nova_palavra, tamanho):
      try:
        txt_file = open(f'comandos/funcionalidade/banco_de_palavras/tamanho_{tamanho}.txt', 'a')
        txt_file.write(nova_palavra+'\n')
        print('[OK]: Palavra adicionada com sucesso!!')
          
      finally:
        txt_file.close()

    else:
      print('[ERROR]: palavra já adicionada anteriormente!')
    
    print(20 * '-=')

    while True:
      continuar = str(input('Deseja continuar? [S/N] ')).lower().split()[0]
     
      if continuar == 'n' or continuar == 's':
        break
      
      else:
        print('[ERROR]: Por favor, Digite novamente!!')

    if continuar == 'n':
      break

    print(20 * '-=')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#                                JOGO
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def cores(estilo, texto, fundo=0):
  return f'\033[{estilo};{texto};{fundo}m'


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def jogo(dificuldade):
  import random
  lines = []
  with open(f'comandos/funcionalidade/banco_de_palavras/tamanho_{dificuldade}.txt', 'r') as file:
    lines = file.readlines()

  palavra = random.choice(lines)
  indice = verifica_palavra(palavra, dificuldade, True)
  print(palavra, indice)
  
  
  for chances in range(0, dificuldade):
    usuario = str(input('Chute: ')).lower().strip()[:dificuldade]
    acertou = 0

    
    for i in range(0, dificuldade):
      if i == 0:
        print(cores(0, 0, 0) + '|', end='')


      """
      # Letras com acento
      # Letra A:
      if palavra[i] in 'aáàâã':
        palavra.replace(palavra[i],  'a')

      # Letra E:
      elif palavra[i] in 'eéèê':
        acento = True

      # Letra I:
      elif palavra[i] in 'iíìî':
        palavra.replace(palavra[i], 'i')
        
      # Letra O:
      elif palavra[i] in 'oóòôõ':
        palavra.replace(palavra[i], 'o')
      
      #Letra U:
      elif palavra[i] in 'uúùû':
        palavra.replace(palavra[i], 'u')
      """
      
      # Certo
      if usuario[i] == palavra[i] and usuario[i] in palavra:
        print(cores(1, 0, 42) + usuario[i], end='')
        acertou += 1
        if acertou == dificuldade:
          break
      
      # Quase certo
      elif usuario[i] in palavra:
        print(cores(1, 0, 43) + usuario[i], end='')
        
      # Errado
      else:
        print(cores(1, 0, 41) + usuario[i], end='')

    if i == (dificuldade-1):
      print(cores(0, 0, 0) + '|')
 
    if acertou == dificuldade:
      break
      
  if acertou == dificuldade:
    print('Parabéns, Você acertou!!!')
  
  else:
    print('Que pena, Não foi dessa vez!')