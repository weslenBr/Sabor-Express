import os

restaurantes = [{'nome' : 'Praça', 'categoria': 'Japonesa', 'ativo': False }, 
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True },
                {'nome' : 'Cantina', 'categoria': 'Italiano', 'ativo': False }]

def exibir_nome_do_programa():
    '''Essa funçao é responsavel por exibir o nome do app'''
    print('🅢🅐🅑🅞🅡 🅔🅧🅟🅡🅔🅢🅢\n')

def exibir_opcoes():
    '''Essa função mostra as opçoes do app'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair')



    # funçao no python
def finalizar_app():
   ''' Essa funçao finaliza o app'''
   exibir_subtitulo('Finalizando app')

def voltar_ao_menu_principal():
    '''Essa funaçao volta ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''Essa funaçao mostra se a opçao é invalida'''
    print('Opção Invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Essa funaçao mostra o subtitulo'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    

def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante
    Inputs:
    -Nome do restaurante
    -Categoria
    Outputs:
    -Adiciona um novo restaurante a lista de restaurantes.
    
    
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:  \n')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    
    voltar_ao_menu_principal()

def listar_restarantes():
    ''' Essa funçao lista os restaurantes'''
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def  alternar_estado_restaurante():
    ''' Essa função alterna o estado do restaurante'''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso'if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado')
        
    voltar_ao_menu_principal()


def escolher_opcao():
    '''Essa funçao esolhe uma opçao a ser realizada '''
    try:
        opcao_escolhida =  int (input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restarantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:opcao_invalida()

def main():
        os.system('cls')
        exibir_nome_do_programa()
        exibir_opcoes()
        escolher_opcao()

if __name__ == '__main__':
    main()