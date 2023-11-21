with open('files.txt', 'r',encoding='UTF-8') as file:
    cook_book = {}
    for line in file:
        recipe_name = line.strip()
        ingredients_count = int(file.readline().strip())
        ingredients = []
        for item in range(ingredients_count):
            ingredient, quantity, measure = (
                file.readline().strip().split(' | '))
            ingredients.append({'ingredient': ingredient, 'quantity': quantity,
                                'measure': measure})
        cook_book[recipe_name] = ingredients
        file.readline()
    print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for recipe_name in dishes:
        for ingredient in cook_book[recipe_name]:
            ingredients_list = dict([(ingredient['ingredient'],
                      {'quantity': int(ingredient['quantity']) * person_count,
                                       'measure': ingredient['measure']})])
            if not shop_list.get(ingredient['ingredient']) == None:
                shop_list[ingredient['ingredient']]['quantity'] = (
                        int(shop_list[ingredient['ingredient']]['quantity']) +
                 int(ingredients_list[ingredient['ingredient']]['quantity']))
            else:
                shop_list.update(ingredients_list)
    return shop_list
print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель',
                               'Утка по-пекински', 'Фахитос'], 3))
