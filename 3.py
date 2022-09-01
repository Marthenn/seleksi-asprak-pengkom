# Python
# Nama      : Bintang Dwi Marthen
# Nim       : 13521144
# Test Case : 1,2,3

n = int(input("Masukkan panjang string: "))
s = input("Masukkan string: ")

charNow = s[0]
jlhNow = 1

print("Hasil: ",end='')

for i in range(1,n):
    if s[i]==charNow:
        jlhNow+=1
    else:
        print(charNow+str(jlhNow),end='')
        charNow=s[i]
        jlhNow=1

print(charNow+str(jlhNow))