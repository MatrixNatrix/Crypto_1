# Функция для нахождения наибольшего общего делителя двух чисел
def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

# Расширенный алгоритм Евклида для нахождения НОД и коэффициентов x, y
def extended_euclidean_algorithm(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_euclidean_algorithm(b % a, a)
        return (gcd, y - (b // a) * x, x)

# Функция для шифрования/дешифрования текста с использованием аффинного шифра
def affine_cipher(text, coefficient_a, coefficient_b, alphabet, mode):
    char_list = list(alphabet)  # Создание списка символов алфавита
    result = ""  # Переменная для хранения результата шифрования/дешифрования
    p = len(char_list)  # Длина алфавита
    char_copy = [i for i in char_list]  # Копирование списка символов алфавита
    a_inv = extended_euclidean_algorithm(coefficient_a, p)[1] % p  # Вычисление обратного элемента по модулю p
    for char in text:  # Перебор символов в тексте
        for j in char_copy:  # Перебор символов в копии алфавита
            if char == j:  # Если символ из текста совпадает с символом из алфавита
                if mode == 'encrypt':  # Если выбран режим шифрования
                    result += char_copy[((coefficient_a * char_copy.index(j) + coefficient_b) % p)]  # Шифрование
                elif mode == 'decrypt':  # Если выбран режим дешифрования
                    result += char_copy[(a_inv * (char_copy.index(j) - coefficient_b)) % p]  # Дешифрование
    return result

if __name__ == '__main__':
    user_text = input("Введите текст для шифрования/дешифрования: ")  # Ввод текста от пользователя
    user_mode = input("Выберите режим работы ('encrypt' для шифрования, 'decrypt' для дешифрования): ")  # Выбор режима работы
    user_coefficient_a = int(input("Введите параметр a: "))  # Ввод параметров ключа
    user_coefficient_b = int(input("Введите параметр b: "))  # Ввод параметров ключа
    user_alphabet = ',- !?./йцукенгшщзхъфывапролджэячстмиьбюЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ'  # Задание алфавита

    if user_mode == 'encrypt':  # Если выбран режим шифрования
        encrypted_text = affine_cipher(user_text, user_coefficient_a, user_coefficient_b, user_alphabet, user_mode)  # Шифрование текста
        print(f"Зашифрованный текст: {encrypted_text}")  # Вывод зашифрованного текста
    elif user_mode == 'decrypt':  # Если выбран режим дешифрования
        decrypted_text = affine_cipher(user_text, user_coefficient_a, user_coefficient_b, user_alphabet, user_mode)  # Дешифрование текста
        print(f"Расшифрованный текст: {decrypted_text}")  # Вывод расшифрованного текста
    else:
        print("Некорректный режим работы. Пожалуйста, выберите 'encrypt' или 'decrypt'.")  # Вывод сообщения об ошибке при некорректном режиме