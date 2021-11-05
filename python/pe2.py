# Even Fibonacci Numbers

print ("=" * 50) 
input_maks = int (input("Masukkan batas atas : "))
input_ganjil_genap = input("Pilih bilangan fibonacci ganjil atau genap : ") 


def fibonacci(bil):
    x = bil
    if x == 0 :
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(bil-2) + fibonacci(bil-1)


def jumlah_fibonacci():
    list_fibonacci_genap = [] 
    list_fibonacci_ganjil = []
    i = 0
    x = len(deret_fibonacci)
    for i in range (x):
        if deret_fibonacci[i] % 2 == 0:
            list_fibonacci_genap.append(deret_fibonacci[i]) 
        elif deret_fibonacci[i] % 2 != 0:
            list_fibonacci_ganjil.append(deret_fibonacci[i]) 
        i += 1
    jumlah_bilangan_ganjil = sum(list_fibonacci_ganjil) 
    jumlah_bilangan_genap = sum(list_fibonacci_genap) 
    if input_ganjil_genap == "ganjil":
        return jumlah_bilangan_ganjil
    elif input_ganjil_genap == "genap":
        return jumlah_bilangan_genap
    else:
        return "MASUKKAN DATA DENGAN BENAR!!!!" 
        

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

