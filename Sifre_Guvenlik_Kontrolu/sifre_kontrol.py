
def şifre_kontrolü(şifre):

    uzunluk = len(şifre)
    büyük_harf = False
    küçük_harf = False
    rakam = False
    özel_karakter = False
    özel_karakterler = "!@#$%^&*()-_=+[]{}|;:',.<>?/~`"

    yüzde = 0
    kriterler = {
        "yeterli_uzunluk": 25,
        "büyük_harf": 15,
        "küçük_harf": 15,
        "rakam": 15,
        "özel_karakter": 15,
        "uzunluk_ekstra": 15
    }

    for karakter in şifre:
        if karakter.isupper():
            büyük_harf = True
        elif karakter.islower():
            küçük_harf = True
        elif karakter.isdigit():
            rakam = True
        elif karakter in özel_karakterler:
            özel_karakter = True

    if uzunluk >= 8:
        yüzde += kriterler["yeterli_uzunluk"]
    if büyük_harf:
        yüzde += kriterler["büyük_harf"]
    if küçük_harf:
        yüzde += kriterler["küçük_harf"]
    if rakam:
        yüzde += kriterler["rakam"]
    if özel_karakter:
        yüzde += kriterler["özel_karakter"]
    if uzunluk > 12:
        yüzde += kriterler["uzunluk_ekstra"]

    print(f"Şifrenizin güvenliği: {yüzde}%")

    if yüzde == 100:
        print("✅ Şifreniz çok güvenli")
    elif yüzde >= 75:
        print("✅ Şifreniz güvenli")
    elif yüzde >= 50:
        print("⚠️ Şifreniz orta derecede güvenli ⚠️")
    elif yüzde >= 25:
        print("⚠️ Şifreniz az güvenli ⚠️")
    else:
        print("❌ Şifreniz güvenli değil ❌")

        if uzunluk < 8:
            print("- En az 8 karakter uzunluğunda olmalı.")
        if not büyük_harf:
            print("- En az bir büyük harf içermeli.")
        if not küçük_harf:
            print("- En az bir küçük harf içermeli.")
        if not rakam:
            print("- En az bir rakam içermeli.")
        if not özel_karakter:
            print("- En az bir özel karakter içermeli.")

    return yüzde

şifre = input("Lütfen şifrenizi girin: ")
şifre_kontrolü(şifre)
