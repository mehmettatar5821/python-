import os
import sys
import time

# Kütüphanelerin kurulu olup olmadığını kontrol eden akıllı sistemimiz
try:
    import speech_recognition as sr
    from gtts import gTTS
    from pygame import mixer
except ModuleNotFoundError:
    print("📦 Ses kütüphaneleri eksik, Mehmet için otomatik kuruluyor...")
    os.system(f'"{sys.executable}" -m pip install SpeechRecognition gTTS pygame')
    print("✅ Kurulum bitti! Lütfen kodu tekraaar çalıştır kanka.")
    sys.exit()

def bilgisayari_konustur(metin):
    # gTTS (Google Text-to-Speech) kullanarak metni Türkçe ses dosyasına çeviriyoruz
    tts = gTTS(text=metin, lang='tr')
    dosya_adi = "konusma.mp3"
    tts.save(dosya_adi)
    
    # Pygame mixer ile sesi arka planda pürüzsüzce çalıyoruz
    mixer.init()
    mixer.music.load(dosya_adi)
    mixer.music.play()
    
    # Ses bitene kadar programı bekletiyoruz
    while mixer.music.get_busy():
        time.sleep(0.1)
        
    mixer.quit()
    # İşimiz bitince geçici ses dosyasını bilgisayardan siliyoruz
    if os.path.exists(dosya_adi):
        os.remove(dosya_adi)

def sesi_yaziya_cevir():
    # Mikrofonu ve ses tanıma motorunu başlatıyoruz
    tanici = sr.Recognizer()
    
    with sr.Microphone() as kaynak:
        print("\n🎤 Sistem hazır! Ortam gürültüsü ayarlanıyor, lütfen 1 saniye sessiz kal...")
        tanici.adjust_for_ambient_noise(kaynak, duration=1)
        
        print("⚡ ŞİMDİ KONUŞ kanka! Seni dinliyorum...")
        bilgisayari_konustur("Seni dinliyorum Mehmet, konuşabilirsin.")
        
        # Sesi kaydediyoruz (5 saniye boyunca sessizlik olursa durur)
        ses = tanici.listen(kaynak, timeout=5, phrase_time_limit=5)
        print("🔄 Sesin alındı, yapay zeka tarafından işleniyor...")
        
        try:
            # Google Ses Tanıma servisini Türkçe diliyle tetikliyoruz
            cevirilen_metin = tanici.recognize_google(ses, language="tr-TR")
            print(f"📝 Ağzından Çıkan Söz: {cevirilen_metin}")
            
            # Bilgisayar senin söylediğin şeyi tekrar etsin
            cevap = f"Mehmet, bana '{cevirilen_metin}' dedin. Seni çok net duydum kral!"
            bilgisayari_konustur(cevap)
            
        except sr.UnknownValueError:
            print("❌ Yapay zeka ne dediğini tam anlayamadı, biraz daha net konuş kanka.")
            bilgisayari_konustur("Ne dediğini tam anlayamadım, tekrar eder misin?")
        except sr.RequestError:
            print("❌ İnternet bağlantısında bir sorun var!")

# Programı çalıştır
if __name__ == "__main__":
    sesi_yaziya_cevir()