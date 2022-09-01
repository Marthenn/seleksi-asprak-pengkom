# Python
# Nama      : Bintang Dwi Marthen
# Nim       : 13521144
# Test Case : 1,2,3

ans = 0
n = int(input("Masukkan banyak kotak: "))
s = input("Masukkan konfigurasi kotak: ")

arr = [-1 for i in range(n)]

for i in range(n):
    arr[i]=int(s[i])

for i in range(n):
    start = now = arr[i]
    belum = True
    while belum and start!=-1:
        prev = now
        now = arr[now-1]
        arr[prev-1]=-1
        if now==-1:
            ans+=1
            belum = False

print("Terdapat {} buah rantai.".format(ans));