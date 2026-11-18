#JESLYN JEANNETA
#065002600039
#PRAKTIKUM ALGORITMA - FILE HANDLING
def tulis_file ():
    file = open("Biodata.txt","w")
    nama = input("Masukkan Nama mu : ")
    umur = input("Masukkan Umur mu : ")
    alamat = input ("Masukkan Alamatmu : ")
    email = input ("Masukkan Emailmu : ")
    dosen = input ("Masukkan dosen walimu : ")

    file.write(f"Nama: {nama}\n")
    file.write(f"Umur: {umur}\n")
    file.write(f"Alamat: {alamat}\n")
    file.write(f"Email: {email}\n")
    file.write(f"Dosen Wali: {dosen}\n")

    file.close()

def baca_file():
    file = open("Biodata.txt", "r")
    isi = file.read()
    print("\nBerikut Ini Data Kamu")
    print(isi)

    file.close()


tulis_file()
baca_file()


