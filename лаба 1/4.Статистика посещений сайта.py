users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
size = len(users)
unique = len(set(users))
dict = {
    "Общее количество": 0,
    "Уникальные посещения": 0,
}
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dict = {
    "Общее количество": size,
    "Уникальные посещения": unique
}
print(dict)
