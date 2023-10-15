# TODO Найдите количество книг, которое можно разместить на дискете


disk_volume_max = 1.44 * 1024 * 1024    # Информационный объем дискеты в байтах
number_pages = 100                      # Количество страниц в книге
number_str = 50                         # Число строк на странице
number_characters = 25                  # Количество символов в строке
character = 4                           # Хранение кода 1-го символа в байтах

number_books = int(disk_volume_max // (character*number_characters*number_str*number_pages))
print("Количество книг, помещающихся на дискету:", number_books)
