#JESLYN JEANNETA
#065002600039
#PRAKTIKUM ALGORITMA PEMROGRAMAN - STRUKTUR KENDALI 2

print("Program Menentukan Hari, Bulan, dan Tahun")
bulan = int(input("Masukkan bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))
while bulan < 1 or bulan > 12:
    print("Bulan tidak valid!")
    bulan = int(input("Masukkan bulan (1-12): "))
nama_bulan = ["Januari", "Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
nama = nama_bulan[bulan-1]
if bulan == 2:
    if tahun % 400 == 0 or (tahun % 4 == 0 and tahun % 100 != 0):
        print(f"Tahun {tahun} merupakan tahun kabisat.")
        jumlah_hari = 29
    else:
        print(f"Tahun {tahun} bukan tahun kabisat.")
        jumlah_hari = 28
elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
    jumlah_hari = 30
else:
    jumlah_hari = 31
if bulan != 2:
    if tahun % 400 == 0 or (tahun % 4 == 0 and tahun % 100 != 0):
        print(f"Tahun {tahun} merupakan tahun kabisat.")
    else:
        print(f"Tahun {tahun} bukan tahun kabisat.")
print(f"Jumlah hari pada bulan {nama}, tahun {tahun} adalah {jumlah_hari} hari")



