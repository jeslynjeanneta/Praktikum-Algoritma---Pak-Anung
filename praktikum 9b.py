#JESLYN JEANNETA
#0650026000039
#PRAKTIKUM ALGORITMA - FILE HANDLING

def create_file():
    nama_file = input("Masukkan Nama File: ")
    nama = input("Masukkan Namamu: ")
    nim = input("Masukkan NIM kamu: ")
    tahun = input("Masukkan tahun angkatanmu: ")
    file = open(f"{nama_file}.txt", "w")
    file.write(f"Nama: {nama}\n")
    file.write(f"NIM: {nim}\n")
    file.write(f"Angkatan: {tahun}\n")
    file.close()

    print("\nFile Berhasil Dibuat")

def read_file():
    nama_file = input("Masukkan Nama File: ")
    file = open(f"{nama_file}.txt", "r")
    isi = file.read()
    file.close()
    print()
    print(isi)


def add_file():
    nama_file = input("Masukkan Nama File: ")
    data = input("Masukkan Nama Sahabatmu: ")
    data2 = input("Masukkan Catatan Tambahan kamu : ")
    file = open(f"{nama_file}.txt", "a")
    file.write(f"Nama Sahabat : {data}\n")
    file.write(f"Catatan : {data2}\n")
    file.close()
    print("\nData Berhasil Ditambahkan")


while True:
    print("\n===== Program File Handling =====")
    print("1. Membuat dan Menulis File")
    print("2. Membaca File")
    print("3. Menambahkan Text Pada File")
    print("4. Keluar Dari Program")
    pilihan = input("\nMasukkan Pilihan Berupa Angka (1/2/3/4): ")

    if pilihan == "1":
        create_file()
    elif pilihan == "2":
        read_file()
    elif pilihan == "3":
        add_file()
    elif pilihan == "4":
        print("Terima Kasih Sudah Menggunakan Program Saya")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
