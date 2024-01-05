entry_1 = input('Введите первый список: ').split()
list_1 = [int(x) for x in entry_1]  # Generate list 1

entry_2 = input('Введите второй список: ').split()
list_2 = [int(x) for x in entry_2]  # Generate list 2

set_1 = set(list_1)  # Let's convert to sets 1
set_2 = set(list_2)  # Let's convert to sets 2

its = set_1.intersection(set_2)  # Let's see if there's any overlap in the lists.
count_its = len(its)  # len intersection
print(f'Колово пересечений: {count_its}')
