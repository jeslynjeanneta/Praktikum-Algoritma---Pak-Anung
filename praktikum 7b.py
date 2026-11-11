#JESLYN JEANNETA
#065002600039
#FUNGSI PADA PEMROGRAMAN PYTHON-LATIHAN
def ordinal(angka):
    if angka % 100 == 11 or angka % 100 == 12 or angka % 100 == 13:
        return "th"
    elif angka % 10 == 1:
        return "st"
    elif angka % 10 == 2:
        return "nd"
    elif angka % 10 == 3:
        return "rd"
    else:
        return "th"

print ("Ordinal Number")
print ("ketik 0 untuk menghentikan program")
while True:
    angka = int(input("Masukkan angka  : "))
    if angka == 0 :
        break
    hasil = ordinal(angka)
    print(f"({angka}, '{hasil}')")

print("Terima kasih telah menggunakan program saya")

        
