import pickle
from pessoa import Player
from pokemon import *
from pessoa import *

def fist_Poke(player):
    eevee = PokeNormal('Eevee', level=1)
    starmie = PokeWater('Starmie', level=1)
    muk = PokePoison('Muk', level=1)

    print('voce possui 1 escolha dentre 3 opçoes...')
    print('1 - ', eevee)
    print('2 - ', starmie)
    print('3 - ', muk)
    print('Pense com cuidado... Temos tempo')

    while True:
        escolha = input('Qual deles sera seu companheiro? \n')

        if escolha == '1':
            player.capturar_poke(eevee)
            break
        elif escolha == '2':
            player.capturar_poke(starmie)
            break
        elif escolha == '3':
            player.capturar_poke(muk)
            break
        else:
            print('infelizmente esta opção não esta disponivel')

def save_game(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
            print('jogo salvo com sucesso')
    except Exception as error:
        print('ocorreu um erro ao salvar o jogo')
        print(error)

def game_load():
    try:
        with open('database.db', 'rb') as arquivo:
            player = pickle.load(arquivo)
            print('Jogo carregado')
            return player
    except Exception as error:
        print('ocorreu um erro ao carregar seu save')
        print(error)
        return None



if __name__ == '__main__':
    print('Seja Bem-Vindo ao incrivel mundo de pokemon')
    print('para começar vamos pelo basico...')

    player = game_load()

    if not player:
        nome = input('qual seu Nome treinador?  \n')
        player = Player(nome)
        player.capturar_poke(PokeIce('Gengar', level = 10))
        if player.team:
            print('vejo que voce ja possui alguns pokemons')
            player.mostrar_poke()
        else:
            print('parece que voce não possui nenhum pokemon')
            fist_Poke(player)
            player.mostrar_poke()
        print('certo {} agora vamos começar enfrentando...'.format(nome))
        print('CARLOS SEU AQUI RIVAL DESDE DE TODA SUA VIDA')
        Carlos = Inimigo('Carlos', team=[PokeWater('Empoleon', level=1)])
        resultado = player.batalhar(Carlos)

        if resultado == 'vitoria':
            print('{} parece que voce se saiu bem desta vez, porem saiba... '.format(nome))
            print('Ele vaiu voltar... e com muita raiva ')
        if resultado == 'derrota':
            print('{} Parece que voce não foi forte o bastante em'.format(nome))
            print('Melhore, treine e se torne mais forte isso não pode acabar assim')
        save_game(player)

    print('Bom ja que voce aprendeu a batalhar \n')
    print('acho que voce ja esta apto a se aventurar mundo afora \n')
    print('Então oque deseja fazer agora')


    def Menu():
        print('1 - Sair em uma exploração')
        print('2 - Batalhar')
        print('3 - Mostrar PokeData')
        print('0 - Sair do jogo')
    Menu()
    while True:
        escolha = input('Sua escolha:')

        if escolha == '1':
            player.explorar()
            save_game(player)
            Menu()
        elif escolha == '2':
            player.batalhar(Inimigo())
            save_game(player)
            Menu()
        elif escolha == '3':
            player.mostrar_poke()
            Menu()
        elif escolha == '0':
            print('Fechando o jogo, Ate a proxima...')
            break
        else:
            print('infelizmente esta opção não esta disponivel')
            Menu()







