
def menu_göster():
    print("---- To-Do Listesi ----")
    print("1. Görev Ekle")
    print("2. Görevleri Görüntüle")
    print("3. Görev Sil")
    print("4. Çıkış")

görevler = []

def görevleri_yükle():
    try:
        with open("todo.txt", "r", encoding="utf-8") as dosya:
            for satır in dosya:
                görevler.append(satır.strip())
    except FileNotFoundError:
        pass  # Dosya yoksa sorun değil, yeni oluşturulur.

def görevleri_kaydet():
    with open("todo.txt", "w", encoding="utf-8") as dosya:
        for görev in görevler:
            dosya.write(görev + "\n")

def görev_ekle():
    görev = input("Eklenecek görevi girin: ")
    görevler.append(görev)
    görevleri_kaydet()
    print("Görev eklendi ve kaydedildi.")

def görevleri_göster():
    if not görevler:
        print("Görev listesi boş.")
    else:
        for i, görev in enumerate(görevler, 1):
            print(f"{i}. {görev}")

def görev_sil():
    görevleri_göster()
    try:
        silinecek = int(input("Silinecek görevin numarasını girin: "))
        if 1 <= silinecek <= len(görevler):
            silinen = görevler.pop(silinecek - 1)
            görevleri_kaydet()
            print(f"{silinen} görevi silindi ve dosya güncellendi.")
        else:
            print("Geçersiz görev numarası.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

def uygulama():
    görevleri_yükle()
    while True:
        menu_göster()
        secim = input("Lütfen bir seçenek girin (1/2/3/4): ")

        if secim == '1':
            görev_ekle()
        elif secim == '2':
            görevleri_göster()
        elif secim == '3':
            görev_sil()
        elif secim == '4':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

uygulama()
