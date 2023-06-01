#Если в функцию передаётся кортеж, то посчитать длину всех его строк.
#Если список, то посчитать кол-во букв и чисел в нём.
#Число – кол-во нечётных цифр.
#Строка – кол-во букв.
#Сделать проверку со всеми этими случаями.
#Использовать готовые типы данных, с клавиатуры ничего не вводится
def print_data_type(func):
    def wrapper(data):
        data_type = type(data).__name__
        print(f"Data type: {data_type}")
        return func(data)
    return wrapper
@print_data_type
def count_elements(data):
    if isinstance(data, tuple):
        total_length = sum(len(str(item)) for item in data if isinstance(item, str))
        print(f"Total length of all strings: {total_length}")
    elif isinstance(data, list):
        total_letters = sum(len(str(item)) for item in data if isinstance(item, str))
        total_numbers = sum(1 for item in data if isinstance(item, int) or isinstance(item, float))
        print(f"Total letters: {total_letters}")
        print(f"Total numbers: {total_numbers}")
    elif isinstance(data, int):
        odd_digit_count = sum(1 for digit in str(data) if int(digit) % 2 != 0)
        print(f"Odd digit count: {odd_digit_count}")
    elif isinstance(data, str):
        letter_count = sum(1 for char in data if char.isalpha())
        print(f"Letter count: {letter_count}")
    else:
        print("Invalid input type. Please provide a tuple, list, or integer.")
        print(f'Data type: {type(data).__name__}')
count_elements(('asd', 'qwe', 'ASDFGH'))
count_elements([1, 2, 'a@#', 'adas', 123])
count_elements(1234567)
count_elements('asdfghjk')
