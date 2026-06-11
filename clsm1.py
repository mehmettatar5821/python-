def resmi_aynala(resim_matrisi):
    print("📸 Orijinal Mehmet Resmi (Piksel Matrisi):")
    print("----------------------------------------")
    for satir in resim_matrisi:
        print(" ".join(satir))
    print("----------------------------------------")
    
    # Yeni boş bir matris oluşturuyoruz (Aynalanmış hali için)
    aynalanmis_resim = []
    
    # 🧠 Algoritma: Her satırı alıp sondan başa doğru (tersine) sıralıyoruz.
    # Matris dilinde: matris[i][j] elemanını matris[i][son_sutun - j] yapıyoruz.
    for satir in resim_matrisi:
        # Python'daki [::-1] listeyi tersine çevirmenin en hızlı yoludur
        ters_satir = satir[::-1]
        aynalanmis_resim.append(ters_satir)
        
    return aynalanmis_resim

# --- PROGRAMI TEST EDELİM ---

# 5x5 boyutunda bir "Mehmet" resmi matrisi tanımlayalım.
# Pikseller yerine karakterler kullanalım ki ekranda ne olduğunu görebilelim.
# Bu matris sol tarafa doğru bakan bir ok işaretini ( < ) temsil ediyor:
orijinal_piksel_matrisi = [
    [".", ".", "#", ".", "."],
    [".", "#", ".", ".", "."],
    ["#", ".", ".", ".", "."],
    [".", "#", ".", ".", "."],
    [".", ".", "#", ".", "."]
]

sonuc_matrisi = resmi_aynala(orijinal_piksel_matrisi)

print("🪞 Aynalanmış Resim (Yeni Piksel Matrisi):")
print("----------------------------------------")
for satir in sonuc_matrisi:
    print(" ".join(satir))
print("----------------------------------------")
print("🎉 Gördün mü kral? Sola bakan ok ( < ) şak diye sağa ( > ) döndü!")