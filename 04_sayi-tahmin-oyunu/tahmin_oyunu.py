# Sayı tahmin oyunu
# Bu oyun 1-100 arasında rastgele bir sayı seçer ve kullanıcıdan bu sayıyı tahmin etmesini ister.


import random

print(("-"*30),("Sayı tahmin oyununa hoş geldiniz"),("-"*30))
print("1-100 arasında bir sayı seçtim")
print("4 hakkın var")
print("Bakalım bulabilecek misin?")
print("Başlayalım")

sayı = random.randint(1, 100)
tahmin = int(input("Hadi tahmin et: "))
hak = 4

for x in range (1, 100):
    if tahmin == sayı:
        print("Helal olsun buldıun")
        break
    elif tahmin < sayı:
        print("Daha büyük bir sayı gir")
        hak -=1
        print("Kalan hakkın",hak)
        tahmin = int(input("Hadi tahmin et: "))
    elif tahmin > sayı:
        print("Daha küçük bir sayı gir")
        hak -=1
        print("Kalan hakkın",hak)
        tahmin = int(input("Hadi tahmin et: "))
    if hak == 0:
        print("Hakkın kalmadı")
        print("Seçtiğim sayı", sayı)
        print("Oyun bitti","birdahaki sefere")
        break