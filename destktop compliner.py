import os
import shutil

def klasorleri_duzenle():
    print("--- DOSYA DUZENLEYICI ---")
    
    # Şu an hangi klasörün içinde olduğumuzu alıyoruz
    guncel_klasor = os.getcwd()
    print(f"Düzenlenecek klasör: {guncel_klasor}\n")

    # Hangi uzantının hangi klasöre gideceğini belirliyoruz
    kategoriler = {
        "Resimler": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Belgeler": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videolar": [".mp4", ".avi", ".mkv", ".mov"],
        "Programlar": [".exe", ".msi", ".bat"],
        "Arsivler": [".zip", ".rar", ".7z"]
    }

    # Klasördeki tüm dosyaları tek tek geziyoruz
    for dosya in os.listdir(guncel_klasor):
        # Bu kodun kendi .py dosyasını yanlışlıkla taşımayalım diye kontrol koyuyoruz
        if dosya == os.path.basename(__file__):
            continue
            
        # Dosya yolunu ve uzantısını alıyoruz
        dosya_yolu = os.path.join(guncel_klasor, dosya)
        
        # Eğer bir klasör değil de gerçekten dosyaysa işlem yap
        if os.path.isfile(dosya_yolu):
            dosya_uzantisi = os.path.splitext(dosya).lower()
            
            # Uzantının hangi kategoriye ait olduğunu buluyoruz
            tasindi_mi = False
            for hedef_klasor, uzantilar in kategoriler.items():
                if dosya_uzantisi in uzantilar:
                    # Hedef klasör yoksa otomatik oluşturuyoruz
                    if not os.path.exists(hedef_klasor):
                        os.makedirs(hedef_klasor)
                    
                    # Dosyayı yeni yerine taşıyoruz
                    shutil.move(dosya_yolu, os.path.join(hedef_klasor, dosya))
                    print(f"[TAŞINDI] {dosya} -> {hedef_klasor}")
                    tasindi_mi = True
                    break
            
            # Belirttiğimiz kategorilere uymayan diğer dosyalar için
            if not tasindi_mi:
                if not os.path.exists("Diger"):
                    os.makedirs("Diger")
                shutil.move(dosya_yolu, os.path.join("Diger", dosya))
                print(f"[TAŞINDI] {dosya} -> Diger")

    print("\nDüzenleme işlemi tamamlandı kanka!")

if __name__ == "__main__":
    klasorleri_duzenle()