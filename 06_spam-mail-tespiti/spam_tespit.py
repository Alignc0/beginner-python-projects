import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.utils import resample

data = {
    "mail": [
        "Kazandınız hemen tıklayın", "Bugün toplantı var unutma", "Bedava fırsatlar sizi bekliyor",
        "Yarın derse gelmeyi unutma", "Banka borcunuzu sıfırlayın!!!", "Haftaya sınav var",
        "Bonus kazanın şimdi", "Çalışma grubu kuruyoruz katılır mısın", "Şans oyunlarıyla büyük ödüller 🙂",
        "Sunumu birlikte hazırlayalım", "Hesabınız askıya alındı, lütfen şifrenizi güncelleyin.",
        "Kredi kartı bilgilerinizi güncellemek için giriş yapın.",
        "Hesabınızda olağan dışı etkinlik tespit edildi.",
        "Banka bilgilerinizi kontrol edin.",
        "Hesap güvenliğiniz tehlikede, şifrenizi sıfırlayın.",
        "Hesabınızda şüpheli giriş tespit edildi.",
        "Banka hesabınızda olağan dışı hareket var.",
        "Hesabınız güvenlik nedeniyle kilitlendi.",
        "Şifre sıfırlama talebiniz başarıyla oluşturuldu.",
        "Giriş yaparak hesabınızı doğrulayın.",
        "Axess Kredi Kartı Hesap Özeti",
        "Apple Hesabı bilgileriniz güncellendi.",
        "Ali, başvurunuz MAKEL TEKNOLOJİ A.Ş. şirketine gönderildi.",
        "Güvenlik uyarısı: Okunmamış bir mesajınız var.",
        "Müşteri Bilgilendirme: Mesajınızı başarıyla aldık.",
        "Lütfen en kısa zamanda bizimle iletişime geçin.",
        "Axess Kredi Kartı Hesap Özeti: Yine ödeme yapmanız gerekebilir.",
        "Şirketimizdeki yeni duyuru hakkında bilgi almak için bağlantıya tıklayın.",
        "Toplantı saatiniz değişti, yeni saat: 14:00.",
        "Yarınki etkinlik hakkında bilgiler ve katılım linki.",
        "MAKEL TEKNOLOJİ A.Ş. yönetim ekibi olarak sizlere en iyi hizmeti sunmayı hedefliyoruz.",
        "Yeni bir güvenlik güncellemesi mevcut, lütfen giriş yaparak doğrulama yapın.",
        "Lütfen iş yerindeki formu doldurmayı unutmayın.",
        "Bugün saat 15:00'te önemli bir toplantı var.",
        "Yapmanız gereken bazı görevlerin listesini gönderdik.",
        "Haftalık raporunuzu eksiksiz olarak sisteme yüklemenizi rica ederiz.",
        "Hesabınızda güncellenmesi gereken bilgiler bulunmaktadır.",
        "Hesabınıza giriş yapmak için tıklayın.",
        "Yeni promosyonlarımızı ve kampanyalarımızı görmek için linke tıklayın.",
        "Lütfen geri dönüş yapmayı unutmayın.",
        "Yeni tekliflerimizle ilgili detaylı bilgi almak için tıklayın.",
        "Bugün için yapılacaklar listenizi kontrol ettiniz mi?",
        "Kazanç Seni Bekliyor!","Şans Kapında, Hemen Değerlendir!"
    ],
    "etiket": [
        1, 0, 1, 0, 1, 0, 1, 0, 1, 0,  # (0: Normal, 1: Spam)
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1,1
    ]
}

df = pd.DataFrame(data)


df_normal = df[df['etiket'] == 0]
df_spam = df[df['etiket'] == 1]


df_spam_upsampled = resample(df_spam,
                             replace=True,
                             n_samples=len(df_normal),
                             random_state=42)

df_balanced = pd.concat([df_normal, df_spam_upsampled])

x = df_balanced["mail"]
y = df_balanced["etiket"]

tfidf = TfidfVectorizer(stop_words=None, ngram_range=(1, 3), max_features=2000)
x_tfidf_balanced = tfidf.fit_transform(x)


x_train, x_test, y_train, y_test = train_test_split(x_tfidf_balanced, y, test_size=0.3, random_state=42)


model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)


y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("Model Doğruluk Oranı:", accuracy)

yeni_mail = input("Bir mail girin: ")
yeni_mail_tfidf = tfidf.transform([yeni_mail])
tahmin = model.predict(yeni_mail_tfidf)
if tahmin[0] == 1:
    print("Bu mail SPAM!")
else:
    print("Bu mail SPAM değil!")