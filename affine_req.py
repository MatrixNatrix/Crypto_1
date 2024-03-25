def gcd(x, y):  # Функция для нахождения наибольшего общего делителя
    while y != 0:  # Пока второе число не равно нулю
        y, x = x % y, y  # Находим остаток от деления и меняем местами числа
    return x

# Расширенный алгоритм Евклида, вычисление a^-1 (mod b)
def extended_euclidean(a, b):  # Расширенный алгоритм Евклида для нахождения обратного элемента
    if gcd(a, b) > 1:  # Если НОД больше 1
        print("Нет обратного элемента")
        return False
    else:
        t = 1
        y = 0.5
        while y % 1 != 0:  # Пока дробная часть не равна нулю
            y = ((1 - t * b) / a) % b
            t += 1
        t = t - 1
        if y > b / 2:
            y = int(y - b)
        if t > b / 2:
            t = int(t - b)
        return [int(y), t]

# Аффинный рекуррентный шифр
def affine_recurrent_cipher(text, a, b, c, d, alphabet):  # Шифрование текста аффинным рекуррентным шифром
    char_dict = [char for char in alphabet]
    result = ""
    p = len(char_dict)
    for char in text:
        for j in char_dict:
            if char == j:
                y = a * c % p
                x = (b + d) % p
                result += char_dict[((y * char_dict.index(j) + x) % p)]
                a, c, b, d = c, y, d, x
    print(f"Зашифровано аффинным рекуррентным шифром : {result}\n")
    return [result, a, b, c, d]

# Расшифровка аффинного рекуррентного шифра
def decrypt_affine_recurrent_cipher(text, a, b, c, d, alphabet):  # Расшифровка текста аффинным рекуррентным шифром
    char_dict = [char for char in alphabet]
    result = ""
    p = len(char_dict)
    for char in text:
        for j in char_dict:
            if char == j:
                y = a * c % p
                x = (b + d) % p
                result += char_dict[(extended_euclidean(y,p)[0] * (char_dict.index(j) - x)) % p]
                a, c, b, d = c, y, d, x
    print(f"Результат расшифровки : {result}\n")
    return result

# Демонстрация работы
def main():
    alphabet = ",- !?./йцукенгшщзхъфывапролджэячстмиьбюЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ"
    mode = input("Выберите режим (encryption - 'e', decryption - 'd'): ")
    if mode == 'e':  # Если выбран режим шифрования
        plaintext = input("Введите открытый текст для шифрования: ")
        a = int(input("Введите параметр a: "))
        b = int(input("Введите параметр b: "))
        c = int(input("Введите параметр c: "))
        d = int(input("Введите параметр d: "))
        m = affine_recurrent_cipher(plaintext, a, b, c, d, alphabet)
    elif mode == 'd':  # Если выбран режим дешифрования
        ciphertext = input("Введите зашифрованный текст для дешифрования: ")
        a = int(input("Введите параметр a: "))
        b = int(input("Введите параметр b: "))
        c = int(input("Введите параметр c: "))
        d = int(input("Введите параметр d: "))
        decrypt_affine_recurrent_cipher(ciphertext,a,b,c,d,alphabet)
    else:
        print("Некорректный режим. Пожалуйста, выберите 'e' для шифрования или 'd' для дешифрования.")

if __name__ == "__main__":
    main()