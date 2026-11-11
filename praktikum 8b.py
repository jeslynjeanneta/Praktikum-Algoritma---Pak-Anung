#JESLYN JEANNETA
#065002600039
#FUNGSI REKURSIF
def perpangkatan(base, power) :
    if  power == 0 :
        return 1
    else :
        return base*perpangkatan(base, power-1)
while True :
    print("Ini merupakan program pemangkatan negatif dan positif, tekan enter untuk berhenti")
    base = input("Masukkan angka : ")
    if base == "" :
        break
    base = int(base)
    power = int(input("Masukkan pangkat : "))
    if  power < 0 :
        print ("Maaf tolong input kembali dengan benar")
    else :
        hasil = perpangkatan(base,power)
        print (f"Hasilnya adalah : {hasil}")
   
print("Program selesai")
