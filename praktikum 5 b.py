#JESLYN JEANNETA
#065002600039
#PRAKTIKUM ALGORITMA - STRUKTUR KENDALI
total = 0
while True:
    umur = input("Masukkan umur (kosong untuk selesai): ")
    if umur == "":
        break
    umur = int(umur)
    if umur <= 2:
        harga = 0
        tampilan_harga = "Gratis"
    elif 3 <= umur <= 12:
        harga = 14.00
        tampilan_harga = f"${harga}"
    elif umur >= 65:
        harga = 18.00
        tampilan_harga = f"${harga}"
    else:
        harga = 23.00
        tampilan_harga = f"${harga}"
    total += harga
    print(f"Harga: {tampilan_harga}")
    
print(f"Total pembayaran adalah: ${total}")
while True:
    uang = int(input("Masukkan jumlah uang: "))
    if uang >= total:
        kembalian = uang - total
        print(f"Kembalian: ${kembalian}, Terimakasih")
        break 
    else:
        print("Uangnya kurang, silakan masukkan uang kembali!")




