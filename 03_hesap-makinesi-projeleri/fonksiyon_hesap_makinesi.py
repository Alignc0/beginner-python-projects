# hesap makinesi


print(("-" * 20) + "Hesap Makinesi\n" + ("-" * 20))


def topla(a, b):
    return a + b
def çıkar(a, b):
    return a - b
def çarp(a, b):
    return a * b
def böl(a, b):
    return a / b

print("Hangi işlemi yapmmak istersiniz? \n 1. Toplama \n 2. Çıkarma \n 3. Çarpma \n 4. Bölme \nSeçiminiz: ")
secim = input("İşlemi seçin (1/2/3/4): ")
if secim == '1':
    print("Toplama işlemi seçtiniz.")
elif secim == '2':
    print("Çıkarma işlemi seçtiniz.")
elif secim == '3':
    print("Çarpma işlemi seçtiniz.")
elif secim == '4':
    print("Bölme işlemi seçtiniz.")
else:
    print("Geçersiz işlem seçimi...")
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
if secim == '1':
    print(f"Toplam sonucu: {topla(sayi1, sayi2)}")
elif secim == '2':
    print(f"Kalan sonucu : {çıkar(sayi1, sayi2)}")
elif secim == '3':
    print(f"Çarpım sonucu: {çarp(sayi1, sayi2)}")
elif secim == '4':
    print(f"Bölme sonucu: {böl(sayi1, sayi2)}")

