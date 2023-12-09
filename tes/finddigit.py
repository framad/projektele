def cari_digit(number, place):

    number_str = str(number)

    if 1 <= place <= len(number_str):
        digit_berada = int(number_str[place-1])
    else:
        digit_berada = None

    total_digit = len(number_str)
    return digit_berada, total_digit

number = 12345
angka_dicari = 2
digit_berada, total_digit = cari_digit(number, angka_dicari)

print(f"Angka {angka_dicari} di {number} adalah {digit_berada}")
print(f"Total Digit {number} adalah {total_digit}")
