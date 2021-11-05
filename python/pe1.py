# Multiples 3 and 5

print ("=" * 50) 
input_maks = int(input("Masukkan batas atas : ")) 
input_multiples1 = int(input("Masukkan bilangan kelipatan yang anda pilih : ")) 
input_multiples2 = int(input("Masukkan bilangan kelipatan yang anda pilih : ")) 


def sum_bilangan():
    list_multiples1 = []
    list_multiples2 = []
    list_total = []
    for a in range (input_maks):
        if a % input_multiples1 == 0:
            list_multiples1.append(a)
        elif a % input_multiples2 == 0:
            list_multiples2.append(a)
    list_total = list_multiples1 + list_multiples2
    jumlah_total = sum(list_total)
    return(jumlah_total)

# =====================
summain = sum_bilangan()
print ("=" * 50) 
print("Jika semua bilangan di bawah", input_maks,"yang merupakan kelipatan", input_multiples1, "dan", input_multiples2, "dijumlahkan, maka menghasilkan bilangan :", summain)

