# Ceaser Cipher

def ceaser_cipher(metin, anahtar, islem):
    sonuc = ""
    
    for harf in metin:
        if harf.isalpha():
            ascii_offset = 65 if harf.isupper() else 97
            if islem == "e":
                yeni_harf = chr((ord(harf) - ascii_offset + anahtar) % 26 + ascii_offset)
            elif islem == "d":
                yeni_harf = chr((ord(harf) - ascii_offset - anahtar) % 26 + ascii_offset)
            sonuc += yeni_harf
        else:
            sonuc += harf
    return sonuc

metin = input("Metin giriniz: ")

try:
    anahtar = int(input("Anahtarı (0-25) giriniz: "))
    if anahtar < 0 or anahtar > 25:
        print("Hata: Anahtar 0 ile 25 arasında olmalıdır!")
        exit()
except ValueError:
    print("Hata: Anahtar bir sayı olmalıdır!")
    exit()

islem = input("Şifrelemek için 'e', çözmek için 'd' basınız: ").lower()
if islem not in ["e", "d"]:
    print("Hata: İşlem türü sadece 'e' veya 'd' olabilir!")
    exit()

sonuc = ceaser_cipher(metin, anahtar, islem)
print("Sonuç:", sonuc)