import random
import string

def sifre_ureticisi():
    print("🔐 Güvenli Şifre Oluşturucuya Hoş Geldin!")
    print("----------------------------------------")
    
    # Kullanıcıdan şifre uzunluğunu alıyoruz
    try:
        uzunluk = int(input("Şifreniz kaç karakter uzunluğunda olsun? (Örn: 12): "))
    except ValueError:
        print("❌ Lütfen sadece sayı gir kanka!")
        return

    if uzunluk < 4:
        print("❌ Güvenlik için şifre en az 4 karakter olmalı!")
        return

    # Python'ın kendi içinde hazır olan karakter havuzlarını tanımlıyoruz
    kucuk_harfler = string.ascii_lowercase
    buyuk_harfler = string.ascii_uppercase
    sayilar = string.digits
    semboller = string.punctuation

    # Her karakter türünden en az bir tane şifrede bulunmasını garanti ediyoruz
    saf_sifre = [
        random.choice(kucuk_harfler),
        random.choice(buyuk_harfler),
        random.choice(sayilar),
        random.choice(semboller)
    ]

    # Geri kalan karakterleri tüm havuzu karıştırarak rastgele seçiyoruz
    tum_karakterler = kucuk_harfler + buyuk_harfler + sayilar + semboller
    for _ in range(uzunluk - 4):
        saf_sifre.append(random.choice(tum_karakterler))

    # Karakterlerin sırasını iyice karıştırıyoruz ki tahmin edilemesin
    random.shuffle(saf_sifre)

    # Listeyi birleştirip tek bir metin (string) haline getiriyoruz
    olusan_sifre = "".join(saf_sifre)

    print("----------------------------------------")
    print(f"🔑 Mehmet için oluşturulan şifre: {olusan_sifre}")
    print("----------------------------------------")

# Programı çalıştır
sifre_ureticisi()