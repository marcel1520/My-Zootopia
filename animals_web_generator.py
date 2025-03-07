import json

def load_data(file_path):
    '''Loads json file'''
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_animal_data(animal_list):
    '''retrieving animal info'''
    animal_info = ""
    for animal in animal_list:
        animal_name = animal["name"]
        diet = animal["characteristics"]["diet"]
        location = ", ".join(map(str, animal["locations"]))
        character = animal["characteristics"]
        if "type" in character:
            character_type = character["type"]
            animal_info += (f"name: {animal_name}\n"
                            f"Diet: {diet}\n"
                            f"Location: {location}\n"
                            f"Type: {character_type}\n\n")
        else:
            animal_info += (f"name: {animal_name}\n"
                            f"Diet: {diet}\n"
                            f"Location: {location}\n\n")
    return animal_info


def main():
    animal_data = load_data("animals_data.json")
    animal_data_get = get_animal_data(animal_data)
    print(animal_data_get)


if __name__ == "__main__":
    main()


