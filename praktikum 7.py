#JESLYN JEANNETA
#065002600039
#FUNGSI PADA PEMROGRAMAN PYTHON-LATIHAN
import math

def cek_prima(a):
    if a == 2:
        return True
    if a <= 1:
        return False
    if a % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(a)) + 1, 2):
        if a % i == 0:
            return False
    return True

def cetak_hasil(a, cek_prima):
    if cek_prima:
        return f"{a} adalah bilangan prima"
    else:
        return f"{a} bukanlah bilangan prima"

a = int(input("Masukkan angka: "))
hasil = cetak_hasil(a, cek_prima(a))
print(hasil)
