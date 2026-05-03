import cv2
import numpy as np
import math

# Tuval boyutları
width, height = 800, 600
# Siyah bir ekran oluştur
img = np.zeros((height, width, 3), np.uint8)

def draw_tree(x, y, angle, length, depth):
    if depth == 0:
        return

    # Dalın uç noktasını hesapla (Trigonometri kullanarak)
    x_end = int(x + length * math.cos(math.radians(angle)))
    y_end = int(y - length * math.sin(math.radians(angle)))

    # Dalın kalınlığını derinliğe göre ayarla (Ağaç gövdesi kalın, uçlar ince olsun)
    thickness = max(1, depth)
    
    # Dalın rengini derinliğe göre değiştir (Gövde kahverengimsi, uçlar yeşilimsi)
    color = (50, 150 - (depth * 10), 50 + (depth * 20))

    # Çizgiyi çiz
    cv2.line(img, (x, y), (x_end, y_end), color, thickness)

    # Özyineleme: Sağa ve sola iki yeni dal çıkar
    # Dalları biraz kısalt ve açılarını değiştir
    draw_tree(x_end, y_end, angle - 25, length * 0.75, depth - 1)
    draw_tree(x_end, y_end, angle + 25, length * 0.75, depth - 1)

# Başlangıç noktası (Alt orta), Açı (90 derece dik), Dal uzunluğu, Derinlik (Dallanma sayısı)
draw_tree(width // 2, height - 20, 90, 120, 10)

cv2.imshow("Fraktal Agac", img)
cv2.waitKey(0)
cv2.destroyAllWindows()