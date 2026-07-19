def en_kisa_yolu_bul(graf, baslangic, hedef):
    # Tüm düğümlere olan mesafeleri başlangıçta sonsuz yapıyoruz
    sonsuz = float('inf')
    mesafeler = {dugum: sonsuz for dugum in graf}
    mesafeler[baslangic] = 0
    
    # Rotayı geri takip edebilmek için öncül düğümleri tutan sözlük
    öncekiler = {dugum: None for dugum in graf}
    
    # Gezilecek düğümlerin listesi
    ziyaret_edilmemis = list(graf.keys())
    
    while ziyaret_edilmemis:
        # Ziyaret edilmemiş düğümler arasından mesafesi en küçük olanı seçiyoruz
        mevcut_dugum = min(ziyaret_edilmemis, key=lambda dugum: mesafeler[dugum])
        
        # Eğer hedef düğüme ulaştıysak veya en yakın düğüm sonsuzsa döngüden çık
        if mevcut_dugum == hedef or mesafeler[mevcut_dugum] == sonsuz:
            break
            
        ziyaret_edilmemis.remove(mevcut_dugum)
        
        # Mevcut düğümün komşularını kontrol ediyoruz
        for komsu, mesafe in graf[mevcut_dugum].items():
            alternatif_rota = mesafeler[mevcut_dugum] + mesafe
            
            # Eğer daha kısa bir yol bulduysak mesafeyi güncelliyoruz
            if alternatif_rota < mesafeler[komsu]:
                mesafeler[komsu] = alternatif_rota
                öncekiler[komsu] = mevcut_dugum
                
    # 🧠 ROTAYI OLUŞTURMA ALGORİTMASI
    # Hedef düğümden geriye doğru giderek rotayı çıkartıyoruz
    rota = []
    mevcut = hedef
    while öncekiler[mevcut] is not None:
        rota.insert(0, mevcut)
        mevcut = öncekiler[mevcut]
    if rota:
        rota.insert(0, baslangic)
        
    return mesafeler[hedef], rota

# --- PROGRAMI TEST EDELİM ---

# Mehmet'in Şehirler Arası Ağı (Graf Yapısı)
# Şehirler birbirine yollarla bağlı ve üzerindeki sayılar kilometreleri temsil ediyor
sehir_agi = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 1, 'D': 5},
    'C': {'B': 1, 'D': 8, 'E': 10},
    'D': {'E': 2},
    'E': {}
}

baslangic_sehri = 'A'
hedef_sehir = 'E'

en_kisa_mesafe, ideal_rota = en_kisa_yolu_bul(sehir_agi, baslangic_sehri, hedef_sehir)

print("🗺️ Mehmet'in Akıllı Rota Hesaplayıcısı 🗺️")
print("=" * 45)
print(f"🚀 Başlangıç: {baslangic_sehri} -> 🎯 Hedef: {hedef_sehir}")
print("-" * 45)
print(f"📏 En Kısa Toplam Mesafe: {en_kisa_mesafe} KM")
print(f"📍 İzlenmesi Gereken En İdeal Rota: {' -> '.join(ideal_rota)}")
print("=" * 45)