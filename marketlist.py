def liste_uygulamasi():
    alisveris_listesi = []
    
    print("--- Alışveriş Listesi Programına Hoş Geldin ---")
    
    while True:
        print("\n1. Listeyi Görüntüle")
        print("2. Listeye Ürün Ekle")
        print("3. Listeyi Temizle")
        print("4. Çıkış")
        
        secim = input("Yapmak istediğiniz işlemin numarasını seçin: ")
        
        if secim == "1":
            if not alisveris_listesi:
                print("\nListeniz şu an boş.")
            else:
                print("\n--- Güncel Listeniz ---")
                for sira, urun in enumerate(alisveris_listesi, 1):
                    print(f"{sira}. {urun}")
                    
        elif secim == "2":
            yeni_urun = input("Eklemek istediğiniz ürünü yazın: ")
            alisveris_listesi.append(yeni_urun)
            print(f"'{yeni_urun}' listeye eklendi.")
            
        elif secim == "3":
            alisveris_listesi.clear()
            print("Liste tamamen temizlendi.")
            
        elif secim == "4":
            print("Programdan çıkılıyor, iyi günler!")
            break
            
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

# Programı başlat
liste_uygulamasi()