import random

class Pokemon:
    def __init__(self, especie, level=None, vida=10, nome=None):
        self.especie = especie
        self.vida = vida
        self.level = level
        if level:
            self.level = level
        else:
            self.level = random.randint(1,100)
        if nome:
            self.nome = nome
        else:
            self.nome = especie
        self.ataque = self.level * 5
        self.vida = self.level *  10


    def __str__(self):
        return "{}({})".format(self.nome, self.level)

    def atacar(self, Pokemon):
        ataque_efetivo = int(self.ataque * random.random() * 1.25)
        Pokemon.vida -= ataque_efetivo
        print('{} perdeu {} pontos de vida'.format(Pokemon, ataque_efetivo))

        if Pokemon.vida <= 0:
            print('{} Foi derrotado'.format(Pokemon))
            return True
        else:
            return False

class PokeEletrico(Pokemon):
    def atacar(self, Pokemon):
        print('{} lançou bola elétrica contra {}'.format(self, Pokemon))
        return super().atacar(Pokemon)

class PokeGhost(Pokemon):
    def atacar(self, Pokemon):
        print('{} lançou paranoia contra {}'.format(self, Pokemon))
        return super().atacar(Pokemon)

class PokeIce(Pokemon):
    def atacar(self, Pokemon):
        print('{} lançou espirro congelante contra {}'.format(self, Pokemon))
        return super().atacar(Pokemon)

class PokeDark(Pokemon):
    def atacar(self, Pokemon):
        print('{} lançou shadow flames contra {}'.format(self, Pokemon))
        return super().atacar(Pokemon)

class PokeNormal(Pokemon):
    def atacar(self, Pokemon):
        print('{} lançou investida corporal contra {}'.format(self, Pokemon))
        return super().atacar(Pokemon)

class PokeFire(Pokemon):
    def atacar(self, Pokemon):
        print('{} lançou rajada de fogo contra {}'.format(self, Pokemon))
        return super().atacar(Pokemon)

class PokeWater(Pokemon):
    def atacar(self, Pokemon):
        print('{} lançou jato d\'água contra {}'.format(self, Pokemon))
        return super().atacar(Pokemon)

class PokeGrass(Pokemon):
    def atacar(self, Pokemon):
        print('{} lançou chicote de cipó contra {}'.format(self, Pokemon))
        return super().atacar(Pokemon)

class PokePsychic(Pokemon):
    def atacar(self, Pokemon):
        print('{} lançou onda psíquica contra {}'.format(self, Pokemon))
        return super().atacar(Pokemon)

class PokePoison(Pokemon):
    def atacar(self, Pokemon):
        print('{} lançou gás tóxico contra {}'.format(self, Pokemon))
        return super().atacar(Pokemon)

class PokeFighting(Pokemon):
    def atacar(self, Pokemon):
        print('{} lançou soco devastador contra {}'.format(self, Pokemon))
        return super().atacar(Pokemon)

class PokeGround(Pokemon):
    def atacar(self, Pokemon):
        print('{} lançou terremoto contra {}'.format(self, Pokemon))
        return super().atacar(Pokemon)

class PokeDragon(Pokemon):
    def atacar(self, Pokemon):
        print('{} lançou fúria dracônica contra {}'.format(self, Pokemon))
        return super().atacar(Pokemon)
