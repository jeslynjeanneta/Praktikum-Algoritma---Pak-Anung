#JESLYN JEANNETA
#065002600039
#FUNGSI REKURSIF

def penjumlahan(jumlah, urutan=1):
    if urutan > jumlah:
        return 0
    else:
        bil = int(input(f"Masukkan bilangan ke-{urutan}: "))
        return bil + penjumlahan(jumlah, urutan+1)

jumlah = int(input("Masukkan Jumlah: "))
hasil = penjumlahan(jumlah)

print("Hasil dari penjumlahan adalah:", hasil)
