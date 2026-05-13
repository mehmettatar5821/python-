password = "1234"

print("Sisteme Hoş Geldin")

attempt = 3

while attempt > 0:
    entered = input("Şifreyi gir: ")

    if entered == password:
        print("Giriş başarılı!")
        break
    else:
        attempt -= 1
        print("Yanlış şifre!")

        if attempt > 0:
            print(f"Kalan hak: {attempt}")
        else:
            print("Sistem kilitlendi!")