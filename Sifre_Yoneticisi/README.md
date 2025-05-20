# Şifre Yöneticisi 🔐

Bu proje, kullanıcıların farklı platformlara ait kullanıcı adı ve şifrelerini yerel dosyada saklayabildiği basit bir şifre yönetimi uygulamasıdır.

## Özellikler
- Yeni platform/kullanıcı/şifre kaydı ekleyebilme
- Kayıtları yıldızlı veya açık şekilde listeleme
- `sifreler.txt` dosyasına veri yazma ve okuma
- Kullanıcı dostu menü ile terminal arayüzü

## Kullanım
```bash
python sifre_yoneticisi.py
```

## Uyarı
> Bu uygulama **şifreleri düz metin olarak saklar**. Gerçek bir uygulamada `hash`, `şifreleme`, `şifreli veritabanı` gibi güvenlik önlemleri gereklidir.

---

Bu proje, dosya işlemleri (`open`, `write`, `readlines`), kullanıcı girişi (`input`), ve listeleme gibi temel Python becerilerini geliştirmek amacıyla yapılmıştır.
