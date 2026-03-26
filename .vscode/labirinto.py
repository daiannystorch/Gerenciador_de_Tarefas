import random
def criar_labirinto(tamanho):
  labirinto =[ [ random.randint(0, 1) for _ in range (tamanho)] for _ in range (tamanho)]
  labirinto [0][0] = 8
  labirinto [tamanho - 1][tamanho - 1] = 9
  return labirinto

def exibir_labirinto(labirinto):
  for linha in labirinto:
    print(linha)

def nao_pode_seguir(labirinto, linha, coluna):
  if (linha >= len(labirinto) or
     coluna >=len (labirinto) or
     linha < 0 or
     coluna < 0 or
     labirinto[linha][coluna] == 1 or
     labirinto[linha][coluna] == 2):
     return True 


def explorar (labirinto, linha, coluna):
  print(f"Explorando ({linha}, {coluna})")
  if nao_pode_seguir(labirinto, linha, coluna):
      print (f"Não pode seguir ({linha}, {coluna})")
      return False
  if labirinto[linha][coluna] == 9:
      print ("Chegou ao final")
      return True
  if linha > 0: 
      explorar(labirinto, linha - 1, coluna)
  
  labirinto[linha][coluna] = 2
  
  return (explorar(labirinto, linha + 1, coluna) or # direitbaixo
      explorar(labirinto, linha - 1, coluna) or # cima
      explorar(labirinto, linha, coluna + 1) or # direita
      explorar(labirinto, linha, coluna - 1))     # esquerda
      
  return False
  
lab = criar_labirinto(5)
exibir_labirinto(lab)

explorar(lab, 0, 0)