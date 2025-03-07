import json


def load_data(file_path):
    '''Loads json file'''
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal_data(animal):
    '''serialize animal data'''
    animal_info = ""
    animal_name = animal["name"]
    diet = animal["characteristics"]["diet"]
    location = ", ".join(map(str, animal["locations"]))
    character = animal["characteristics"]
    if "type" in character:
        character_type = character["type"]
        animal_info += ("<li class='cards__item'>\n"
                        f"<div class='card__title'>{animal_name}</div>"
                        f"<strong>Diet:</strong> {diet}<br/>\n"
                        f"<strong>Location:</strong> {location}<br/>\n"
                        f"<strong>Type:</strong> {character_type}<br/>\n"
                        '</li>\n')
    else:
        animal_info += ("<li class='cards__item'>\n"
                        f"<div class='card__title'>{animal_name}</div>"
                        f"<strong>Diet:</strong> {diet}<br/>\n"
                        f"<strong>Location:</strong> {location}<br/>\n"
                        '</li>\n')
    return animal_info


def get_animal_data(animal_list):
    '''retrieving animal info'''
    animal_info = ""
    for animal in animal_list:
        animal_info += serialize_animal_data(animal)
    return animal_info


def read_html_file(html_animal):
    '''reads html file'''
    with open(html_animal, "r") as html_animal_file:
        animal_html = html_animal_file.read()
        return animal_html


def replace_string(old_string, new_string):
    '''replaces target string from html file with animal info'''
    string_to_replace = "__REPLACE_ANIMALS_INFO__"
    text_to_replace = old_string
    html_with_replace = text_to_replace.replace(string_to_replace, new_string)
    return html_with_replace


def write_animal_html(animal_html_replaced):
    '''writes html file with animal data in class'''
    animal_html = "animal.html"
    with open(animal_html, "w") as new_animal_file:
        new_animal_file.write(animal_html_replaced)
        return new_animal_file


def main():
    '''loads animal data, creates animal string, reads html,
    replaces html target string with animal data'''
    animal_data = load_data("animals_data.json")
    animal_data_get = get_animal_data(animal_data)
    html_file_read = read_html_file("animals_template.html")
    string_replace = replace_string(html_file_read, animal_data_get)
    write_animal_html(string_replace)


if __name__ == "__main__":
    main()


