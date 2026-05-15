def doviz_hesapla():
    print("--- DOVIZ HESAPLAYICI ---")
     
    # Gercek projelerde bunlar internetten cekilir
    dolar_kuru = 34.50
    euro_kuru = 37.20
    
    try:
        tl_miktari = float(input("Cevirmek istediginiz TL miktarini girin: "))
        
        dolar_sonuc = tl_miktari / dolar_kuru
        euro_sonuc = tl_miktari / euro_kuru
        
        print("-" * 30)
        print(f"{tl_miktari:.2f} TL sunlari eder:")
        print(f"Dolar: {dolar_sonuc:.2d} USD")
        print(f"Euro : {euro_sonuc:.2d} EUR")
        print("-" * 30)
        
    except ValueError:
        print("Lutfen sadece sayi giriniz!")

if __name__ == "__main__":
    doviz_hesapla()