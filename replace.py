# Импорт необходимых модулей
import pyperclip
import random

# Алфавит для шифрования
ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

# Основная функция программы
def main():
    # Получение текста от пользователя
    user_input = input("Введите текст для шифрования или дешифрования: ")
    # Получение секретного ключа от пользователя
    encryption_key = input("Введите секретный ключ: ")
    # Выбор режима работы программы
    mode = input("Выберите режим работы ('encrypt' для шифрования, 'decrypt' для дешифрования): ")

    # Проверка валидности ключа
    if not is_key_valid(encryption_key):
        print('Ошибка в ключе или символьном наборе.')
        return

    # Шифрование или дешифрование текста в зависимости от выбранного режима
    if mode == 'encrypt':
        translated_message = encrypt_message(encryption_key, user_input)
        print('Зашифрованный текст:', translated_message)
    elif mode == 'decrypt':
        translated_message = decrypt_message(encryption_key, user_input)
        print('Расшифрованный текст:', translated_message)
    else:
        print('Некорректный режим работы.')

    # Копирование результата в буфер обмена
    pyperclip.copy(translated_message)
    print('Текст скопирован в буфер обмена.')

# Функция проверки валидности ключа
def is_key_valid(key):
    key_list = list(key)
    alphabet_list = list(ALPHABET)
    key_list.sort()
    alphabet_list.sort()

    return key_list == alphabet_list

# Функция шифрования текста
def encrypt_message(key, message):
    translated = ''
    chars_a = ALPHABET
    chars_b = key

    for symbol in message:
        if symbol.upper() in chars_a:
            sym_index = chars_a.find(symbol.upper())
            if symbol.isupper():
                translated += chars_b[sym_index].upper()
            else:
                translated += chars_b[sym_index].lower()
        else:
            translated += symbol

    return translated

# Функция дешифрования текста
def decrypt_message(key, message):
    translated = ''
    chars_a = ALPHABET
    chars_b = key

    for symbol in message:
        if symbol.upper() in chars_b:
            sym_index = chars_b.find(symbol.upper())
            if symbol.isupper():
                translated += chars_a[sym_index].upper()
            else:
                translated += chars_a[sym_index].lower()
        else:
            translated += symbol

    return translated

# Запуск программы при запуске файла
if __name__ == '__main__':
    main()