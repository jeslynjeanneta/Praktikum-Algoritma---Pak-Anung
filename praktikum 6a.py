#JESLYN JEANNETA
#065002600039
#PRAKTIKUM ALGORITMA - FUNGSI
def nilai(huruf):
    if huruf == "A":
        return 4.00
    elif huruf == "A-":
        return 3.75
    elif huruf == "B+":
        return 3.50
    elif huruf == "B":
        return 3.00
    elif huruf == "B-":
        return 2.75
    elif huruf == "C+":
        return 2.50
    elif huruf == "C":
        return 2.00
    elif huruf == "D":
        return 1.50
    elif huruf == "E":
        return 1.25
total = 0
jumlah = 0 
while True :
    huruf = input("Masukkan nilai (atau enter untuk berhenti): ")
    if huruf == "":
        break
    huruf = huruf.upper()
    nilaihuruf = nilai(huruf)
    print (f"nilai = {nilaihuruf}")
    if nilaihuruf == None :
        print ("Nilai tidak valid")
    else :
        total += nilaihuruf
        jumlah += 1


if jumlah > 0:
    rata_rata = total / jumlah
    print(f"Rata-rata nilai = {rata_rata}")
else:
    print("Belum ada nilai yang dimasukkan.")   
    
    
    
