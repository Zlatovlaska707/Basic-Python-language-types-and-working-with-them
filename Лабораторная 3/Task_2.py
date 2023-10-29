# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separator='|'):
    # Разбиваем строки на списки фамилий участников, используя указанный разделитель
    participants1 = participants_first_group.split(separator)
    participants2 = participants_second_group.split(separator)

    # Преобразуем списки во множества для поиска общих участников
    participants_set = set(participants1).intersection(participants2)

    # Преобразуем множество в список и сортируем его в алфавитном порядке
    participants_sorted = sorted(list(participants_set))

    return participants_sorted

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print("Общие участники: ", find_common_participants(participants_first_group, participants_second_group))
