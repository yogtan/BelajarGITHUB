#Nomor 1
print("     DATA PEMLU      ")
print("---------------------")
umur = int(input("Masukkan Umur Anda "))
if umur < 17:
    print("Maaf, umur anda tidak mencukupi untuk memilih dalam pemilu!")
else:
    print("Selamat, umur anda mencukupi untuk memilih dalam pemilu!")
    print("Silahkan isi data lebih lanjut....")
#Nomor 2
print("\nBilangan Bulat dan Bilangan Ganjil")
print("----------------------------------")
bilangan = int(input("Masukkan bilangan : "))
hasil = bilangan%2

if hasil == 0:
    print("True")

else:
    print("False")
#Nomor 3
print("\n   Bilangan Habis Bagi 6   ")
print("----------------------------------")
bilangan = int(input("Masukkan bilangan : "))
hasil = bilangan%6

if hasil == 0:
    print("Habis Dibagi Enam")

else:
    print("Tidak Habis Dibagi Enam")
#Nomor 4

print("\nBilangan Bulat dan Bilangan Ganjil")
print("----------------------------------")
bilangan = int(input("Masukkan bilangan : "))
hasil = bilangan%2

if hasil == 0:
    print("Bilangan Genap")

else:
    print("Bilangan Ganjil")
#Nomor 5
print(" \nNilai Akhir Mahasiswa")
print("----------------------")
nama = str(input("Masukkan nama : "))
uts1 = int(input("Masukkan UTS1 : "))
uts2 = int(input("Masukkan UTS2 : "))
uas = int(input("Masukkan UAS  : "))

nilaiFinal = (0.3*uts1)+(0.3*uts2)+(0.4*uas)

if nilaiFinal < 55:
    print(nama,"nilai finalnya adalah ",nilaiFinal,"E")
elif nilaiFinal > 55 and nilaiFinal < 59:
    print(nama,"nilai finalnya adalah ",nilaiFinal,"D")
elif nilaiFinal > 60 and nilaiFinal < 69:
    print(nama,"nilai finalnya adalah ",nilaiFinal,"C")
elif nilaiFinal > 70 and nilaiFinal < 79:
    print(nama,"nilai finalnya adalah ",nilaiFinal,"B")
else:
    print(nama,"nilai finalnya adalah ",nilaiFinal,"A")


     
