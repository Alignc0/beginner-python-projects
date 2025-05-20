
def hikaye_olusturucu():
    isim = input("Bir isim giriniz: ")
    yer = input("Bir yer giriniz: ")
    hayvan = input("Bir hayvan giriniz: ")
    renk = input("Bir renk giriniz: ")
    nesne = input("Bir nesne giriniz: ")
    meslek = input("Bir meslek giriniz: ")

    hikaye = (f"""Bir zamanlar {isim} adında bir çocuk {yer}'da yaşardı.  
    En sevdiği hayvan {renk} bir {hayvan}ydi.
    Bu {hayvan}yle her gün {nesne}sını alıp birlikte gezerlerdi.
    {isim}'nin hayali bir gün {meslek} olmaktı.
    Ve sonunda hayalini gerçekleştirdi!""")
    print(hikaye)

hikaye_olusturucu()
