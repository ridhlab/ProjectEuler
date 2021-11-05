# Largest Palindrome Product

print("=" * 15, "BILANGAN PALINDROM", "=" * 15)
print("=" * 50)
print("Bilangan palindrom adalah bilangan yang jka dibaca \ndari kiri ataupun dari kanan menghasilkan bilangan \nyang sama")
input_digit = int(input("Masukkan digit bilangan")) 


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



        

