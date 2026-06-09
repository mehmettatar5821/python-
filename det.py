def matris_tersini_al(matris):
    # Matrisin elemanlarını formüldeki harflere atıyoruz
    # [[a, b],
    #  [c, d]]
    a = matris[0][0]
    b = matris[0][1]
    c = matris[1][0]
    d = matris[1][1]
    
    # 1. Adım: Determinant hesapla (a*d - b*c)
    determinant = (a * d) - (b * c)
    
    print(f"📊 Girilen Matris: {matris}")
    print(f"📐 Matrisin Determinantı: {determinant}")
    print("----------------------------------------")
    
    # Güvenlik Kontrolü: Determinant 0 ise tersi yoktur!
    if determinant == 0:
        print("❌ HATA: Bu matrisin determinantı 0 olduğu için TERSİ YOKTUR kanka!")
        return None
        
    # 2. Adım: Formülü uygula ve elemanları yeni yerlerine yerleştir
    # Ana köşegen (a ve d) yer değiştirir. Diğerleri (-b ve -c) işaret değiştirir.
    # Her eleman 1 / determinant ile çarpılır (yani determinanta bölünür).
    ters_matris = [
        [d / determinant, -b / determinant],
        [-c / determinant, a / determinant]
    ]
    
    return ters_matris

# --- PROGRAMI TEST EDELİM ---

# Örnek 1: Tersi olan bir matris (Yukarıda elle çözdüğümüz matris)
matris_A = [
    [1, 2],
    [3, 4]
]

sonuc = matris_tersini_al(matris_A)

if sonuc:
    print("🔑 Mehmet için Hesaplanan Ters Matris:")
    for satir in sonuc:
        print(satir)
        
print("\n" + "="*40 + "\n")

# Örnek 2: Tersi OLMAYAN bir matris deneyelim (Determinantı 0 çıkacak)
matris_B = [
    [2, 4],
    [1, 2]  # (2*2) - (4*1) = 4 - 4 = 0
]

matris_tersini_al(matris_B)