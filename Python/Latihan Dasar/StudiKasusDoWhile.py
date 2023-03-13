#Menghitung Harga Perliter
print("Harga/Liter Rp.6500")
print("Jum Liter\tHarga")
print("----------------------")
harga = int(6500)

liter = 1 #Meyimpan Bilangan
while liter < 5: #Melakukan Perulangan dengan kondisi 1 ke 21
    total = liter*harga #Menghitng total harga/liter
    print(liter,"\t",harga) #mencetak liter dan harga
    liter += 1 #Menambah liter di setiap perulangan

print("=============================================")
#Menghitung nilai rata-rata
total = int(input("Masukkan data yang diproses : "))
print("------------------------------------------")
jum = 0
i = 0

while i < total:
    data = int(input("Data ke  :"))
    jum = jum + data
    i += 1

rata = jum/total
print("Total Rata Ratanya adalah ",rata)

#Menghitung Berat Mangga
print("------------")
print("Toko Mangga")
print("------------")
i = 0
kecil = 0
sedang = 0
besar = 0
proses = int(input("Masukkan banyak proses manga : "))
while i < proses:
    data = int(input("Masukkan berat mangga : "))
    i += 1

    if data < 200:
        kecil = kecil + 1
    
    elif data < 600:
        sedang = sedang + 1
    else:
        besar = besar + 1

print("Dari ",proses," mangga yang ditimbang : ")
print("Kecil  : ",kecil," buah")
print("Sedang : ",sedang," buah")
print("besar  : ",besar," buah")
        
#Sistem Nilai Mahasiswa
print("Nilai Final Mahasiswa")
print("---------------------")
uts1 = 0
nama = input("Masukkan nama mahasiswa : ")
while True:
    uts1 = int(input("UTS 1 : "))
    if uts1 <= 0:
        break
    print("Ketik Ulang")


