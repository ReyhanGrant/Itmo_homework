import requests
class Pokemon:
    def __init__(self, id, name, height, weight):
        self.id = id
        self.name = name
        self.height = height
        self.weight = weight
        pass
    def Pokename(self):
        print(self.name)
class BasePokemon(Pokemon):
    def __init__(self, name):
        Pokemon.__init__(self, name)
        self.name=name
        pass
class PokeApi():
    def __init__(self):
        pass
    def get_pokemon(self, pokename):
        try:
            url = 'https://pokeapi.co/api/v2/pokemon/' + pokename.lower()
            r = requests.get(url).json()
        except:
            return print("There is some errors")
        pokedex = Pokemon(str(r["id"]), r["name"], str(r["height"]), str(r["weight"]))
        print ("name: " + pokedex.name.upper())
        print("id: " + pokedex.id)
        print("height: " + pokedex.height)
        print("weight: " + pokedex.weight)
pokemon_name = input("Type pokemon id or pokemon name: ")
PokeApi().get_pokemon(pokemon_name)