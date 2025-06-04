
with open("günlük.txt", "a", encoding="utf-8") as dosya:
    while True:
        tarih_input = input("Lütfen tarihi (GG-AA-YYYY) şeklinde gir çıkmak için ise 'q' ile çık: ")
        if tarih_input.lower() == 'q':
            print("Günlük kaydı kapatılıyor...")
            break

        try:
            tarih = tarih_input 
            içerik = input("Bugün neler yaptın?\n ")
            dosya.write(f"({tarih})\n - {içerik}\n")
            print(f"{tarih} tarihli günlük kaydı eklendi.")
        except Exception as e:
            print(f"Hata oluştu: {e}")
