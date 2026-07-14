def mandelbrot_fraktali_ciz():
    # Terminal boyutlarına göre resmi ayarlıyoruz
    genislik = 80
    yukseklik = 35
    maks_iterasyon = 30
    
    # İterasyon derinliğine göre pikselleri temsil edecek karakterler
    # (Boşluktan en yoğun karaktere doğru sıralı)
    karakterler = " .:-=+*#%@"
    
    print("🌀 Mehmet'in Matematiksel Mandelbrot Fraktalı 🌀")
    print("=" * 80)
    
    for y in range(yukseklik):
        satir = ""
        # Sanal eksen (Im) aralığı: -1.2 ile 1.2 arası
        sanal_kisim = (y / yukseklik) * 2.4 - 1.2
        
        for x in range(genislik):
            # Reel eksen (Re) aralığı: -2.0 ile 0.6 arası
            reel_kisim = (x / genislik) * 2.6 - 2.0
            
            # Kompleks sayımızı (c) tanımlıyoruz
            c = complex(reel_kisim, sanal_kisim)
            z = 0j
            iterasyon = 0
            
            # Ünlü kaos teorisi formülü: z = z^2 + c
            # Sayı sonsuza ıraksıyor mu (kaosa mı gidiyor) yoksa kümede kalıyor mu?
            while abs(z) <= 2 and iterasyon < maks_iterasyon:
                z = z**2 + c
                iterasyon += 1
            
            # İterasyon oranına göre karakter seçip satıra ekliyoruz
            karakter_indeksi = int((iterasyon / maks_iterasyon) * (len(karakterler) - 1))
            satir += karakterler[karakter_indeksi]
            
        print(satir)
        
    print("=" * 80)
    print("📊 Formül: $z_{n+1} = z_n^2 + c$ | Kompleks Düzlemde Kaos Analizi")

# Programı çalıştır
if __name__ == "__main__":
    mandelbrot_fraktali_ciz()