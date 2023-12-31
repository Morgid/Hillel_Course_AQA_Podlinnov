# ДЗ 7 Уроку
#
# Створіть два файли
# в 1-му напишіть такі функції:
# 1) сортування списка по зростанню числа, від меншого до більшого. Функція приймає список з чисел і повертає відсортований список.
# 2) сортування списка на спад, від  більшого до меншого. Функція приймає список з чисел і повертає відсортований список.
# 3) сортування за кількістю букв у слові. Функція приймає список з слів і повертає відсортований список.
#
# 2-ий файл з трьома тестами який буде тестити ці три функції. В кожному тесті 1 тест.
# В тестових функціях ми ставимо типізацію. В першому файлі в всіх функціях проставляємо що приймає і що повертає.
# Встановіть собі пайтест і прораньте. До домашки отрім кода додайте скріншот прогона тестів.

def sorting_by_increase(list_of_numbers: list = [12, 22, 1, 3, 2, 4, -5, -66, -777, 0, 66, 400, 55.4, 66.6]) -> list:
    increase_result = sorted(list_of_numbers)
    return increase_result


def sorting_by_decrease(list_of_numbers: list = [12, 22, 1, 3, 2, 4, -5, -66, -777, 0, 66, 400, 55.4, 66.6]) -> list:
    decrease_result = sorted(list_of_numbers, reverse=True)
    return decrease_result


def sorting_by_letters(list_fo_words: list = ["ця", "фраза", "сортування", "Є", "перевірки", "одна", "лиш", "роботи",
                                              "функцією!!!"]) -> list:
    letters_lens_result = sorted(list_fo_words, key=len)
    return letters_lens_result
