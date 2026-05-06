import random

def oyun_baslat():
    # Bilgisayar 1 ile 100 arasında rastgele bir sayı seçer
    hedef_sayi = random.randint(1, 100)
    tahmin_hakki = 7
    
    print("--- Sayı Tahmin Oyununa Hoş Geldin! ---")
    print("1 ile 100 arasında bir sayı tuttum. 7 hakkın var.")

    while tahmin_hakki > 0:
        print(f"\nKalan tahmin hakkın: {tahmin_hakki}")
        
        try:
            tahmin = int(input("Tahminin nedir?: "))
        except ValueError:
            print("Lütfen sadece sayı gir!")
            continue

        if tahmin == hedef_sayi:
            print(f"Tebrikler! {hedef_sayi} sayısını doğru tahmin ettin! 🎉")
            break
        elif tahmin < hedef_sayi:
            print("Daha büyük bir sayı dene. ⬆️")
        else:
            print("Daha küçük bir sayı dene. ⬇️")
            
        tahmin_hakki -= 1

    if tahmin_hakki == 0:
        print(f"\nMaalesef hakkın bitti. Tuttuğum sayı: {hedef_sayi} idi. 😔")

# Oyunu çalıştır
oyun_baslat()