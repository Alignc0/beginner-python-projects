# 1. Kullanıcıdan iki sayı alarak toplama, çıkarma, çarpma ve bölme işlemlerini yapan bir hesap makinesi uygulaması
# # Bu kod, kullanıcıdan iki sayı alır ve bu sayılar üzerinde toplama, çıkarma, çarpma ve bölme işlemlerini yapar.

# def toplama(a, b):
#     return a + b

# def cikarma(a, b):
#     return a - b

# def carpma(a, b):
#     return a * b

# def bolme(a, b):
#     if b == 0:
#         return "Hata: Bölme işlemi için bölen sıfır olamaz."
#     return a / b

# def hesap_makinesi():
#     print("Hesap Makinesi")
#     print("İşlemler:")
#     print("1. Toplama")
#     print("2. Çıkarma")
#     print("3. Çarpma")
#     print("4. Bölme")

#     secim = input("İşlemi seçin (1/2/3/4): ")

#     sayi1 = float(input("Birinci sayıyı girin: "))
#     sayi2 = float(input("İkinci sayıyı girin: "))

#     if secim == '1':
#         print(f"Sonuç: {toplama(sayi1, sayi2)}")
#     elif secim == '2':
#         print(f"Sonuç: {cikarma(sayi1, sayi2)}")
#     elif secim == '3':
#         print(f"Sonuç: {carpma(sayi1, sayi2)}")
#     elif secim == '4':
#         print(f"Sonuç: {bolme(sayi1, sayi2)}")
#     else:
#         print("Geçersiz giriş")

# if __name__ == "__main__":
#     hesap_makinesi()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 2. Kullanıcıdan iki sayı ve işlem türü alarak hesap yapan bir hesap makinesi uygulaması
# # Bu kod, kullanıcıdan iki sayı ve işlem türü alarak hesap yapan bir hesap makinesi uygulamasıdır.

# a = float(input("Birinci sayıyı girin: "))
# b = float(input("İkinci sayıyı girin: "))

# islem = input("Yapmak istediğiniz işlemi girin (+, -, *, /): ")
# if islem == "+":
#     print(f"{a}+{b} = {a + b}")
# elif islem == "-":
#     print(f"{a}-{b} = {a - b}")
# elif islem == "*":
#     print(f"{a}*{b} = {a * b}")
# elif islem == "/":
#     if b == 0:
#         print("Bölme işlemi için bölen sıfır olamaz.")
#     else:
#         print(f"{a}/{b} = {a / b}")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 3. Basit halde bir hesap makinesi uygulaması

# a = float(input("Birinci sayıyı girin: "))
# b = float(input("İkinci sayıyı girin: "))

# toplama = a + b
# cikarma = a - b
# carpma = a * b
# bolme = a / b

# print("toplama: ", toplama)
# print("çıkarma: ", cikarma)
# print("çarpma: ", carpma)
# print("bölme: ", bolme)
# print("işlemler tamamlandı.")

# Fonksiyonlar ile hesap makinesi uygulaması
# Bu kod, kullanıcıdan iki sayı alır ve bu sayılar üzerinde toplama, çıkarma, çarpma ve bölme işlemlerini yapar.

def topla(a,b):
    return a+b
def çıkar(a,b):
    return a-b
def çarp(a,b):
    return a*b
def böl(a,b):
    return a/b
a = float(input("İlk sayıyı giriniz:"))
b = float(input("ikinci sayıyı giriniz:"))

print("toplama işlemi sonucu: ", topla(a,b))
print("çıkarma işlemi sonucu: ", çıkar(a,b))
print("çarpma işlemi sonucu: ", çarp(a,b))
print("bölme işlemi sonucu: ", böl(a,b))