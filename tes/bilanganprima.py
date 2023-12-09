def cari_bilangan_prima(number):
    prime_number = []

    for num in range(2,number):
        is_prime = True

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_number.append(num)

    print("Bilangan prima yang lebih kecil dari", number, "adalah", prime_number)

cari_bilangan_prima(11)