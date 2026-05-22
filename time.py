import tkinter as tk
import time

def zamani_guncelle():
    # Anlık saati alıp etikete yazdırıyoruz
    su_an = time.strftime('%H:%M:%S')
    saat_etiketi.config(text=su_an)
    # Her 200 milisaniyede bir kendini yeniler
    pencere.after(200, zamani_guncelle)

# Pencere ayarları
pencere = tk.Tk()
pencere.title("Hızlı Saat")
pencere.geometry("250x80")
pencere.configure(bg='black')

# Pencereyi her zaman en üstte tutar, arka plana kaçmaz
pencere.attributes('-topmost', True)

# Saat Etiketi
saat_etiketi = tk.Label(pencere, font=('Consolas', 30, 'bold'), bg='black', fg='#00FF00')
saat_etiketi.pack(expand=True)

# Sistemi başlat
zamani_guncelle()
pencere.mainloop()