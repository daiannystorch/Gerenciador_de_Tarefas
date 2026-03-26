# f(x) = y
# f(x) = 2x
# f(2) = 4
# f(x) = 10
# def é o que define uma função
# def nome_da_funcao(parametros): sempre tem abre e fecha parenteses
def olaMundo():
    print("Olá, Mundo")

def olaPessoa (nome):
    print(f"Olá, {nome}!")

def dobro (numero):
    return numero * 2
print (dobro (5) + 2)
# quando eu tenho ** é o exponencial, ou seja, 2 elevado a 2 é igual a 4. 
""" Esquema de documentação em string com 3 aspas"""

def multiplicaDoisNumeros( a, b = 2**2):
    return a * b
print (multiplicaDoisNumeros(3,))

x = 5 #variável global, ou seja, pode ser acessada em qualquer parte do código
def soma ():
  x = 10 #se não tiver nada marcado, ela pega uma de fora, aqui dentro se tiver é uma variável local, ou seja, só pode ser acessada dentro da função 
  print(x)
  return x + 1  
soma ()
print(x)  