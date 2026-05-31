import cv2

def yuz_takip_garanti():
    # OpenCV'nin kendi içinde internet istemeden çalışan yüz tanıma modelini yüklüyoruz
    yuz_modeli = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    yuz_tasarim = cv2.CascadeClassifier(yuz_modeli)
    
    print("📷 Saf OpenCV Kamerası Açılıyor...")
    print("❌ Kapatmak için kamera penceresindeyken 'q' tuşuna bas.")
    
    kamera = cv2.VideoCapture(0)
    
    while True:
        ret, kare = kamera.read()
        if not ret:
            print("❌ Kameradan görüntü alınamadı!")
            break
            
        # Görüntüyü işlemeyi kolaylaştırmak için gri tonlamaya çeviriyoruz
        gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
        
        # Yüzleri tespit et
        yuzler = yuz_tasarim.detectMultiScale(gri, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
        
        # Tespit edilen her yüzün etrafına yeşil kare çiz ve yazı yaz
        for (x, y, w, h) in yuzler:
            cv2.rectangle(kare, (x, y), (x+w, y+h), (0, 255, 0), 3)
            cv2.putText(kare, "MEHMET", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            
        # Canlı yayını ekranda göster
        cv2.imshow("Sorunsuz Yuz Takip", kare)
        
        # 'q' tuşuna basınca döngüden çık
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    kamera.release()
    cv2.destroyAllWindows()

# Programı çalıştır
yuz_takip_garanti()