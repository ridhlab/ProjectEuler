# Project Euler largest palindrome product
# =========================================================================================
# Bilangan palindrom adalah bilangan yang jika dibaca dari awal maupun akhir adalah sama
# Contohnya 121, 12321, 45754, 108801\
# Bilangan palindrom terbesar yang bisa dibuat dengan 2 bilangan 2 digit adalah 9009, karena 9009 = 99 * 91 
# Tentukan bilangan palindrom terbesar yang bisa dibuat dengan 2 bilangan 3 digit

print("=" * 15, "BILANGAN PALINDROM", "=" * 15)
print("=" * 50)
print("Bilangan palindrom adalah bilangan yang jka dibaca \ndari kiri ataupun dari kanan menghasilkan bilangan \nyang sama")
input_digit = int(input("Masukkan digit bilangan")) # Masukkan digit bilangan (dalam kasus ini adalah 3 digit)

# Code untuk menentukan apakah sebuah bilangan itu palidrom atau bukan
def cek_palindrom(bil):
    str_num = str(bil)
    panjang = len(str_num)
    for x in range(panjang//2):
        if str_num[x] == str_num[panjang - 1 - x]:
            cek = True
        else:
            cek = False
            break
    return cek
    
input_ = input_digit
max_digit  = 10 ** input_ - 1
min_digit = 10 ** (input_ - 1)
list_palindrom = []

for i in range(max_digit, min_digit, -1):
    for x in range(i, min_digit, -1):
        a = i * x
        cek_palindrom(a)
        if cek_palindrom(a) == True:
            list_palindrom.append(a)
        else:
            pass
list_palindrom.sort()
result = list_palindrom[-1]
print("Bilangan palindrom terbesar yang dapat dibentuk \ndari", input_digit, "digit, adalah", result)



        

