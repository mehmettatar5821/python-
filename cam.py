import cv2

def kamerayi_ac():
    print("📷 Kamera açılıyor... Kapatmak için klavyeden 'q' tuşuna bas!")
  
    kamera = cv2.VideoCapture(0)
    
    while True:
    
        ret, kare = kamera.read()
        
        if not ret:
            print("❌ Kameradan görüntü alınamadı!")
            break
     
        gri_kare = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
  
        kenarlar = cv2.Canny(gri_kare, 30, 100)
 
        cv2.imshow("Mehmet'in Kamerasi (Orijinal)", kare)
        cv2.imshow("Mehmet'in Kamerasi (Efektli)", kenarlar)
 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
             
    kamera.release()
    cv2.destroyAllWindows()

 
kamerayi_ac()