tabuleiro = [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' '],
]
jogador = 'X'

print ("Vamos jogar um belo jogo da velha? ")
def exibir_tabuleiro():
  for linha in tabuleiro:
    print("|".join(linha))
    print("-" * 5)
    
def jogada (linha, coluna):
    if (
      not 0 <= linha or 
      not 0 <= coluna <=2 or 
      tabuleiro[linha][coluna] !=  ' '):
      print ("jogada inválida")
      #Não faça linhas grandes 
      return jogador
    tabuleiro[linha][coluna] = jogador
    return "O" if jogador == "X" else "X"
def temGanhador():
  """Verifica as linhas"""
  for linha in range(3):
      if (
          tabuleiro[linha][0] != ' ' and 
          tabuleiro[linha][0] == tabuleiro[linha][1] and
          tabuleiro[linha][0] == tabuleiro[linha][2]
      ):
          print (f'{tabuleiro[linha][0]} Ganhou!!!')
          return True
  """Verifica as linhas"""
  for linha in range(3):
      if (
          tabuleiro[0][coluna] != ' ' and 
          tabuleiro[0][coluna] == tabuleiro[1][coluna] and
          tabuleiro[0][coluna] == tabuleiro[2][coluna]
      ):
          print (f'{tabuleiro[0][coluna]} Ganhou!!!')
          return True
      #Verificar as diagonais
      if (
          tabuleiro [1][1] != " " and
          (
            (tabuleiro [0][0] == tabuleiro[1][1] and
            tabuleiro [0][0]== tabuleiro [2][2]
            ) or
            (tabuleiro [0][2] == tabuleiro[1][1] and
            tabuleiro [1][1]== tabuleiro [2][0]
            )
          )
      ):
          print (f"{tabuleiro[1][1]} GANHOU !!!")
          return True
        
    #Se não tiver ganhador de nenhuma forma
def temEmpate():
  for linha in range(3):
    for coluna in range(3):
      if tabuleiro[linha][coluna]==" ":
        return False
  print ("Acabou empatado!")
  return True 
 
while True:
    print (f"Jogador da vez: {jogador}")
    try:
      linha = int(input('Digite a linha: '))
      coluna = int(input('Digite a coluna: '))
      jogador = jogada(linha, coluna)
    except (ValueError, IndexError):
      print ("Digite valores numéricos entre 0 e 2")
    exibir_tabuleiro()
    if temGanhador() or temEmpate():
      break
  
  