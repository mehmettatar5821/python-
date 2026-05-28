import qrcode

def qr_kod_ureticisi():
    print("📱 Python QR Kod Üreticiye Hoş Geldin!")
    print("---------------------------------------")
    
    # Kullanıcıdan link veya metin alıyoruz
    veri = input("QR koda dönüştürmek istediğin linki veya mesajı gir: ")
    dosya_adi = input("Kaydedilecek dosyanın adı ne olsun? (Örn: benim_kodum): ")
    
    # QR kodun tasarım ayarlarını yapıyoruz
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Veriyi ekliyoruz ve QR kodu oluşturuyoruz
    qr.add_data(veri)
    qr.make(fit=True)
    
    # QR kodu renklendiriyoruz (Arka plan siyah, kod beyaz veya tam tersi yapabilirsin)
    resim = qr.make_image(fill_color="black", back_color="white")
    
    # Resmi bilgisayara kaydediyoruz
    tam_dosya_adi = f"{dosya_adi}.png"
    resim.save(tam_dosya_adi)
    
    print("---------------------------------------")
    print(f"🎉 Harika! QR kodun '{tam_dosya_adi}' adıyla başarıyla kaydedildi.")
    print("📸 Klasörüne gidip resmi açabilir ve telefonunla taratabilirsin!")

# Programı çalıştır
qr_kod_ureticisi()