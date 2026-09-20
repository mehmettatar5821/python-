"""
Matrix Operations & Linear System Solver (Pure Python)
- Matris Çarpımı
- Determinant Hesabı (Rekürsif / Laplace Açılımı)
- Gauss-Jordan Eliminasyonu ile Denklem Çözücü (Ax = b)
"""

def matris_yazdir(matris, baslik=""):
    if baslik:
        print(f"\n--- {baslik} ---")
    for satir in matris:
        print("[" + " ".join(f"{val:8.3f}" for val in satir) + "]")
    print()


def matris_carpimi(A, B):
    satir_A, sutun_A = len(A), len(A[0])
    satir_B, sutun_B = len(B), len(B[0])

    if sutun_A != satir_B:
        print("[!] Hata: A'nın sütun sayısı B'nin satır sayısına eşit olmalıdır!")
        return None

    sonuc = [[0.0 for _ in range(sutun_B)] for _ in range(satir_A)]
    for i in range(satir_A):
        for j in range(sutun_B):
            for k in range(sutun_A):
                sonuc[i][j] += A[i][k] * B[k][j]
    return sonuc


def alt_matris(matris, i, j):
    """Determinant için i. satır ve j. sütunu silip alt matrisi döndürür."""
    return [satir[:j] + satir[j+1:] for satir in (matris[:i] + matris[i+1:])]


def determinant(matris):
    n = len(matris)
    if n != len(matris[0]):
        print("[!] Hata: Matris kare olmalıdır!")
        return None

    if n == 1:
        return matris[0][0]
    if n == 2:
        return matris[0][0] * matris[1][1] - matris[0][1] * matris[1][0]

    det = 0
    for j in range(n):
        kofaktor = ((-1) ** j) * matris[0][j] * determinant(alt_matris(matris, 0, j))
        det += kofaktor
    return det


def gauss_jordan(A, b):
    """
    Ax = b sistemini çözer.
    A: nxn katsayılar matrisi
    b: n elemanlı sonuç vektörü
    """
    n = len(A)
    # Genişletilmiş matris oluştur (Augmented Matrix: [A | b])
    M = [A[i][:] + [float(b[i])] for i in range(n)]

    for i in range(n):
        # Pivot seçimi (0'a bölme hatasını engellemek için satır değiştirme)
        maks_satir = i
        for k in range(i + 1, n):
            if abs(M[k][i]) > abs(M[maks_satir][i]):
                maks_satir = k
        M[i], M[maks_satir] = M[maks_satir], M[i]

        pivot = M[i][i]
        if abs(pivot) < 1e-9:
            print("[!] Hata: Sistemin tek bir çözümü yok (Sonsuz çözüm veya Çözümsüz)!")
            return None

        # Pivot satırını 1 yap
        for j in range(i, n + 1):
            M[i][j] /= pivot

        # Diğer satırları sıfırla
        for k in range(n):
            if k != i:
                kat = M[k][i]
                for j in range(i, n + 1):
                    M[k][j] -= kat * M[i][j]

    # Çözüm son sütunda oluşur
    cozum = [M[i][n] for i in range(n)]
    return cozum


def matris_al(satir_sayisi, sutun_sayisi, isim="Matris"):
    print(f"\n{isim} değerlerini girin ({satir_sayisi}x{sutun_sayisi}):")
    M = []
    for i in range(satir_sayisi):
        while True:
            try:
                girdi = input(f"Satır {i+1} (sayıları boşlukla ayırın): ").strip().split()
                satir = [float(x) for x in girdi]
                if len(satir) != sutun_sayisi:
                    print(f"Lütfen tam olarak {sutun_sayisi} sayı girin!")
                    continue
                M.append(satir)
                break
            except ValueError:
                print("Hatalı giriş! Sadece sayı giriniz.")
    return M


def menu():
    while True:
        print("\n" + "=" * 40)
        print("   📐 MATRİS & DENKLEM ÇÖZÜCÜ (CLI)")
        print("=" * 40)
        print("1. Matris Çarpımı (A x B)")
        print("2. Determinant Hesabı (|A|)")
        print("3. Doğrusal Denklem Sistemi Çöz (Ax = b)")
        print("0. Çıkış")
        
        secim = input("\nSeçiminiz: ").strip()
        
        if secim == "0":
            print("Görüşmek üzere!")
            break

        elif secim == "1":
            r1 = int(input("A Matrisi Satır Sayısı: "))
            c1 = int(input("A Matrisi Sütun Sayısı: "))
            A = matris_al(r1, c1, "A Matrisi")

            r2 = int(input("B Matrisi Satır Sayısı: "))
            c2 = int(input("B Matrisi Sütun Sayısı: "))
            B = matris_al(r2, c2, "B Matrisi")

            sonuc = matris_carpimi(A, B)
            if sonuc:
                matris_yazdir(sonuc, "A x B Sonucu")

        elif secim == "2":
            n = int(input("Kare matris boyutu (n): "))
            A = matris_al(n, n, "Matris")
            det = determinant(A)
            if det is not None:
                print(f"\n[+] Matrisin Determinantı: {det:.4f}")

        elif secim == "3":
            n = int(input("Bilinmeyen sayısı (n): "))
            print("\nÖrnek: 2x + 3y = 8 için katsayılar '2 3', sonuç '8'")
            A = matris_al(n, n, "Katsayılar Matrisi (A)")
            
            print(f"\nSonuç Vektörünü (b) girin:")
            b = []
            for i in range(n):
                val = float(input(f"Denklem {i+1} sonucu: "))
                b.append(val)

            cozum = gauss_jordan(A, b)
            if cozum:
                print("\n[+] Bulunan Değişken Değerleri:")
                for i, x in enumerate(cozum):
                    print(f"  x{i+1} = {x:.4f}")

        else:
            print("[!] Geçersiz seçim, tekrar deneyin.")


if __name__ == "__main__":
    menu()