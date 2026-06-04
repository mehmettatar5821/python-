import winsound
import time

def nota_calici():
    print("🎹 Mehmet'in Dijital Piyanosuna Hoş Geldin!")
    print("------------------------------------------")
    print("Tuşlar ve Notalar:")
    print("A = DO  | S = RE  | D = Mİ  | F = FA")
    print("G = SOL | H = LA  | J = Sİ  | K = İNCE DO")
    print("------------------------------------------")
    print("❌ Çıkış yapmak için 'X' tuşuna bas kanka.\n")

    # Notaların frekans değerleri (Hz cinsinden)
    notalar = {
        'a': 261,  # Do
        's': 294,  # Re
        'd': 329,  # Mi
        'f': 349,  # Fa
        'g': 392,  # Sol
        'h': 440,  # La
        'j': 494,  # Si
        'k': 523   # İnce Do
    }

    while True:
        tus = input("Bir nota tuşuna bas ve Enter'la: ").lower()

        if tus == 'x':
            print("👋 Piyano kapatıldı, harika besteydi kral!")
            break
        
        if tus in notalar:
            frekans = notalar[tus]
            # winsound.Beep(frekans, süre_milisaniye)
            # 300 milisaniye boyunca o notanın sesini çalar
            winsound.Beep(frekans, 300)
        else:
            print("❌ Geçersiz tuş! Sadece A, S, D, F, G, H, J, K kullan.")

# Programı çalıştır
nota_calici()