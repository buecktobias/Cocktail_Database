import requests



URL_RANDOM = "https://www.thecocktaildb.com/api/json/v1/1/random.php"

URL_ID = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i="


def get_cocktail(id_, session):
    r = session.get(URL_ID + str(id_))
    json_o = r.json()
    if "drinks" in json_o and json_o["drinks"] is not None:
        drink = json_o["drinks"][0]
        print(drink)
        name = drink["strDrink"]
        return name
    else:
        return ""

def get_random_cocktail(session):
    r = session.get(URL_RANDOM)
    json_o = r.json()
    if "drinks" in json_o and json_o["drinks"] is not None:
        drink = json_o["drinks"][0]
        return drink
    else:
        return None

def get_cocktail_name(session):
    cocktail = get_random_cocktail(session)
    if cocktail is not None:
        return cocktail["strDrink"]
    else:
        return ""


def get_cocktail_glass(session):
    cocktail = get_random_cocktail(session)
    if cocktail is not None:
        glass = cocktail["strGlass"]
    else:
        return ""
    return glass


def get_cocktail_ingredients(session):
    ingredients = []
    cocktail = get_random_cocktail(session)
    ingredient_string = "strIngredient"
    if cocktail is not None:
        for i in range(1, 15):
            ingredients.append(cocktail[ingredient_string + str(i)])
    ingredients = list(set(ingredients))
    if None in ingredients:
        ingredients.remove(None)
    return ingredients


def get_glasses(count):
    names = []
    session = requests.Session()
    for i in range(count):
        name = get_cocktail_glass(session)
        name = name.replace("\'", "")
        names.append(name)

    return list(set(names))


def get_ingredients(count):
    names = []
    session = requests.Session()
    for i in range(count):
        name = get_cocktail_ingredients(session)
        name = list(map(lambda x: x.replace("\'", ""), name))
        names.extend(name)
    return list(set(names))

def get_cocktail_names(count):
    names = []
    session = requests.Session()
    for i in range(count):
        name = get_cocktail_name(session)
        name = name.replace("\'", "")
        names.append(name)
    return names


if __name__ == '__main__':
    session = requests.Session()
    print(get_ingredients(10))
