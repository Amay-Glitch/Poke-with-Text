import random
from pokemon import *

NOMES = ["Ana", "Bruno", "Camila", "Diego", "Elisa", "Felipe", "Gabriela", "Henrique", "Isabela", "João"]

PokeList = [
    # Elétrico
    PokeEletrico('Raikou'),
    PokeEletrico('Zapdos'),
    PokeEletrico('Jolteon'),
    PokeEletrico('Luxray'),
    PokeEletrico('Electivire'),
    PokeEletrico('Manectric'),
    PokeEletrico('Rotom'),

    # Fantasma
    PokeGhost('Gengar'),
    PokeGhost('Mismagius'),
    PokeGhost('Banette'),
    PokeGhost('Dusclops'),
    PokeGhost('Cofagrigus'),
    PokeGhost('Drifblim'),
    PokeGhost('Chandelure'),

    # Gelo
    PokeIce('Glacie'),
    PokeIce('Articuno'),
    PokeIce('Lapras'),
    PokeIce('Froslass'),
    PokeIce('Weavile'),
    PokeIce('Walrein'),
    PokeIce('Glaceon'),

    # Noturno
    PokeDark('Darkrai'),
    PokeDark('Umbreon'),
    PokeDark('Absol'),
    PokeDark('Honchkrow'),
    PokeDark('Zoroark'),
    PokeDark('Hydreigon'),
    PokeDark('Tyranitar'),

    # Normal
    PokeNormal('Snorlax'),
    PokeNormal('Porygon-Z'),
    PokeNormal('Blissey'),
    PokeNormal('Tauros'),
    PokeNormal('Ditto'),
    PokeNormal('Eevee'),
    PokeNormal('Exploud'),

    # Fogo
    PokeFire('Charizard'),
    PokeFire('Arcanine'),
    PokeFire('Infernape'),
    PokeFire('Blaziken'),
    PokeFire('Moltres'),
    PokeFire('Magmortar'),
    PokeFire('Ninetales'),

    # Água
    PokeWater('Suicune'),
    PokeWater('Vaporeon'),
    PokeWater('Milotic'),
    PokeWater('Gyarados'),
    PokeWater('Starmie'),
    PokeWater('Kingdra'),
    PokeWater('Empoleon'),

    # Planta
    PokeGrass('Venusaur'),
    PokeGrass('Sceptile'),
    PokeGrass('Roserade'),
    PokeGrass('Leafeon'),
    PokeGrass('Shaymin'),
    PokeGrass('Torterra'),
    PokeGrass('Ludicolo'),

    # Psíquico
    PokePsychic('Mewtwo'),
    PokePsychic('Alakazam'),
    PokePsychic('Metagross'),
    PokePsychic('Espeon'),
    PokePsychic('Gallade'),
    PokePsychic('Starmie'),
    PokePsychic('Jirachi'),

    # Veneno
    PokePoison('Nidoking'),
    PokePoison('Crobat'),
    PokePoison('Roserade'),
    PokePoison('Muk'),
    PokePoison('Toxicroak'),
    PokePoison('Gengar'),
    PokePoison('Weezing'),

    # Lutador
    PokeFighting('Machamp'),
    PokeFighting('Lucario'),
    PokeFighting('Conkeldurr'),
    PokeFighting('Hitmonlee'),
    PokeFighting('Hitmonchan'),
    PokeFighting('Gallade'),
    PokeFighting('Infernape'),

    # Terra
    PokeGround('Garchomp'),
    PokeGround('Rhyperior'),
    PokeGround('Swampert'),
    PokeGround('Excadrill'),
    PokeGround('Nidoking'),
    PokeGround('Mamoswine'),
    PokeGround('Flygon'),

    # Dragão
    PokeDragon('Dragonite'),
    PokeDragon('Salamence'),
    PokeDragon('Garchomp'),
    PokeDragon('Latios'),
    PokeDragon('Latias'),
    PokeDragon('Rayquaza'),
    PokeDragon('Haxorus'),
]


class Pessoa:

    def __init__(self, nome=None, team=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.team = team
        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def mostrar_poke(self):
        if self.team:
            print('==================================')
            print('Pokemons de {}:'.format(self))
            for index,pokemon in enumerate(self.team):
                print('{} - {}'.format(index, pokemon))
            print('==================================')
        else:
            print('{} não tem pokemons'.format(self))

    def poke_chose(self):
        if self.team:
            poke_chose = random.choice(self.team)
            print('{} escolheu {}'.format(self, poke_chose))
            return poke_chose
        else:
            print('ERRO: Este jogador não possui pokemons elegiveis')



    def batalhar(self, pessoa):
        print('{} Inicio um combate contra {}'.format(self, pessoa))

        pessoa.mostrar_poke()
        pokemon_inimigo = pessoa.poke_chose()

        my_poke = self.poke_chose()

        if my_poke and pokemon_inimigo:
            while True:
                vitoria = my_poke.atacar(pokemon_inimigo)
                if vitoria:
                    print('{} Ganhou o combate'.format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 50)
                    return "vitoria"


                vitoria_inimiga = pokemon_inimigo.atacar(my_poke)
                if vitoria_inimiga:
                    print('{} Perdeu o combate'.format(self))
                    return 'derrota'

        else:
            print('este combate não pode acontecer')


    def mostrar_dinheiro(self):
        print('voce tem R${} em sua conta'.format(self.dinheiro))

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print('voce ganhou R${}'.format(quantidade))
        self.mostrar_dinheiro()


class Player(Pessoa):
    tipo = 'Player'

    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(PokeList)
            print('um {} apareceu!!!'.format(pokemon))
            escolha = input('Deseja tentar capturar este pokemon Selvagem? (S/N)')

            if escolha == 's' or 'S' or 'Sim' or 'sim':
                if random.random() >=0.5:
                    self.capturar_poke(pokemon)
                else:
                    print('O {} selvagem escapou'.format(pokemon))
            else:
                print('Certo então ate a proxima')
        else:
            print('Desta vez voce não encontrou nada... que pena')


    def capturar_poke(self, Pokemon):
        self.team.append(Pokemon)
        print('{} Capturou {} com sucesso!!!'.format(self, Pokemon))

    def poke_chose(self):
        self.mostrar_poke()

        if self.team:
            while True:
                escolha = input('Escolha um de seus Pokemons!!!')
                try:
                    escolha = int(escolha)
                    poke_chose = self.team[escolha]
                    print('{} eu escolho voce!!!'.format(poke_chose))
                    return poke_chose
                except:
                    print('escolha invalida')
        else:
            print('ERRO: Este jogador não possui pokemons elegiveis')


class Inimigo(Pessoa):
    tipo = 'Inimigo'

    def __init__(self, nome=None, team=None):
        if team is None:
            team = [random.choice(PokeList) for _ in range(random.randint(1, 6))]

        super().__init__(nome=nome, team=team)



