# Project Euler largest prime factor
# ===================================
# Faktor prima dari 13195 adalah 5, 7, 13, dan 29
# Tentukan faktor prima terbesar dari 600851475143

print("=" * 15, "FAKTOR PRIMA TERBESAR", "=" * 15)
print("=" * 53)
input_bilangan = int(input("Masukkan bilangan yang ingin diketahui faktor prima terbesarnya : ")) # Masukkan bilangan yang ingin diketahui faktor primanya (dalam kasus ini adalah 600851475143) 

# code untuk mencari daftar bilangan prima dibawah input yang dimasukkan
def cek_prima(cek):
    test_bol = []
    for x in range(2, cek):
        if cek % x == 0:
            test_bol.append(False)
        else:
            test_bol.append(True)
    test_prima = True
    for i in test_bol:
        if i == False:
            test_prima = False
            break
        if i == True:
            pass
    temp = test_prima
    if temp == True:
        list_prima.append(cek)        
def cek_bil(bil):
    for i in range(2, bil + 1):
        cek_prima(i) 
    return list_prima

# ===============
list_prima = []        
cek_bil(input_bilangan)

# Code untuk menentukan faktor prima dari input yang dimasukkan
list_faktor_prima = []
for test in list_prima:
    if input_bilangan % test == 0:
        list_faktor_prima.append(test)
    else:
        pass
prima_terbesar = list_faktor_prima[-1]
print("Faktor prima dari bilangan", input_bilangan, "adalah", list_faktor_prima)
print("Faktor prima terbesarnya adalah", prima_terbesar)


