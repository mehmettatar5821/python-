def hesapla():
    print("--- Python Hesap Makinesi ---")
    print("İşlemler: +, -, *, /")

    # Kullanıcıdan sayı al
    try:
        sayi1 = float(input("Birinci sayıyı girin: "))
        islem = input("Yapmak istediğiniz işlemi seçin (+, -, *, /): ")
        sayi2 = float(input("İkinci sayıyı girin: "))

        # İşlem kontrolü
        if islem == "+":
            sonuc = sayi1 + sayi2
            print(f"Sonuç: {sayi1} + {sayi2} = {sonuc}")
        elif islem == "-":
            sonuc = sayi1 - sayi2
            print(f"Sonuç: {sayi1} - {sayi2} = {sonuc}")
        elif islem == "*":
            sonuc = sayi1 * sayi2
            print(f"Sonuç: {sayi1} * {sayi2} = {sonuc}")
        elif islem == "/":
            # Sıfıra bölünme hatasını kontrol edelim
            if sayi2 != 0:
                sonuc = sayi1 / sayi2
                print(f"Sonuç: {sayi1} / {sayi2} = {sonuc}")
            else:
                print("Hata: Bir sayı sıfıra bölünemez!")
        else:
            print("Geçersiz bir işlem girdiniz.")
            
    except ValueError:
        print("Hata: Lütfen geçerli bir sayı girin!")

hesapla()