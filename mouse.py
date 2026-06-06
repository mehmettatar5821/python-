import pyautogui
import time

def renk_tetiklemeli_bot():
    print("🎯 Mehmet'in Akıllı Piksel Botu Başlatılıyor...")
    print("--------------------------------------------------")
    
    # Botun avlayacağı rengi seçiyoruz (RGB formatında)
    # Örnek: (255, 0, 0) tamamen saf kırmızıdır. 
    # Sen buraya ekranında olan herhangi bir rengin RGB kodunu yazabilirsin.
    hedef_renk = (255, 0, 0) 
    
    print(f"🔍 Ekranda {hedef_renk} rengi aranıyor...")
    print("🛑 Botu durdurmak için fareyi ekranın en sol üst köşesine (0,0 noktasına) götür kanka.")
    print("--------------------------------------------------")
    
    # PyAutoGUI için acil durum freni (Fareyi sol üste çekince kod durur)
    pyautogui.FAILSAFE = True 
    
    tarama_alani = (0, 0, 1920, 1080) # Tüm ekranı tara (Genişliğe göre değiştirebilirsin)
    
    try:
        while True:
            # 1. Ekranın anlık fotoğrafını (screenshot) çekiyoruz
            ekran_resmi = pyautogui.screenshot(region=tarama_alani)
            genislik, yukseklik = ekran_resmi.size
            
            bulundu = False
            
            # 2. Ekrandaki pikselleri 20'şer adımla tarıyoruz (Hızlı olması için)
            for x in range(0, genislik, 20):
                for y in range(0, yukseklik, 20):
                    # O anki pikselin rengini al
                    piksel_rengi = ekran_resmi.getpixel((x, y))
                    
                    # 3. Eğer aradığımız rengi bulduysak:
                    if piksel_rengi == hedef_renk:
                        print(f"💥 Renk Bulundu! Koordinat: X={x}, Y={y} -> Tıklanıyor!")
                        # Fareyi o rengin üstüne götür ve tıkla
                        pyautogui.click(x, y)
                        bulundu = True
                        break # İç döngüden çık
                        
                if bulundu:
                    break # Dış döngüden çık
            
            # Ekranı sürekli tarayıp bilgisayarı ağlatmamak için kısa bir mola
            time.sleep(0.1)
            
    except pyautogui.FailSafeException:
        print("\n🛑 Acil durum freni tetiklendi! Bot başarıyla durduruldu kral.")
    except Exception as e:
        print(f"❌ Bir hata oluştu: {e}")

# Programı çalıştır
renk_tetiklemeli_bot()