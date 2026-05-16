balance = 1000

print("=== TATAR Bankasına Hoş Geldiniz ===")

while True:
    print("\n1 - Bakiye Görüntüle")
    print("2 - Para Yatır")
    print("3 - Para Çek")
    print("4 - Çıkış")

    choice = input("Seçim yap: ")

    if choice == "1":
        print(f"Güncel bakiyen: {balance} TL")

    elif choice == "2":
        amount = int(input("Yatırılacak miktar: "))
        balance += amount
        print(f"{amount} TL yatırıldı.")

    elif choice == "3":
        amount = int(input("Çekilecek miktar: "))

        if amount > balance:
            print("Yetersiz bakiye!")
        else:
            balance -= amount
            print(f"{amount} TL çekildi.")

    elif choice == "4":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz seçim!")