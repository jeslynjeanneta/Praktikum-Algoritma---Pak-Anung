#JESLYN JEANNETA
#065002600039
#PRAKTIKUM ALGORITMA - FUNGSI
def kabisat(tahun):
    if tahun % 400 == 0:
        return True
    elif tahun % 100 == 0:
        return False
    elif tahun % 4 == 0:
        return True
    else:
        return False

def jumlah_hari(bulan, tahun):
    if bulan == 2:
        if kabisat(tahun):
            return 29
        else:
            return 28
    elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
        return 30
    elif 1 <= bulan <= 12:
        return 31
    else:
        return 0
    
print("Program ini akan menentukan jumlah hari dalam bulan tertentu")
print("Masukkan 0 untuk menghentikan program")

while True:
    bulan = int(input("Masukkan bulan (1-12): "))
    if bulan == 0:
        break
    if bulan == 2 :
        tahun = int(input("Masukkan tahun (e.g., 2021): "))
    else :
        tahun = int(input("Masukkan tahun : "))
    
    hari = jumlah_hari(bulan, tahun)
    if hari == 0:
        print("Bulan tidak valid!")
    else:
        print(f"{hari} hari dalam sebulan")

print ("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")



