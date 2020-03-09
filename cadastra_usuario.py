import os, json, sys

def adiciona_nome():
    nome = input('\nNome do usuario: ')
    idade = int(input(f'Idade do usuario { nome }: '))
    global list
    try:
        list.update({ nome : idade })
        print(json.dumps(list, indent=2, sort_keys=True))
    except AttributeError:
        list = { nome : idade }
        print(json.dumps(list, indent=2, sort_keys=True))

def remove_usuario():
    nome = input('\nUsuario a ser removido: ')
    try:
        del list[nome]
        print(json.dumps(list, indent=2, sort_keys=True))
        print('Usuario removido com sucesso.')
    except KeyError:
        print('Nome nao encontrado.')

def main():
    adiciona_nome()
    print('\n> Usuario cadastrado.\n')
    while True:
        print("\n=== Menu ===")
        outro = input('[a]dicionar usuario\n[r]emover usuario\n[S]air\n\nOpcao: ')
        if outro == "a":
            adiciona_nome()
            print('Usuario cadastrado.')
        if outro == "r":
            remove_usuario()
        if outro == "S":
            print('OK, bye.')
            break

if __name__ == '__main__':
    main()
