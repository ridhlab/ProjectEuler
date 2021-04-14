# Project Euler even finbonacci numbers
# =========================================================================================
# Bilangan fibonacci adalah bilangan yang dihasilkan dari penjumlahan 2 bilangan sebelumnya
# Contoh bilangan fibonacci adalah : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 dst.
# Jumlahkan bilangan fibonacci genap di bawah 4000000

print ("=" * 50) 
input_maks = int (input("Masukkan batas atas : ")) # Masukkan batas atas (dalam kasus ini adalah 4000000)
input_ganjil_genap = input("Pilih bilangan fibonacci ganjil atau genap : ") # Tentukan bilangan fibonacci genap/ganjil (dalam kasus ini adalah genap)

# Kode program bilangan fibonacci
def fibonacci(bil):
    x = bil
    if x == 0 :
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(bil-2) + fibonacci(bil-1)

# Kode program untuk menjumlah bilangan fibonacci ganjil/genap
def jumlah_fibonacci():
    list_fibonacci_genap = [] # Membuat list kosong yang nantinya akan menampung bil fibonacci genap
    list_fibonacci_ganjil = [] # Membuat list kosong yang nantinya akan menampung bil fibonacci ganjil
    i = 0
    x = len(deret_fibonacci)
    for i in range (x):
        if deret_fibonacci[i] % 2 == 0:
            list_fibonacci_genap.append(deret_fibonacci[i]) # Memasukkan bilangan fibonacci genap ke dalam list
        elif deret_fibonacci[i] % 2 != 0:
            list_fibonacci_ganjil.append(deret_fibonacci[i]) # Memasukkan bilangan fibonacci ganjil ke dalam list
        i += 1
    jumlah_bilangan_ganjil = sum(list_fibonacci_ganjil) # Menjumlahkan semua bilangan yg ada di list fibonacci ganjil
    jumlah_bilangan_genap = sum(list_fibonacci_genap) # Menjumlahkan semua bilangan yg ada di list fibonacci genap
    if input_ganjil_genap == "ganjil":
        return jumlah_bilangan_ganjil
    elif input_ganjil_genap == "genap":
        return jumlah_bilangan_genap
    else:
        return "MASUKKAN DATA DENGAN BENAR!!!!" 
        
# ==============
print ("=" * 50)         
deret_fibonacci = []
i = 0
deret_fibonacci.append(0)
while deret_fibonacci[i] < input_maks:
    deret_fibonacci.append(fibonacci(i+1))
    i += 1
if deret_fibonacci[-1] >= input_maks:
    del deret_fibonacci[-1]
jumlah = jumlah_fibonacci()
if jumlah == "MASUKKAN DATA DENGAN BENAR!!!!":
    print (jumlah)
else:
    print("Jika semua bilangan fibonacci", input_ganjil_genap, " yang kurang dari", input_maks, "dijumlahkan, maka hasilnya adalah :", jumlah)

