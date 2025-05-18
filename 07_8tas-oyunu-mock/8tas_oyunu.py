

from random import choice

cevaplar = ("Evet","Hayır","Kesinlikle olmaz","Buna bende emin değilim","Cevabı sende","İmkansız","...")
acımasız = ["Kesinlikle olmaz","İmkansız"]
normal = ["Evet","Hayır","Buna bende emin değilim","Cevabı sende","..."]
cevap_tipi = input("Cevabım acımasız mı olsun normal mi?: ").strip().lower()

if cevap_tipi == "acımasız":
    cevap = choice(acımasız)
elif cevap_tipi == "normal":
    cevap = choice(normal)
else:
    cevap = choice(cevaplar)

input("Hadi sor bakalım?: ")

print("Cevabım: ", cevap)

