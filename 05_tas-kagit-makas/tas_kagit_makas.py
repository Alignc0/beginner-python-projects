#  TAŞ-KAĞIT-MAKAS OYUNU
# 1. Oyuncu ve bilgisayarın seçimini alacak
# 2. Oyuncunun seçimi ve bilgisayarın seçimi karşılaştırılacak
# 3. Kazanan belirlenecek
# 4. Oyun devam edecek mi sorulacak
import random

print("-" * 30 + "Taş-Kağıt-Makas Oyununa Hoş Geldiniz!" + "-" * 30)


kullanıcı = input("Taş, Kağıt veya Makas seçin: ").lower()
bilgisayar = random.choice(["taş", "kağıt", "makas"])
print("Bilgisayarın seçimi:", bilgisayar)
hak = 3


while hak > 0:
    if (kullanıcı == "taş" and bilgisayar == "makas") \
        or (kullanıcı == "kağıt" and bilgisayar == "taş") \
        or (kullanıcı == "makas" and bilgisayar == "kağıt"):
            print("Kazandınız!")
            print("Kalan hak sayınız:", hak)
            
    elif (bilgisayar == "taş" and kullanıcı == "makas") \
        or (bilgisayar == "kağıt" and kullanıcı == "taş") \
        or (bilgisayar == "makas" and kullanıcı == "kağıt"):
            print("Kaybettiniz!")
            hak -= 1
            print("Kalan hak sayınız:", hak)
    else:
            print("Berabere!")
            print("Kalan hak sayınız:", hak)
    
    if hak > 0:
        kullanıcı = input("Taş, Kağıt veya Makas seçin: ").lower()
        bilgisayar = random.choice(["taş", "kağıt", "makas"])
        print("Bilgisayarın seçimi:", bilgisayar)

print("Oyun bitti! Haklarınız tükendi.")




