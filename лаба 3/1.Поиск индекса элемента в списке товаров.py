# TODO Напишите функцию find_common_items
def find_common_items(a, b):
    общие = list(set(a).intersection(b))
    общие.sort()
    return общие

last_week_items = ['книга', 'ноутбук', 'флешка', 'мышь']
current_week_items = ['ноутбук', 'флешка', 'наушники', 'монитор']
надо = find_common_items(last_week_items, current_week_items)
print(f"Общие товары: {надо}")  # TODO Распечатайте общие товары
