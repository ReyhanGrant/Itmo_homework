import requests
from dataclasses import dataclass
@dataclass
class BasePokemon:
        name: str
        pass
@dataclass
class Pokemon(BasePokemon):
    id: str
    height: str
    weight: str
    pass

class PokeApi():
    @staticmethod
    def get_pokemon(pokename):
        try:
            url = 'https://pokeapi.co/api/v2/pokemon/' + pokename.lower()
            r = requests.get(url).json()
        except:
            return print("There is some errors")
        return Pokemon(str(r["name"]).capitalize() , str(r["id"]), str(r["height"]), str(r["weight"]))
    @staticmethod
    def get_all(get_name, state):
        if state=="True":
            print(PokeApi().get_pokemon(get_name))
        else:
            print(BasePokemon(PokeApi().get_pokemon(get_name).name))
pokemon_name = input("Type pokemon id or pokemon name: ")
state = input("Get all info?(True or False): ")
PokeApi().get_all(pokemon_name, state)
print("----------------------------")
PokeApi().get_all("ditto", "True")
poke_weight = 0
for i in range(49):
    number = i+1
    pokemon=PokeApi().get_pokemon(str(number))
    if int(pokemon.weight) > int(poke_weight):
        pocket_monster = pokemon
        poke_weight = int(pokemon.weight)
print(pocket_monster.name + " is the fattest pokemon with weight is " + pocket_monster.weight)