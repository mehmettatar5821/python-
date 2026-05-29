import platform
import os
import sys

def sistem_bilgilerini_getir():
    print("🖥️  Mehmet'in Bilgisayar Sistem Kartı 🖥️")
    print("=" * 40)
    
    # İşletim sistemi detayları
    print(f"📁 İşletim Sistemi: {platform.system()} {platform.release()}")
    print(f"⚙️ Sistem Mimarisi: {platform.architecture()[0]}")
    
    # İşlemci bilgisi
    print(f"🧠 İşlemci (CPU): {platform.processor()}")
    
    # Bilgisayar adı ve Python sürümü
    print(f"📛 Bilgisayar Adı: {platform.node()}")
    print(f"🐍 Python Sürümü: {sys.version.split()[0]}")
    
    print("=" * 40)
    
    # Küçük bir interaktif dokunuş: Kullanıcı isterse bir klasör açalım
    secim = input("Klasör temizliği için masaüstünü görmek ister misin? (E/H): ").upper()
    if secim == "E":
        if platform.system() == "Windows":
            os.system("explorer .")
        elif platform.system() == "Darwin":  # Mac için
            os.system("open .")

# ÇÖZÜM: Bu satırın başındaki boşluğu tamamen sildik (En sola yasladık)
sistem_bilgilerini_getir()