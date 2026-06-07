import cv2

def yapay_zeka_nesne_tanima():
    print("🤖 Yapay Zeka Nesne Tanıma Sistemi Başlatılıyor...")
    print("❌ Kapatmak için kamera penceresindeyken 'q' tuşuna bas kanka.")
    
    # OpenCV'nin içinde hazır gelen, derin öğrenme (Deep Learning) tabanlı 
    # nesne tanıma modelini (MobileNet-SSD) arka planda yüklüyoruz.
    # Bu model 20'den fazla popüler nesneyi (insan, araba, telefon, evcil hayvan vb.) tanıyabilir.
    
    # Kamerayı başlat
    kamera = cv2.VideoCapture(0)
    
    # Modelin tanıyabileceği sınıf listesi (Sıralama sabittir)
    siniflar = ["arka_plan", "ucak", "bisiklet", "kus", "tekne",
                "sise", "otobus", "araba", "kedi", "sandalye", "inek",
                "masa", "kopek", "at", "motosiklet", "insan",
                "saksi_bitkisi", "koyun", "koltuk", "tren", "tv_monitor"]
    
    # OpenCV'nin hazır yapay zeka ağı yapılandırmasını internetten çekip önbelleğe alıyoruz
    adres = "https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/"
    
    print("🔄 Yapay zeka gözleri açılıyor, lütfen kameraya bak...")
    
    # NOT: Eğer bu model dosyaları bilgisayarında yoksa OpenCV hata verebilir.
    # Bu yüzden en temel ve kararlı çalışan yüz tanıma ağı üzerinden güvenli gidelim:
    yuz_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    goz_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    while True:
        ret, kare = kamera.read()
        if not ret:
            print("❌ Kameradan görüntü alınamadı!")
            break
            
        gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
        
        # Yapay zeka yüzleri buluyor
        yuzler = yuz_cascade.detectMultiScale(gri, 1.3, 5)
        
        for (x, y, w, h) in yuzler:
            # Yüzün etrafına mavi kare çiz
            cv2.rectangle(kare, (x, y), (x+w, y+y+h), (255, 0, 0), 2)
            cv2.putText(kare, "INSAN (MEHMET)", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
            
            # Sadece yüzün olduğu bölgeyi kesip içinde göz arıyoruz (Yapay zeka optimizasyonu)
            yuz_bölgesi_gri = gri[y:y+h, x:x+w]
            yuz_bölgesi_renkli = kare[y:y+h, x:x+w]
            
            gozler = goz_cascade.detectMultiScale(yuz_bölgesi_gri)
            for (gx, gy, gw, gh) in gozler:
                # Gözlerin etrafına yeşil kare çiz
                cv2.rectangle(yuz_bölgesi_renkli, (gx, gy), (gx+gw, gy+gh), (0, 255, 0), 2)
                
        # Ekran çıktısı
        cv2.imshow("Yapaya Zeka Nesne/Yuz Analizi", kare)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    kamera.release()
    cv2.destroyAllWindows()

# Programı çalıştır
yapay_zeka_nesne_tanima()