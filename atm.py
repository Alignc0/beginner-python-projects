
def atm():
    print("-" * 20 + " ATM Uygulaması " + "-" * 20)
    bakiye = 1000
    giriş_hakkı = 3

    while giriş_hakkı > 0:
        kullanıcı_adı = input("Kullanıcı adınızı giriniz: ")
        şifre = input("Şifrenizi giriniz: ")

        if kullanıcı_adı == "admin" and şifre == "1234":
            print("Giriş başarılı!")
            break
        else:
            giriş_hakkı -= 1
            print(f"Hatalı giriş. Kalan hakkınız: {giriş_hakkı}")
            if giriş_hakkı == 0:
                print("Giriş hakkınız kalmadı. Hesabınız kilitlendi.")
                return

    while True:
        print("\n--- İşlem Menüsü ---")
        print("1. Bakiye Sorgula")
        print("2. Para Yatırma")
        print("3. Para Çekme")
        print("4. Çıkış")
        işlem = input("İşlemi seçiniz (1-4): ")

        if işlem == "1":
            print(f"Bakiyeniz: {bakiye} TL")

        elif işlem == "2":
            miktar = int(input("Yatırmak istediğiniz miktarı giriniz: "))
            bakiye += miktar
            print(f"{miktar} TL yatırıldı. Yeni bakiyeniz: {bakiye} TL")

        elif işlem == "3":
            miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))
            if miktar > bakiye:
                print("Yetersiz bakiye!")
            else:
                bakiye -= miktar
                print(f"{miktar} TL çekildi. Yeni bakiyeniz: {bakiye} TL")

        elif işlem == "4":
            print("Çıkış yapılıyor. İyi günler!")
            break

        else:
            print("Geçersiz işlem seçimi!")

atm()
