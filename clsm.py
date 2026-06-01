import tkinter as tk
from tkinter import messagebox

def gorev_ekle():
    gorev = gorev_giris.get()
    if gorev != "":
        liste_kutusu.insert(tk.END, f"📌 {gorev}")
        gorev_giris.delete(0, tk.END)
    else:
        messagebox.showwarning("Uyarı", "Lütfen boş bırakma, bir şeyler yaz kanka!")

def gorev_sil():
    try:
        secili_indeks = liste_kutusu.curselection()[0]
        liste_kutusu.delete(secili_indeks)
    except IndexError:
        messagebox.showwarning("Uyarı", "Silmek için listeden bir görev seçmelisin!")

# Ana pencere kurulumu
pencere = tk.Tk()
pencere.title("Mehmet'in Görev Defteri")
pencere.geometry("400x450")
pencere.configure(bg="#2c3e50") # Havalı bir koyu gri/mavi arka plan

# Başlık etiketi
baslik = tk.Label(pencere, text="📝 YAPILACAKLAR LİSTESİ", font=("Arial", 16, "bold"), bg="#2c3e50", fg="#ecf0f1")
baslik.pack(pady=15)

# Görev giriş alanı
gorev_giris = tk.Entry(pencere, font=("Arial", 12), width=25)
gorev_giris.pack(pady=5)

# Ekleme butonu
ekle_butonu = tk.Button(pencere, text="Listeye Ekle", font=("Arial", 10, "bold"), bg="#2ecc71", fg="white", width=15, command=gorev_ekle)
ekle_butonu.pack(pady=5)

# Görevlerin listeleneceği kutu
liste_kutusu = tk.Listbox(pencere, font=("Arial", 12), width=30, height=12, bg="#34495e", fg="#ecf0f1", selectbackground="#e74c3c")
liste_kutusu.pack(pady=10)

# Silme butonu
sil_butonu = tk.Button(pencere, text="Seçileni Sil", font=("Arial", 10, "bold"), bg="#e74c3c", fg="white", width=15, command=gorev_sil)
sil_butonu.pack(pady=5)

# Pencereyi açık tutan döngü
pencere.mainloop()