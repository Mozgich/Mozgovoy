# TODO Напишите функцию find_common_items
def find_common_items(a, b):
    common = list(set(a).intersection(b))
    common.sort()
    return common

last_week_items = ['книга', 'ноутбук', 'флешка', 'мышь']
current_week_items = ['ноутбук', 'флешка', 'наушники', 'монитор']
current_items = find_common_items(last_week_items, current_week_items)
print(f"Общие товары: {current_items}")  # TODO Распечатайте общие товары
