#Studi Kasus Menghitung Bilangan Bulat
import math
print("\nCek Besar Kecilnya Bilangan Bulat")
print("-------------------------")
angka1 = float(input("Masukkan Angka Pertama : ")) #Meminta User untuk memasukkan angka
angka2 = float(input("Masukkan Angka Kedua   : ")) #Meminta User untuk memasukkan angka

#Mengecek angka Terbesar dan Terkecil
if angka1 > angka2:
    print("Angka Pertama Lebih Besar dari Angka Kedua")
elif angka1 < angka2:
    print("Angka Kedua Lebih Besar dari Angka Pertama")
else:
    print("Angka Sama Besar")


#Program Berat Badan Ideal menggunakan AND
print("\nProgram Berat Badan Ideal")
print("------------------------")
nama = input("Masukkan Nama Anda : ")
TB = float(input("Masukkab Tinggi Badan : "))
BB = float(input("Masukkab Berat Badan  : "))

if TB > 90 and TB < 110: #Aturan AND(&&)
    print("Berat Badan Ideal")
elif TB < 90:
    print("Berat Badan Terlalu Gemuk")
else:
    print("Berat Badan Terlalu Kurus")

#Pembayaran TOKO Programer
print("\nTOKO IT")
print("-------------------------")
print("Informasi Harga Barang ")
print("Harga/Barang Rp. 100.000")
item = 100000
jumB = float(input("Masukkan Jumlah Barang : ")) #Meminta user memasukkan jumlah barang
jumH = item*jumB #Perhitungan harga dengan jumlah barang
disc = 0.1*jumH #Menghitung discount

if jumH >= 1000000:
    print("Selamat Anda Mendapatkan Diskon 10%")
    print("Harga Sebelum Discount : ",jumH)
    print("Discount :",disc)
    jumTot = jumH - disc
    print("Total Pembayaran RP.",jumTot)
else:
    print("Total Pembayaran Rp.",jumH)

#Menghitung Nilai Mahasiswa
print("\nNilai Final Mahasiswa")
print("-----------------------")
nama = str(input("Masukkan Nama    : ")) #Beberapa baris disini berfungsi untuk input data dari user
uts1 = float(input("Masukkan UTS 1 : "))
uts2 = float(input("Masukkan UTS 2 : "))
uas  = float(input("Masukkan UAS   : "))\

nilaiFinal = (0.3*uts1) + (0.3*uts2) + (0.4*uas) #menghitung nilaiFinal

#Percabangan untuk emncari nilaiFinal mahasiswa
if nilaiFinal > 80:
    print(nama,"Nilai Finalnya adalah ",nilaiFinal," A")
elif nilaiFinal > 70:
    print(nama,"Nilai Finalnya adalah ",nilaiFinal, "B")
elif nilaiFinal > 60:
    print(nama," Nilai Finalnya adalah ",nilaiFinal," C")
else:
    print(nama," Nilai Finalnya adalah ",nilaiFinal," D")


angka = float(input("Masukkan Angka : "))
akar = math.sqrt(angka)



 