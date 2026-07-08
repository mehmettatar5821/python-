def harf_to_sayi(harf):
    # 'A' harfini 0, 'B' harfini 1 ... yapıyoruz (İngiliz alfabesi mantığı)
    return ord(harf.upper()) - ord('A')

def sayi_to_harf(sayi):
    # Sayıyı tekrar harfe çeviriyoruz (26 harf üzerinden mod alarak)
    return chr((sayi % 26) + ord('A'))

def hill_sifrele(metin, anahtar_matris):
    print(f"📝 Orijinal Metin: {metin}")
    print(f"🔑 Anahtar Matris: {anahtar_matris}")
    print("----------------------------------------")
    
    # Metindeki harfleri sayılara çevirip 2'şerli gruplara (vektörlere) ayırıyoruz
    # Örnek: "MEHMET" -> [M,E], [H,M], [E,T] şeklinde matris vektörleri olacak
    vektorler = []
    for i in range(0, len(metin), 2):
        v = [harf_to_sayi(metin[i]), harf_to_sayi(metin[i+1])]
        vektorler.append(v)
        
    sifreli_metin = ""
    
    # 🧠 MATRİS ÇARPIMI İLE ŞİFRELEME ALGORİTMASI
    # Her bir 2x1'lik harf vektörünü, 2x2'lik anahtar matrisimizle çarpıyoruz
    for v in vektorler:
        # Yeni X = (A[0][0]*v[0] + A[0][1]*v[1]) % 26
        # Yeni Y = (A[1][0]*v[0] + A[1][1]*v[1]) % 26
        yeni_x = (anahtar_matris[0][0] * v[0] + anahtar_matris[0][1] * v[1]) % 26
        yeni_y = (anahtar_matris[1][0] * v[0] + anahtar_matris[1][1] * v[1]) % 26
        
        sifreli_metin += sayi_to_harf(yeni_x) + sayi_to_harf(yeni_y)
        
    return sifreli_metin

# --- PROGRAMI TEST EDELİM ---

# Şifrelenecek metin (Çift sayıda harf olmalı, o yüzden MEHMET tam uyuyor)
mesaj = "MEHMET"

# Rastgele seçilmiş, determinantı 0 olmayan ve tersi alınabilen gizli anahtar matrisimiz:
# [[3, 3],
#  [2, 5]]
gizli_anahtar = [
    [3, 3],
    [2, 5]
]

sonuc = hill_sifrele(mesaj, gizli_anahtar)

print(f"🔒 Mehmet İçin Oluşturulan Şifreli Metin: {sonuc}")
print("----------------------------------------")
print("💡 Bu şifreyi çözmek için, bu metni alıp 'anahtar matrisin tersi' ile çarpmak gerekir kanka!")