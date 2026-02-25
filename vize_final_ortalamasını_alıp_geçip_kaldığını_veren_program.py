#vizenin %40 finalin ½60 ini alarak 50 gecme notu ile sonucu bildiren program

vize_notu=int(input("vize notunuzu giriniz: "))

final_notu=int(input("final notunuzu giriniz: "))

ortalama=(vize_notu*40/100)+(final_notu*60/100)

if ortalama < 50:
    print("geçmiş olsun büte bekleriz.. ")
else:
    print("tebrikler sinavdan geçtiniz")