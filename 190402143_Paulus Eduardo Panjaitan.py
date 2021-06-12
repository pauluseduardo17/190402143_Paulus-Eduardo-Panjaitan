#UAS PEMOGRAMAN TE-D
#MESIN ATM OTOMATIS
#Oleh Paulus Eduardo Panjaitan
#Nim 190402143

a = "Selamat Datang di ATM saya"
b = "Pilih Option"
print (a)
print (b)
list1 = "1. Ambil Uang Saya"
list2 = "2. Tabung Uang Saya"
list3 = "3. Check Uang Saya"
print(list1)
print(list2)
print(list3)
option=int(input("Silahkan Pilih Option :"))
if option==1:
    print("Uang Kamu Berjumlah Rp.500.000,00, Mau ambil berapa?")
    list4 = "1. Rp.50.000,00"
    list5 = "2. Rp.100.000,00"
    print(list4)
    print(list5)
    uang_kamu=500000
    option1=int(input("Option :"))
    if option1==1:
        hasil1=uang_kamu-50000
        print("Uang Kamu Sekarang Berjumlah :", hasil1)
    elif option1==2:
        hasil2 = uang_kamu-100000
        print("Uang Kamu Sekarang Berjumlah :", hasil2)
    else:
        print("Keywoard Anda Salah!")

elif option==2:
    uang_kamu=500000
    print("Uang Kamu Berjumlah Rp.500.000,00, Mau Nabung Berapa?")
    option2=int(input("Masukkan Jumlah Uang :"))
    hasil3=uang_kamu+option2
    print("Jumlah Uang Kamu Sekarang Adalah ", hasil3)
else:
    print("Keyword Anda Salah, Mohon Coba lagi")

if option==3:
    print("Uang Kamu Berjumlah Rp.500.000,00")
