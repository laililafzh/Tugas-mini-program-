total1=0
total2=0
totalsemua=0
jenis1=""
jenis2=""

print("=== Program Kasir Sederhana ===")
nama = input("Masukkan nama Konsumen: ")
print ("Nama Konsumen :", nama)
print("")
print ("Menu Makanan")
    


def pilihan(i):
        switcher={
                1:'----Nasi Goreng 12000----',
                2:'----Soto 10000----',
                3:'----Mie Ayam 9000----'
             }
        return switcher.get(i,"Masukan Pilihan yang Benar!")


print("1. Nasi Goreng")
print("2. Soto")
print("3. Mie Ayam")
nomor=int(input("Masukan Pilihan: "))
menu=pilihan(nomor)
print (menu)
porsi1= int(input("Berapa Porsi: "))

if nomor==1:
    total1=total1+porsi1*12000
    print ("Hasilnya = ", total1)
    jenis1=("Nasi Goreng")
if nomor==2:
    total1=total1+porsi1*10000
    print ("Hasilnya = ", total1)
    jenis1=("Soto")
if nomor==3:
    total1=total1+porsi1*9000
    print ("Hasilnya = ", total1)
    jenis1=("Mie Ayam")

def pilihan(i):
        switcher={
                1:'----Es Teh 3000----',
                2:'----Es Jeruk 4000----',
                3:'----Es Kopi 3000----'
             }
        return switcher.get(i,"Masukan Pilihan yang Benar!")
print("\nMenu Minuman")
print("1. Es teh")
print("2. Es jeruk")
print("3. Es kopi")
nomor=int(input("Masukan Pilihan: "))
menu=pilihan(nomor)
print (menu)
porsi2= int(input("Berapa Gelas: "))
if nomor==1:
    total2=total2+(porsi2*3000)
    print ("Hasilnya = ", total2)
    jenis2=("Es Teh")
if nomor==2:
    total2=total2+(porsi2*4000)
    print ("Hasilnya = ", total2)
    jenis2=("Es Jeruk")
if nomor==3:
    total2=total2+(porsi2*3000)
    print ("Hasilnya = ", total2)
    jenis2=("Es Kopi")
    
uang=int(input("\nUang Tunai: Rp."))
totalsemua=total1+total2    
print("============================")
print("======= WARUNG MAKAN =======")
print("========= MAK LELA =========")
print("=Jl. RE. Martadinata No.53 =")
print("======== BONDOWOSO =========")
print("============================")
import time;
localtime = time.asctime( time.localtime(time.time()) )
print (localtime)
print ("=== Nama      :",nama)
print ("=== Beli      :",porsi1,jenis1)
print ("===            ",porsi2,jenis2)
print ("=== Tagihan   :Rp.",totalsemua)
print ("=== Uang      :Rp.",uang)
akhir=int(uang-totalsemua)
print ("=== Kembalian :Rp.",akhir)
print("=========================")
print("=========================")