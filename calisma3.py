import turtle
import colorsys

# Ekran ayarlarını yapıyoruz
ekran = turtle.Screen()
ekran.bgcolor("black")  # Arka planı siyah yap
ekran.title("Renk Girdabı")

# Çizim yapacak kaplumbağayı (imleci) oluşturuyoruz
cizici = turtle.Turtle()
cizici.speed(0)  # En hızlı mod

# Renklerin düzgün değişmesi için döngü kuruyoruz
for i in range(360):
    # Renk paletini gökkuşağı rengine ayarlıyoruz
    renk = colorsys.hsv_to_rgb(i / 360, 1.0, 1.0)
    cizici.pencolor(renk)
    
    # İleri git ve her adımda biraz dönerek şekli oluştur
    cizici.forward(i * 1.5)
    cizici.right(59)  # 59 derece dönerek girdap efekti yaratır
    cizici.width(i / 100 + 1)  # Çizgi kalınlığı gitgide artar

# Çizim bitince pencerenin hemen kapanmaması için
turtle.done()