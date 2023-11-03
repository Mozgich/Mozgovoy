# TODO Найдите количество книг, которое можно разместить на дискете
Number_of_characters_in_a_string = 25
Number_of_lines_per_page = 50
Number_of_pages_in_the_book = 100
disc_volume = 1.44 # мб
symbol_size = 4 # байта
total_symbols_in_the_book = Number_of_characters_in_a_string * Number_of_lines_per_page * Number_of_pages_in_the_book
volume_of_all_symbols_in_the_book = symbol_size * total_symbols_in_the_book
disc_volume = 1.44 * 1024 * 1024  # в байтах
book_number = disc_volume / volume_of_all_symbols_in_the_book
print("Количество книг, помещающихся на дискету:", round(book_number))
