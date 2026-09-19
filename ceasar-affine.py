import string
import math


def temizle(metin: str) -> str:
    """Türkçe karakterleri dönüştürür ve metni normalize eder."""
    tr_map = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")
    return metin.translate(tr_map).upper()


# ---------------- 1. CAESAR CIPHER ----------------
def caesar_encrypt(text: str, shift: int) -> str:
    text = temizle(text)
    res = []
    for ch in text:
        if ch.isalpha():
            res.append(chr((ord(ch) - 65 + shift) % 26 + 65))
        else:
            res.append(ch)
    return "".join(res)


def caesar_decrypt(text: str, shift: int) -> str:
    return caesar_encrypt(text, -shift)


def caesar_brute_force(text: str):
    print("\n--- Olası 25 Farklı Çözüm ---")
    for s in range(1, 26):
        print(f"[Shift {s:02d}]: {caesar_decrypt(text, s)}")
    print("------------------------------\n")


# ---------------- 2. AFFINE CIPHER (E(x) = (ax + b) mod 26) ----------------
def mod_inverse(a: int, m: int = 26) -> int:
    """ax ≡ 1 (mod m) denkliğini sağlayan modüler tersi bulur."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def affine_encrypt(text: str, a: int, b: int) -> str:
    if math.gcd(a, 26) != 1:
        print("[!] Hata: 'a' sayısı 26 ile aralarında asal olmalı (örn: 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25).")
        return ""
    text = temizle(text)
    res = []
    for ch in text:
        if ch.isalpha():
            x = ord(ch) - 65
            enc = (a * x + b) % 26
            res.append(chr(enc + 65))
        else:
            res.append(ch)
    return "".join(res)


def affine_decrypt(text: str, a: int, b: int) -> str:
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        print("[!] Hata: Modüler ters bulunamadı, şifre çözülemez.")
        return ""
    text = temizle(text)
    res = []
    for ch in text:
        if ch.isalpha():
            y = ord(ch) - 65
            dec = (a_inv * (y - b)) % 26
            res.append(chr(dec + 65))
        else:
            res.append(ch)
    return "".join(res)


# ---------------- 3. ATBASH CIPHER (A <-> Z, B <-> Y) ----------------
def atbash(text: str) -> str:
    text = temizle(text)
    alfabe = string.ascii_uppercase
    ters_alfabe = alfabe[::-1]
    tablo = str.maketrans(alfabe, ters_alfabe)
    return text.translate(tablo)


# ---------------- MENÜ VE AKIŞ ----------------
def menu():
    while True:
        print("\n================================")
        print("   🔐 CLI KRİPTO & ŞİFRELEME    ")
        print("================================")
        print("1. Sezar Şifreleme (Caesar)")
        print("2. Sezar Şifre Çözme")
        print("3. Sezar Kaba Kuvvet (Brute-Force)")
        print("4. Affine Şifreleme")
        print("5. Affine Şifre Çözme")
        print("6. Atbash Şifreleme / Çözme")
        print("0. Çıkış")
        
        secim = input("\nSeçiminiz [0-6]: ").strip()
        
        if secim == "0":
            print("Görüşürüz!")
            break
            
        metin = input("Metni girin: ")

        if secim == "1":
            shift = int(input("Öteleme miktarı (Anahtar - int): "))
            print(f"\n[+] Sonuç: {caesar_encrypt(metin, shift)}")
            
        elif secim == "2":
            shift = int(input("Öteleme miktarı (Anahtar - int): "))
            print(f"\n[+] Sonuç: {caesar_decrypt(metin, shift)}")
            
        elif secim == "3":
            caesar_brute_force(metin)
            
        elif secim == "4":
            a = int(input("'a' katsayısı (26 ile asal, örn: 3, 5, 7): "))
            b = int(input("'b' kaydırma katsayısı: "))
            sonuc = affine_encrypt(metin, a, b)
            if sonuc:
                print(f"\n[+] Sonuç: {sonuc}")
                
        elif secim == "5":
            a = int(input("'a' katsayısı: "))
            b = int(input("'b' katsayısı: "))
            sonuc = affine_decrypt(metin, a, b)
            if sonuc:
                print(f"\n[+] Sonuç: {sonuc}")
                
        elif secim == "6":
            print(f"\n[+] Sonuç: {atbash(metin)}")
            
        else:
            print("[!] Geçersiz seçim, tekrar deneyin.")


if __name__ == "__main__":
    menu()