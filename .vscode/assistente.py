print ("Olá, eu sou sua assistente Pytrina, o que quer fazer hoje?")

comando = input("Digite o comando: ")
match comando:
    case "1" | "0": 
        print ("Voce escolheu a opção 1")
    case "2":
        print ("Voce escolheu a opção 2")
    case "3":
        print ("Voce escolheu a opção 3")
    case _:
        print ("Comando inválido")