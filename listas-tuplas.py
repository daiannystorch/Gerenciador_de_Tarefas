import os
tarefas = []

def adicionaTarefa(tarefa):
    novaTarefa = (tarefa, 'pendente')
    tarefas.append(novaTarefa)

def exibeTarefas():
    if not tarefas:
        print("\nA lista está vazia!")
    for t in tarefas:
        print(f'{t[0]} - Status: {t[1]}')

def concluirTarefa(tarefa_nome):
    global tarefas
    novaLista = []
    for t in tarefas:
        if t[0] == tarefa_nome:
            novaLista.append((tarefa_nome, 'concluída'))
        else:
            novaLista.append(t)
    tarefas = novaLista

def removerTarefa(tarefa_nome):
    global tarefas
    tarefas = [t for t in tarefas if t[0] != tarefa_nome]

def buscarTarefa(tarefa_nome):
    resultado = [t for t in tarefas if t[0] == tarefa_nome]
    if resultado:
        for titulo, status in resultado:
            print(f'Encontrada: {titulo} - Status: {status}')
    else:
        print(f'Tarefa não encontrada: {tarefa_nome}')

# O MENU DEVE FICAR FORA DAS FUNÇÕES (ENCCOSTADO NA ESQUERDA)
while True:
    os.system ('clear')
    print('\n--- Gerenciador de Tarefas ---')
    print('1 - Listar Tarefas')
    print('2 - Adicionar Tarefa')
    print('3 - Remover Tarefa')
    print('4 - Concluir Tarefa')
    print('5 - Buscar Tarefa')
    print('0 - Sair')
    
    opcao = int(input('\nDigite uma opção: '))

    match opcao:
        case 1:
            exibeTarefas()
        case 2:
            nome = input('Digite a tarefa desejada: ')
            adicionaTarefa(nome)
        case 3:
            nome = input('Qual tarefa deseja remover? ')
            removerTarefa(nome)
        case 4:
            nome = input('Qual tarefa deseja concluir? ')
            concluirTarefa(nome)
        case 5:
            nome = input('Digite o nome para busca: ')
            buscarTarefa(nome)
        case 0:
            print('Saindo do programa...')
            break
        case _:
            print('Opção inválida!')
    print ()      
    input('Pressione ENTER para continuar...')
        