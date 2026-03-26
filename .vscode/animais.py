perguntas = [["O seu animal gosta de bananas?", "macaco"]]

while True:
  print ("Pense em um animal...")
  acertou = False
  for pergunta in perguntas:
    resposta = input(f"{pergunta[0]}(s/n):")
    if resposta.lower() == "s":
      print (f"O animal é {pergunta[1]}!") 
      acertou = True
      break

  if not acertou:
    animal = input("Desisto, em qual animal você pensou? ")
    novaPergunta = input ("Qual pergunta eu poderia ter feito para acertar o animal? ")
    perguntas.append([novaPergunta, animal])
    
    resposta = input ("Quer jogar novamente? (s/n): ")
  if resposta.lower() != "s":
      print ("Obrigado por jogar!")
      break
