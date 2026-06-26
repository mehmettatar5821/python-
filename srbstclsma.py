def konvolusyon_filtresi_uygula(resim, filtre):
    print("📸 Orijinal Piksel Matrisi (Gürültülü/Düz):")
    print("----------------------------------------")
    for satir in resim:
        print(" ".join(f"{p:3}" for p in satir))
    print("----------------------------------------")
    
    # Resim boyutlarını alıyoruz
    satir_sayisi = len(resim)
    sutun_sayisi = len(resim[0])
    
    # Filtrelenmiş yeni resim için boş matris (Kenarlardan 1 piksel kırpılacak)
    yeni_resim = [[0 for _ in range(sutun_sayisi - 2)] for _ in range(satir_sayisi - 2)]
    
    # 🧠 MATRİS GEZDİRME ALGORİTMASI
    # Filtreyi resmin üzerinde 1'er piksel kaydırarak gezdiriyoruz
    for i in range(satir_sayisi - 2):
        for j in range(sutun_sayisi - 2):
            
            toplam = 0
            # 3x3'lük bölgeyi filtre matrisi ile karşılıklı çarpıyoruz
            for fi in range(3):
                for fj in range(3):
                    piksel_degeri = resim[i + fi][j + fj]
                    filtre_degeri = filtre[fi][fj]
                    toplam += piksel_degeri * filtre_degeri
            
            # Sınır kontrolü (Piksel değerleri 0-255 arasında kalmalı)
            yeni_resim[i][j] = max(0, min(255, toplam))
            
    return yeni_resim

# --- PROGRAMI TEST EDELİM ---

# 5x5 boyutunda gri tonlamalı sahte bir resim matrisi (Pikseller 0-255 arası)
# Ortada (100 yazan yerde) hafif bir detay/kenar var
orijinal_resim = [
    [10, 10, 10,  10, 10],
    [10, 10, 10,  10, 10],
    [10, 10, 100, 10, 10],
    [10, 10, 10,  10, 10],
    [10, 10, 10,  10, 10]
]

# Yapay zekada ve görüntü işlemede meşhur "Keskinleştirme" (Sharpen) matrisi:
keskinlestirme_filtresi = [
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
]

sonuc = konvolusyon_filtresi_uygula(orijinal_resim, keskinlestirme_filtresi)

print("✨ Filtre Sonrası Keskinleşmiş Matris (Detaylar Patladı):")
print("----------------------------------------")
for satir in sonuc:
    print(" ".join(f"{p:3}" for p in satir))
print("----------------------------------------")
print("🎯 Farkı gördün mü kral? Ortadaki 100 değeri çevreye göre dehşet vurgulandı (255 oldu)!")