# Python
# Nama      : Bintang Dwi Marthen
# Nim       : 13521144
# Test Case : 1,2,3

n = int(input("Masukkan N: "))

arr = [['' for i in range(n+2)]for j in range(n+2)]
prev = [['' for i in range(n+2)]for j in range(n+2)]
stat = [[0 for i in range(n+2)]for j in range(n+2)]

print("Masukkan isi peta:")
for i in range(1,n+1):
    s=input()
    for j in range(n):
        arr[i][j+1]=s[j]

m = int(input("Masukkan M: "))

for k in range(m+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            prev[i][j] = arr[i][j]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][j]!='O':
                if arr[i][j]=='P':
                    stat[i][j]+=1
                    if stat[i][j]==4:
                        arr[i][j]='N'
                        stat[i][j]=1
                else:
                    count = 0
                    if prev[i-1][j-1]=='P':
                        count+=1
                    if prev[i-1][j]=='P':
                        count+=1
                    if prev[i-1][j+1]=='P':
                        count+=1
                    if prev[i][j+1]=='P':
                        count+=1
                    if prev[i+1][j+1]=='P':
                        count+=1
                    if prev[i+1][j]=='P':
                        count+=1
                    if prev[i+1][j-1]=='P':
                        count+=1
                    if prev[i][j-1]=='P':
                        count+=1
                    if count>1:
                        arr[i][j]='P'

print("Peta Minggu {}:".format(m))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(arr[i][j],end='')
    print()