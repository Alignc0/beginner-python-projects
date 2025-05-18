# kELİME FREKANSI HESAPLAMA
""""""""""""""""""""""""""""""""
## Bu program, kullanıcının girdiği metindeki kelimelerin frekansını hesaplar.
## Kullanıcıdan metin alır ve her kelimenin kaç kez geçtiğini sayar.
## Sonuçları bir sözlükte saklar ve ekrana yazdırır.

def word_frequency(text):
    test = text.lower()
    text = "".join(char if char.isalnum() else " " for char in test)
    words = text.split()

    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    return frequency_dict

input_text = input("bir metin giriniz: ")
result = word_frequency(input_text)
print("\nkelime frekansları:")
for word, frequency in result.items():
    print(f"{word}: {frequency} kez")