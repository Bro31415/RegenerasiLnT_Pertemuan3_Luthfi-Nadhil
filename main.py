import os

def mainMenu():
    print("\nSelamat Datang di Aplikasi Manajemen Karyawan Simple\n")
    print("1. Create File Karyawan Baru")
    print("2. Input File Karyawan Baru")
    print("3. Read File Karyawan")
    print("4. Delete File Karyawan")
    print("5. Exit")

mainMenu()
choose = int(input("Pilih salah satu opsi : "))

while choose != 0:
    if choose == 1:
        f = open("karyawan.txt", "x")
        f.close()
    if choose == 2:
        f = open("karyawan.txt", "w")
        nama = input("Masukkan nama: ")
        f.write("Nama: " + nama)
        age = input("Masukkan umur: ")
        f.write("\nUmur: " + age)
        f.close()
    elif choose == 3:
        f = open("karyawan.txt", "r")
        content = f.readlines()
        type(content)
        print(content)
        f.close()
    elif choose == 4:
        os.remove("karyawan.txt")
    elif choose == 5:
        exit()

    mainMenu()
    choose = int(input("\nPilih salah satu opsi : \n"))