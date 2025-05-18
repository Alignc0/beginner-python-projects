
import tkinter as tk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

class MilyonerOyunu:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.title("Kim Milyoner Olmak İster")
        self.pencere.geometry("900x700")
        self.pencere.configure(bg="#0A1128")

        self.hosgeldin_frame = tk.Frame(self.pencere, bg="#0A1128")
        self.hosgeldin_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.baslik_label = tk.Label(
            self.hosgeldin_frame,
            text="KİM MİLYONER\nOLMAK İSTER?",
            font=("Georgia", 40, "bold"),
            bg="#0A1128",
            fg="#FFD700"
        )
        self.baslik_label.pack(pady=(0, 20))

        self.hosgeldin_label = tk.Label(
            self.hosgeldin_frame,
            text="Hazırsanız başlayalım!",
            font=("Georgia", 22),
            bg="#0A1128",
            fg="white"
        )
        self.hosgeldin_label.pack(pady=(0, 20))

        self.basla_btn = tk.Button(
            self.hosgeldin_frame,
            text="OYUNA BAŞLA",
            command=self.oyunu_baslat,
            font=("Georgia", 18, "bold"),
            bg="#1D3557",
            fg="white",
            activebackground="#457B9D",
            width=20,
            height=2,
            bd=0,
            relief="flat"
        )
        self.basla_btn.pack(pady=20)

        self.oyun_frame = tk.Frame(self.pencere, bg="#0A1128")

        # Süre göstergesi için Canvas ekleyelim
        self.sure_canvas = tk.Canvas(self.oyun_frame, width=300, height=50, bg="#0A1128", highlightthickness=0)
        self.sure_canvas.pack(pady=(10, 0))
        
        # Süre metni
        self.sure_text = self.sure_canvas.create_text(150, 25, text="Süre: 15", font=("Georgia", 16, "bold"), fill="white")
        
        # Süre çubuğu
        self.sure_cubugu = self.sure_canvas.create_rectangle(10, 40, 290, 50, fill="#457B9D")

        self.soru_label = tk.Label(
            self.oyun_frame,
            text="",
            font=("Georgia", 20, "bold"),
            bg="#0A1128",
            fg="white",
            wraplength=800,
            justify="center",
            pady=30
        )
        self.soru_label.pack(pady=10)

        self.buton_frame = tk.Frame(self.oyun_frame, bg="#0A1128")
        self.buton_frame.pack()

        self.butonlar = []
        for i in range(4):
            btn = tk.Button(
                self.buton_frame,
                text="",
                font=("Georgia", 14),
                width=35,
                height=2,
                wraplength=300,
                bg="#1D3557",
                fg="white",
                activebackground="#2A9D8F",
                relief="groove",
                command=lambda x=i: self.cevap_kontrol(x)
            )
            btn.grid(row=i//2, column=i%2, padx=20, pady=10)
            self.butonlar.append(btn)

        self.joker_frame = tk.Frame(self.oyun_frame, bg="#0A1128")
        self.joker_frame.pack(pady=20)

        self.elli_joker_btn = tk.Button(
            self.joker_frame, text="50:50", command=self.elli_joker_kullan,
            bg="#457B9D", fg="white", font=("Georgia", 12), width=10
        )
        self.elli_joker_btn.grid(row=0, column=0, padx=10)

        self.seyirci_joker_btn = tk.Button(
            self.joker_frame, text="Seyirci", command=self.seyirci_joker_kullan,
            bg="#457B9D", fg="white", font=("Georgia", 12), width=10
        )
        self.seyirci_joker_btn.grid(row=0, column=1, padx=10)

        self.telefon_joker_btn = tk.Button(
            self.joker_frame, text="Telefon", command=self.telefon_joker_kullan,
            bg="#457B9D", fg="white", font=("Georgia", 12), width=10
        )
        self.telefon_joker_btn.grid(row=0, column=2, padx=10)

        self.para_label = tk.Label(
            self.oyun_frame,
            text="Para: 0 TL",
            font=("Georgia", 14, "bold"),
            bg="#0A1128",
            fg="#FFD700"
        )
        self.para_label.pack(pady=10)
        
        # Süre ile ilgili değişkenler
        self.kalan_sure = 15
        self.timer_id = None
        self.sure_devam_ediyor = False

    def elli_joker_kullan(self):
        if not hasattr(self, 'sorular') or not hasattr(self, 'soru_indeks'):
            messagebox.showwarning("Uyarı", "Soru verileri eksik!")
            return

        # Joker zaten kullanıldıysa uyarı ver
        if not self.elli_joker_btn["state"] == "normal":
            messagebox.showwarning("Uyarı", "Bu jokeri zaten kullandınız!")
            return

        dogru_cevap = self.sorular[self.soru_indeks]["cevap"]
        secenekler = ["A", "B", "C", "D"]
        secenekler.remove(dogru_cevap)
        gizlenecekler = random.sample(secenekler, 2)

        for harf in gizlenecekler:
            idx = ord(harf) - ord("A")
            self.butonlar[idx].config(state="disabled")

        # Jokeri devre dışı bırak
        self.elli_joker_btn.config(state="disabled")

    def seyirci_joker_kullan(self):
        if not hasattr(self, 'sorular') or not hasattr(self, 'soru_indeks'):
            messagebox.showwarning("Uyarı", "Soru verileri eksik!")
            return

        # Joker zaten kullanıldıysa uyarı ver
        if not self.seyirci_joker_btn["state"] == "normal":
            messagebox.showwarning("Uyarı", "Bu jokeri zaten kullandınız!")
            return

        dogru_cevap = self.sorular[self.soru_indeks]["cevap"]
        dagilim = [10, 10, 10, 10]
        dogru_idx = ord(dogru_cevap) - ord("A")
        dagilim[dogru_idx] = 70
        kalan = 30
        for i in range(4):
            if i != dogru_idx:
                dagilim[i] += kalan // 3

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(["A", "B", "C", "D"], dagilim, color=["#FF6347", "#FFD700", "#32CD32", "#1E90FF"])
        ax.set_title("Seyirci Oylaması", fontsize=16, fontweight="bold", color="#333333")
        ax.set_ylabel("%", fontsize=12, fontweight="bold", color="#333333")
        ax.set_xlabel("Seçenekler", fontsize=12, fontweight="bold", color="#333333")

        for i, v in enumerate(dagilim):
            ax.text(i, v + 2, f"{v}%", ha='center', va='bottom', fontsize=10, color="#333333", fontweight="bold")

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_linewidth(1.5)
        ax.spines['bottom'].set_linewidth(1.5)
        ax.spines['left'].set_color("#333333")
        ax.spines['bottom'].set_color("#333333")
        ax.set_facecolor("#F0F0F0")
        ax.grid(True, which='both', axis='y', linestyle='--', color='gray', alpha=0.5)

        pencere2 = tk.Toplevel(self.pencere)
        pencere2.title("Seyirci Oylaması")
        canvas = FigureCanvasTkAgg(fig, master=pencere2)
        canvas.draw()
        canvas.get_tk_widget().pack(padx=20, pady=20)

        # Jokeri devre dışı bırak
        self.seyirci_joker_btn.config(state="disabled")

    def telefon_joker_kullan(self):
        if not hasattr(self, 'sorular') or not hasattr(self, 'soru_indeks'):
            messagebox.showwarning("Uyarı", "Soru verileri eksik!")
            return

        # Joker zaten kullanıldıysa uyarı ver
        if not self.telefon_joker_btn["state"] == "normal":
            messagebox.showwarning("Uyarı", "Bu jokeri zaten kullandınız!")
            return

        dogru_cevap = self.sorular[self.soru_indeks]["cevap"]
        mesaj = f"Bence doğru cevap '{dogru_cevap}', ama emin değilim."
        messagebox.showinfo("Telefon Jokeri", mesaj)

        # Jokeri devre dışı bırak
        self.telefon_joker_btn.config(state="disabled")

    def soru_goster(self):
        if self.soru_indeks >= len(self.sorular):
            messagebox.showinfo("Tebrikler!", f"Tüm soruları bildiniz!\nKazandığınız para: {self.kazanc} TL")
            self.oyun_bitti()
            return

        soru = self.sorular[self.soru_indeks]
        self.soru_label.config(text=soru["soru"])
        secenekler = soru["secenekler"]
        for i in range(4):
            self.butonlar[i].config(text=f"{chr(65+i)}: {secenekler[i]}", state="normal", bg="#1D3557")
        
        # Süreyi başlat
        self.kalan_sure = 15
        self.sure_cubugu_guncelle()
        self.sure_baslat()

    def sure_baslat(self):
        self.sure_devam_ediyor = True
        self.sure_say()
    
    def sure_durdur(self):
        self.sure_devam_ediyor = False
        if self.timer_id:
            self.pencere.after_cancel(self.timer_id)
            self.timer_id = None
    
    def sure_say(self):
        if not self.sure_devam_ediyor:
            return
            
        self.sure_canvas.itemconfig(self.sure_text, text=f"Süre: {self.kalan_sure}")
        
        # Süre çubuğunu güncelle
        self.sure_cubugu_guncelle()
        
        if self.kalan_sure <= 0:
            self.sure_bitti()
            return
            
        self.kalan_sure -= 1
        self.timer_id = self.pencere.after(1000, self.sure_say)

    def sure_cubugu_guncelle(self):
        # Süre çubuğunun uzunluğunu güncelle
        cubuk_uzunluk = 280 * (self.kalan_sure / 15)
        self.sure_canvas.coords(self.sure_cubugu, 10, 40, 10 + cubuk_uzunluk, 50)
        
        # Son 5 saniyede renk değişimi
        if self.kalan_sure <= 5:
            if self.kalan_sure % 2 == 0:
                renk = "#FF0000"  # Kırmızı
            else:
                renk = "#FF6347"  # Turuncu
        else:
            renk = "#457B9D"  # Normal renk
            
        self.sure_canvas.itemconfig(self.sure_cubugu, fill=renk)

    def sure_bitti(self):
        self.sure_durdur()
        messagebox.showinfo("Süre Bitti", "Süre doldu! Kaybettiniz.")
        self.oyun_bitti()

    def cevap_kontrol(self, secilen_idx):
        # Süreyi durdur
        self.sure_durdur()
        
        secilen_harf = chr(65 + secilen_idx)
        dogru_cevap = self.sorular[self.soru_indeks]["cevap"]

        if secilen_harf == dogru_cevap:
            self.kazanc += self.oduller[self.soru_indeks]
            self.para_label.config(text=f"Para: {self.kazanc} TL")
            self.butonlar[secilen_idx].config(bg="green")
            self.soru_indeks += 1
            self.after_delay(self.soru_goster)
        else:
            self.butonlar[secilen_idx].config(bg="red")
            for i, btn in enumerate(self.butonlar):
                if chr(65 + i) == dogru_cevap:
                    btn.config(bg="green")
            self.after_delay(self.oyun_bitti)

    def after_delay(self, func):
        self.pencere.after(2000, func)

    def oyun_bitti(self):
        # Süreyi durdur (eğer hala çalışıyorsa)
        self.sure_durdur()
        
        cevap = messagebox.askyesno("Oyun Bitti", f"Kazandığınız para: {self.kazanc} TL\nTekrar oynamak ister misiniz?")
        if cevap:
            self.oyunu_baslat()
        else:
            self.pencere.destroy()

    def oyunu_baslat(self):
        kolay_sorular = [
            {"soru": "Türkiye'nin başkenti neresidir?", "secenekler": ["İstanbul", "Ankara", "İzmir", "Bursa"], "cevap": "B"},
            {"soru": "Python hangi tür bir programlama dilidir?", "secenekler": ["Derleyici", "Yorumlayıcı", "Makine", "Donanım"], "cevap": "B"},
            {"soru": "En uzun nehir hangisidir?", "secenekler": ["Amazon", "Nil", "Yangtze", "Mississippi"], "cevap": "B"},
            {"soru": "Atatürk hangi yıl doğmuştur?", "secenekler": ["1881", "1923", "1938", "1919"], "cevap": "A"},
            {"soru": "Türkiye'nin en kalabalık şehri hangisidir?", "secenekler": ["Ankara", "İzmir", "İstanbul", "Antalya"], "cevap": "C"},
            {"soru": "Bir haftada kaç gün vardır?", "secenekler": ["5", "6", "7", "8"], "cevap": "C"},
            {"soru": "Su kaç derecede donar?", "secenekler": ["0", "100", "-10", "50"], "cevap": "A"},
            {"soru": "En küçük asal sayı kaçtır?", "secenekler": ["0", "1", "2", "3"], "cevap": "C"},
            {"soru": "Ay hangi gezegenin uydusudur?", "secenekler": ["Mars", "Venüs", "Dünya", "Jüpiter"], "cevap": "C"},
            {"soru": "İstanbul hangi iki kıta arasında yer alır?", "secenekler": ["Asya ve Avrupa", "Asya ve Afrika", "Avrupa ve Amerika", "Afrika ve Avrupa"], "cevap": "A"}
        ]
        orta_sorular = [
            {"soru": "Güneş sistemindeki en büyük gezegen hangisidir?", "secenekler": ["Mars", "Venüs", "Jüpiter", "Satürn"], "cevap": "C"},
            {"soru": "DNA'nın açılımı nedir?", "secenekler": ["Deoksiribonükleik Asit", "Dinamik Nöron Ağı", "Doğal Nükleotid Alanı", "Direkt Nükleotid Asidi"], "cevap": "A"},
            {"soru": "İngiltere'nin para birimi nedir?", "secenekler": ["Euro", "Dolar", "Sterlin", "Frank"], "cevap": "C"},
            {"soru": "HTML neyin kısaltmasıdır?", "secenekler": ["HighText Machine Language", "HyperText Markup Language", "HyperTool Multi Language", "HyperText Multiple Language"], "cevap": "B"},
            {"soru": "Einstein'ın ünlü denklemi nedir?", "secenekler": ["F=ma", "E=mc^2", "V=IR", "a^2 + b^2 = c^2"], "cevap": "B"},
            {"soru": "Türkiye kaç coğrafi bölgeden oluşur?", "secenekler": ["6", "7", "8", "9"], "cevap": "B"},
            {"soru": "Osmanlı Devleti'nin ilk padişahı kimdir?", "secenekler": ["Yavuz Sultan Selim", "Kanuni", "Osman Gazi", "Orhan Gazi"], "cevap": "C"},
            {"soru": "Ankara hangi bölgede yer alır?", "secenekler": ["Ege", "Marmara", "Karadeniz", "İç Anadolu"], "cevap": "D"},
            {"soru": "Barometre neyi ölçer?", "secenekler": ["Nem", "Basınç", "Sıcaklık", "Rüzgar"], "cevap": "B"},
            {"soru": "Hücre bölünmesi sırasında DNA'nın kopyalanmasına ne ad verilir?", "secenekler": ["Transkripsiyon", "Replikasyon", "Mutasyon", "Evrim"], "cevap": "B"}
        ]
        zor_sorular = [
            {"soru": "Kuantum fiziğinin babası kim olarak bilinir?", "secenekler": ["Einstein", "Max Planck", "Bohr", "Heisenberg"], "cevap": "B"},
            {"soru": "Hangisi asal sayı değildir?", "secenekler": ["2", "3", "5", "9"], "cevap": "D"},
            {"soru": "Hangi element simgesi doğrudur?", "secenekler": ["Oksijen - Ox", "Hidrojen - H", "Karbon - Ca", "Azot - At"], "cevap": "B"},
            {"soru": "Linux'un çekirdeğini kim geliştirmiştir?", "secenekler": ["Bill Gates", "Linus Torvalds", "Steve Jobs", "Dennis Ritchie"], "cevap": "B"},
            {"soru": "Higgs Bozonu başka hangi isimle bilinir?", "secenekler": ["Kara Delik", "Tanrı Parçacığı", "Atom Altı Tanecik", "Nötron"], "cevap": "B"},
            {"soru": "Osmanlı Devleti'nin kurulduğu yıl hangisidir?", "secenekler": ["1071", "1453", "1299", "1923"], "cevap": "C"},
            {"soru": "Einstein Nobel ödülünü hangi alanda almıştır?", "secenekler": ["Görelilik", "Fotoelektrik Etki", "Kuantum", "Kütle Çekim"], "cevap": "B"},
            {"soru": "Plank sabiti sembolü nedir?", "secenekler": ["c", "λ", "h", "e"], "cevap": "C"},
            {"soru": "Python'da bellek yönetimini kim yapar?", "secenekler": ["Yorumlayıcı", "Çekirdek", "Garbage Collector", "Kernel"], "cevap": "C"},
            {"soru": "Yüz ölçümü en büyük ülke hangisidir?", "secenekler": ["Kanada", "Çin", "ABD", "Rusya"], "cevap": "D"}
        ]

        # Soruları karıştır ve seç
        secilen_sorular = random.sample(kolay_sorular, 4) + random.sample(orta_sorular, 4) + random.sample(zor_sorular, 4)

        self.sorular = secilen_sorular
        self.oduller = [1000, 2000, 3000, 5000, 7000, 10000, 15000, 25000, 50000, 100000, 250000, 1000000]
        self.soru_indeks = 0
        self.kazanc = 0

        self.hosgeldin_frame.place_forget()
        self.oyun_frame.pack(pady=20)
        self.soru_goster()

if __name__ == "__main__":
    oyun = MilyonerOyunu()
    oyun.pencere.mainloop()