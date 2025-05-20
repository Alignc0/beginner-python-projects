
import os

def sifre_yoneticisi():
    dosya_adi = "sifreler.txt"

    if not os.path.exists(dosya_adi):
        with open(dosya_adi, "w") as f:
            pass

    while True:
        print("\n--- Şifre Yöneticisi ---")
        print("1. Yeni kayıt ekle")
        print("2. Kayıtları listele (yıldızlı)")
        print("3. Kayıtları listele (şifreleri açık göster)")
        print("4. Çıkış yap")
        secim = input("Seçiminiz (1-4): ")

        if secim == "1":
            platform = input("Platform adı (örnek: Gmail): ")
            kullanici = input("Kullanıcı adınız: ")
            sifre = input("Şifreniz: ")

            with open(dosya_adi, "a") as f:
                f.write(f"{platform},{kullanici},{sifre}\n")

            print(f"{platform} için kayıt eklendi.")

        elif secim == "2" or secim == "3":
            print("\n--- Kayıtlar ---")
            try:
                with open(dosya_adi, "r") as f:
                    satirlar = f.readlines()
                    for satir in satirlar:
                        platform, kullanici, sifre = satir.strip().split(",")
                        if secim == "2":
                            gizli = "*" * len(sifre)
                            print(f"Platform: {platform}, Kullanıcı: {kullanici}, Şifre: {gizli}")
                        else:
                            print(f"Platform: {platform}, Kullanıcı: {kullanici}, Şifre: {sifre}")
            except FileNotFoundError:
                print("Kayıt bulunamadı.")

        elif secim == "4":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim!")

sifre_yoneticisi()
