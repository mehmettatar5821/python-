import pygame
import numpy as np
import sys

# Ekran Ayarları
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 4  # Her bir hücrenin piksel boyutu
COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

# Renkler (RGB)
COLOR_BG = (10, 10, 15)       # Derin uzay siyahı
COLOR_ALIVE = (0, 255, 204)   # Neon Turkuaz (Canlı hücreler)
COLOR_DYING = (255, 0, 128)   # Neon Pembe (Ölen/Can çekişen hücreler)

# Pygame Başlatma
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matematiksel Kristal Büyüme Simülasyonu")
clock = pygame.time.Clock()

# Matrisleri Başlatma: 0=Ölü, 1=Canlı, 2=Can Çekişiyor
grid = np.zeros((ROWS, COLS), dtype=int)

# Tam merkeze ilk "tohum" kristalini ekiyoruz
grid[ROWS // 2, COLS // 2] = 1
# Çevresine de birkaç rastgele nokta koyalım ki etkileşim hızlı başlasın
grid[ROWS // 2 + 1, COLS // 2 - 1] = 1
grid[ROWS // 2 - 2, COLS // 2 + 2] = 1

def update_grid(current_grid):
    """Hücresel otomat kurallarına göre bir sonraki nesli hesaplar."""
    next_grid = np.zeros_like(current_grid)
    
    # Kenarlardaki taşmaları önlemek için iç kısımda dönüyoruz
    for r in range(1, ROWS - 1):
        for c in range(1, COLS - 1):
            state = current_grid[r, c]
            
            if state == 1:
                # Canlı hücre bir sonraki adımda can çekişme (dying) fazına geçer
                next_grid[r, c] = 2
            elif state == 2:
                # Can çekişen hücre bir sonraki adımda ölür
                next_grid[r, c] = 0
            elif state == 0:
                # Ölü bir hücrenin çevresindeki 8 komşudan tam olarak KAÇ tanesi CANLI?
                # (Can çekişenler yani 2'ler üremeyi tetiklemez, sadece 1'ler)
                neighbors = current_grid[r-1:r+2, c-1:c+2]
                alive_neighbors = np.sum(neighbors == 1)
                
                # KURAL: Ölü bir hücrenin çevresinde tam olarak 2 canlı komşu varsa HAYATA DÖNER.
                # Bu kural muazzam simetrik kristal yapılar ve labirentler doğurur.
                if alive_neighbors == 2:
                    next_grid[r, c] = 1
                    
    return next_grid

# Ana Döngü
running = True
paused = False

while running:
    screen.fill(COLOR_BG)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Boşluk tuşu ile duraklat/devam et
                paused = not paused
            elif event.key == pygame.K_c:    # 'C' tuşu ile ekranı temizle
                grid = np.zeros((ROWS, COLS), dtype=int)
                
    # Mouse ile ekrana dokunarak yeni canlı hücreler ekleyebilirsin!
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # Sol tık
        mx, my = pygame.mouse.get_pos()
        mc, mr = mx // CELL_SIZE, my // CELL_SIZE
        if 0 < mr < ROWS-1 and 0 < mc < COLS-1:
            grid[mr, mc] = 1

    # Hücreleri Ekrana Çizme
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r, c] == 1:
                pygame.draw.rect(screen, COLOR_ALIVE, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))
            elif grid[r, c] == 2:
                pygame.draw.rect(screen, COLOR_DYING, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))

    # Güncelleme
    if not paused:
        grid = update_grid(grid)
        
    pygame.display.flip()
    clock.tick(30)  # FPS sınırı (Hızı değiştirmek için burayı oynayabilirsin)

pygame.quit()
sys.exit()