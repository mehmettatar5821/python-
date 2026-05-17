import time

print("Sisteme bağlanılıyor...")
time.sleep(2)

print("IP adresi bulunuyor...")
time.sleep(2)

print("Sunucuya giriş yapılıyor...")
time.sleep(2)

print("Şifreler çözülüyor...")
time.sleep(2)

for i in range(0, 101, 10):
    print(f"%{i} tamamlandı")
    time.sleep(0.5)

print("\nERİŞİM BAŞARILI!")
print("Hoş geldiniz efendim 😎")