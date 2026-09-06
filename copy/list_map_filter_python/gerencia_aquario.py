import json

f = open("aquario.json", encoding="utf8")
data_aquario = json.load(f)
animals = data_aquario["data"]

def verificar_peixe(animal):
    if animal["type"] == "fish":
        return True
    return False

animals_fish = list(filter(verificar_peixe, animals))

def animal_name(animal):
    return animal["name"]

animals_fish_name = list(map(animal_name, animals_fish))
print(animals_fish_name)

def assistencia_do_tank(animals, names_selected, new_tank_number):
    def change_tank_number(animal):
        if animal["name"] in names_selected:
            animal["tank number"] = new_tank_number
        return animal
    return list(map(change_tank_number, animals))
    
new_aquario = assistencia_do_tank(animals, animals_fish_name, 42)
print(new_aquario)