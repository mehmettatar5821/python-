import math

def koordinat_dondur(x, y, aci_derece):
    print(f"📍 Başlangıç Koordinatı: ({x}, {y})")
    print(f"🔄 Döndürme Açısı: {aci_derece}°")
    print("----------------------------------------")
    
    # Python'ın sin ve cos fonksiyonları radyan cinsinden çalışır.
    # Bu yüzden önce dereceyi radyanna çeviriyoruz.
    radyan = math.radians(aci_derece)
    
    # 1. Adım: Döndürme Matrisinin (Rotation Matrix) elemanlarını hesapla
    # [ [cos_a, -sin_a],
    #   [sin_a,  cos_a] ]
    cos_a = math.cos(radyan)
    sin_a = math.sin(radyan)
    
    # 2. Adım: Matris Çarpımı Yapıyoruz
    # Yeni X = x * cos(a) - y * sin(a)
    # Yeni Y = x * sin(a) + y * cos(a)
    yeni_x = (x * cos_a) - (y * sin_a)
    yeni_y = (x * sin_a) + (y * cos_a)
    
    # Sonuçları virgülden sonra 2 basamağa yuvarlayalım temiz gözüksün
    return round(yeni_x, 2), round(yeni_y, 2)

# --- PROGRAMI TEST EDELİM ---

# Örnek: (1, 0) noktasını (yani X ekseni üzerindeki bir noktayı) 
# Saatin tersi yönünde 90 derece döndürelim. Tam (0, 1) noktasına yani Y eksenine gelmeli!
nokta_x = 1
nokta_y = 0
aci = 90

son_x, son_y = koordinat_dondur(nokta_x, nokta_y, aci)

print(f"🎯Hesaplanan Yeni Koordinat: ({son_x}, {son_y})")
print("========================================")

# Bir test daha: Aynı noktayı 180 derece döndür, (-1, 0) olmalı!
son_x2, son_y2 = koordinat_dondur(nokta_x, nokta_y, 180)
print(f"🎯 180 Derece Sonrası Yeni Koordinat: ({son_x2}, {son_y2})")