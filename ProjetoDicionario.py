import json

data = json.load(open("data.json"))


print('Bem vindo(a) ao dicionario mais brabo desse mundo !\n')
confirmar = input('Temos um estoque de significados muito grande\nJa sabe o que gostaria de pesquisar? (s/n)\n ')

while confirmar.lower() == 's':
    palavra = input('\nQual palavra voce gostaria de descobrir o significado?\n ').lower()
    if palavra in data.keys():
        print(f'\n{palavra.title()}: \n\t {data[palavra][0]}')
        continuar = input('\nVoce gostaria de saber o significado de outras palavras? (s/n)\n')
        if continuar.lower() == 'nao' or continuar.lower() == 'n':
            break
    else:
        print('A palavra não existe ')

# abosrber     base load       dustproof