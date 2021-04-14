# Project Euler multiples 3 and 5
# =====================================================================================
# Jika sebuah bilangan di bawah 10 yang merupakan kelipatan 3 dan 5 adalah 3, 5, 6, dan 9.
# Maka jumlahkan semua bilangan yang merupakan kelipatan 3 dan 5 dibawah 1000

print ("=" * 50) 
input_maks = int(input("Masukkan batas atas : ")) # Masukkan batas bilangan (dalam kasus ini batas bilangannya adalah 1000)
input_multiples1 = int(input("Masukkan bilangan kelipatan yang anda pilih : ")) # Masukkan bilangan kelipatan pertama {dalam kasus ini adalah 3)
input_multiples2 = int(input("Masukkan bilangan kelipatan yang anda pilih : ")) # Masukkan bilangan kelipatan pertama {dalam kasus ini adalah 5)

# Kode program untuk menjumlahkan semua bilangan kelipatan yang dipilih dan dibawah batas yang dipilih
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

