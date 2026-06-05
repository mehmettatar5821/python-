import os
import sys

# HİLE: Eğer bilgisayar pyautogui kütüphanesini bulamazsa, kod çalışırken otomatik kuracak!
try:
    import pyautogui
except ModuleNotFoundError:
    print("📦 'pyautogui' bulunamadı, Mehmet için otomatik kuruluyor...")
    # VS Code o an hangi Python'ı çalıştırıyorsa onun pip sistemini tetikliyoruz
    os.system(f'"{sys.executable}" -m pip install pyautogui')
    print("✅ Kurulum bitti! Lütfen programı tekraaar çalıştır kanka.")
    sys.exit()

import time

def otomatik_islem_botu():
    print("🤖 Mehmet'in Otomasyon Botu Başlatılıyor...")
    print("--------------------------------------------------")
    print("⏳ 5 saniye içinde farenizi işlem yapılacak alana getirin...")
    print("--------------------------------------------------")
    
    for i in range(5, 0, -1):
        print(f"⏱️ Son {i} saniye...")
        time.sleep(1)
        
    try:
        x, y = pyautogui.position()
        print(f"\n🎯 İşlem Başladı! Fare Konumu: X={x}, Y={y}")
        
        pyautogui.click(x, y)
        time.sleep(0.5) 
        
        mesaj = "Bu mesaj Python otomasyon botu tarafindan otomatik yazilmistir! Kral basti, bot yazdi. 😎"
        pyautogui.write(mesaj, interval=0.05)
        
        pyautogui.press('enter')
        print("--------------------------------------------------")
        print("🎉 Otomasyon başarıyla tamamlandı kral!")
        
    except Exception as e:
        print(f"❌ Bir hata oluştu: {e}")

# Programı çalıştır
otomatik_islem_botu() 