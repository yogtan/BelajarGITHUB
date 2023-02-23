def metod() :
    print("hello world")

def presodur(a) : 
    
    print("data ",a) 

def persegi(panjang, lebar) :
    luas = panjang*lebar
    return luas

def segitiga(alas, tinggi) :
    luas = (alas*tinggi)*0.5
    return luas
    
cek = segitiga(5,4)
print(cek)

met = metod()

gas = presodur(5)
hitung = persegi(5, 4)
print(hitung)

print("tes")

# Belajar menginoputkan data melalui keyboard


def inputData() : #Method
    a = int(input("Panjang = "))
    b = int(input("Lebar = "))
    print("Total = ", a*b)

inputData()



a = 10

def coba(): #Coba tampilkan angka lewat fungsi
    print("Nilai a adalah",a)

    coba()
"""def Array():
    a = ["Egi", "Yogtan", "Tian", "Leon", "Junai", "Justin"]
    for i in a:
        print(a.index(i),".", i)

Array()"""
