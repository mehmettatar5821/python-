import pygame
import math
import sys

# Ekran Ayarları
WIDTH, HEIGHT = 900, 700
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kaotik Çift Sarkaç ve Çizgi İzi Simülasyonu")
clock = pygame.time.Clock()

# Sarkaç Parametreleri (Uzunluklar ve Kütleler)
L1, L2 = 180, 180  # Sarkaç kollarının uzunlukları
M1, M2 = 15, 15    # Sarkaç uçlarındaki kütleler
G = 0.6            # Yerçekimi ivmesi (Hızı ayarlamak için ölçeklendi)

# Başlangıç Durumları (Açılar ve Açısal Hızlar)
# Açılar radyan cinsinden (math.pi / 2 = 90 derece)
theta1 = math.pi / 2
theta2 = math.pi / 2
alpha1 = 0.0  # Açısal hız 1
alpha2 = 0.0  # Açısal hız 2

# Merkez Noktası (Sarkacın tavana asıldığı yer)
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2 - 50

# Sarkacın ucunun bıraktığı izleri saklamak için liste
trace_points = []
MAX_TRACE_LENGTH = 1200  # Ekranda kalacak maksimum iz çizgisi sayısı

# Renk Tanımlamaları
COLOR_BG = (12, 12, 18)       # Gece mavisi / siyah arka plan
COLOR_PENDULUM = (200, 200, 200) # Sarkaç kolları rengi

running = True
paused = False

while running:
    screen.fill(COLOR_BG)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Boşluk tuşu ile duraklat
                paused = not paused
            elif event.key == pygame.K_c:    # 'C' ile sadece çizilen izi temizle
                trace_points.clear()

    if not paused:
        # ÇİFT SARKAÇ HAREKET DENKLEMLERİ (Lagrangian Mekaniği Çözümü)
        # Bu formüller sarkacın o anki açılarına göre ivmelerini (accel1 ve accel2) hesaplar.
        num1 = -G * (2 * M1 + M2) * math.sin(theta1) - M2 * G * math.sin(theta1 - 2 * theta2) - 2 * math.sin(theta1 - theta2) * M2 * (alpha2**2 * L2 + alpha1**2 * L1 * math.cos(theta1 - theta2))
        den1 = L1 * (2 * M1 + M2 - M2 * math.cos(2 * theta1 - 2 * theta2))
        accel1 = num1 / den1

        num2 = 2 * math.sin(theta1 - theta2) * (alpha1**2 * L1 * (M1 + M2) + G * (M1 + M2) * math.cos(theta1) + alpha2**2 * L2 * M2 * math.cos(theta1 - theta2))
        den2 = L2 * (2 * M1 + M2 - M2 * math.cos(2 * theta1 - 2 * theta2))
        accel2 = num2 / den2

        # Hız ve konum güncelleme (Euler-Cromer Metodu)
        alpha1 += accel1
        alpha2 += accel2
        theta1 += alpha1
        theta2 += alpha2

        # Sürtünme simülasyonu (Enerjinin sonsuza gitmesini engellemek için hafif sönümleme)
        alpha1 *= 0.999
        alpha2 *= 0.999

    # Birinci sarkacın uç koordinatları
    x1 = CENTER_X + L1 * math.sin(theta1)
    y1 = CENTER_Y + L1 * math.cos(theta1)

    # İkinci sarkacın uç koordinatları (İzi bırakan asıl kaotik uç)
    x2 = x1 + L2 * math.sin(theta2)
    y2 = y1 + L2 * math.cos(theta2)

    # Eğer oyun duraklatılmadıysa yeni pozisyonu iz listesine ekle
    if not paused:
        trace_points.append((x2, y2))
        if len(trace_points) > MAX_TRACE_LENGTH:
            trace_points.pop(0)

    # 1. İZİ ÇİZME: Zaman içindeki renk geçişi (Gökkuşağı / Spektrum etkisi)
    if len(trace_points) > 1:
        for i in range(len(trace_points) - 1):
            # İz eskidikçe rengini değiştiren ve solduran bir renk algoritması
            progress = i / len(trace_points)
            r = int(100 + 155 * math.sin(progress * math.pi))
            g = int(50 + 205 * progress)
            b = int(255 - 155 * progress)
            
            pygame.draw.line(screen, (r, g, b), trace_points[i], trace_points[i+1], 2)

    # 2. SARKAÇ KOLLARINI VE KÜTLELERİ ÇİZME
    # Tavandan birinci kütleye kol
    pygame.draw.line(screen, COLOR_PENDULUM, (CENTER_X, CENTER_Y), (x1, y1), 3)
    # Birinci kütleden ikinci kütleye kol
    pygame.draw.line(screen, COLOR_PENDULUM, (x1, y1), (x2, y2), 3)

    # Kütlelerin kendileri (Daireler)
    pygame.draw.circle(screen, (0, 255, 254), (int(x1), int(y1)), 10)
    pygame.draw.circle(screen, (255, 0, 128), (int(x2), int(y2)), 12)
    # Sabit tavan noktası
    pygame.draw.circle(screen, (255, 255, 255), (CENTER_X, CENTER_Y), 5)

    pygame.display.flip()
    clock.tick(60)  # 60 FPS akıcılık

pygame.quit()
sys.exit()