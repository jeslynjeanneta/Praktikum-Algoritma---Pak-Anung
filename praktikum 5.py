#JESLYN JEANNETA
#065002600039
#PRAKTIKUM ALGORITMA - STRUKTUR KENDALI
total = 0
i = 0
while True:
    huruf = input("Masukkan nilai (atau enter untuk berhenti): ")
    if huruf == "":
        break
    huruf = huruf.upper()
    if huruf == "A":
        nilai = 4.00
    elif huruf == "A-":
        nilai = 3.75
    elif huruf == "B+":
        nilai = 3.50
    elif huruf == "B":
        nilai = 3.00
    elif huruf == "B-":
        nilai = 2.75
    elif huruf == "C+":
        nilai = 2.50
    elif huruf == "C":
        nilai = 2.00
    elif huruf == "D":
        nilai = 1.50
    elif huruf == "E":
        nilai = 1.25
    else:
        print("Masukkan nilai dengan benar!")
        continue

    total += nilai
    i += 1
    print (f"Nilainya adalah {nilai}")

if i > 0:
    rata_rata = total / i
    print(f"Rata-ratanya adalah: {rata_rata:.2f}")
else:
    print("Belum ada nilai yang dimasukkan.")
