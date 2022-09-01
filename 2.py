# Python
# Nama      : Bintang Dwi Marthen
# Nim       : 13521144
# Test Case : 1,2,3

capMax = int(input("Masukkan kapasitas kendaraan: "))
capNow = 0

jlhPelanggan = int(input("Masukkan banyak pelanggan (N): "))

n = int(input("Masukkan banyak data: "))

stat = True

dataNow = [False for i in range(jlhPelanggan)]

for i in range(n):
    s,x=input("Data ke-"+str(i+1)+": ").split()
    x = int(x)
    if s=='+':
        if dataNow[x-1]:
            stat = False
        else:
            dataNow[x-1] = True
            capNow+=1
    else:
        if dataNow[x-1]:
            dataNow[x-1] = False
            capNow-=1
        else:
            stat = False
    if capNow>capMax:
        stat = False
if stat:
    print("Data benar.")
else:
    print("Data tidak benar.")