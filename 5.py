# Python
# Nama      : Bintang Dwi Marthen
# Nim       : 13521144
# Test Case : 1,2,3


n = int(input("Masukkan ukuran peta: "))

arr = [['' for j in range(n+2)] for i in range(n+2)]

print("Masukkan isi peta:")
for i in range(1,n+1):
    s=input()
    for j in range(n):
        arr[i][j+1]=s[j]
        if s[j]=='S':
            xNow = j+1
            yNow = i
        elif s[j]=='E':
            xTarget = j+1
            yTarget = i

print("Langkah-langkah: ",end='')

belum = True #belum sampai lokasi

while(belum):
    if arr[yNow][xNow+1]=='X' or arr[yNow][xNow+1]=='E':
        arr[yNow][xNow]='.'
        arr[yNow][xNow+1]='S'
        print('E',end='')
        xNow+=1
    elif arr[yNow][xNow-1]=='X' or arr[yNow][xNow-1]=='E':
        arr[yNow][xNow]='.'
        arr[yNow][xNow-1]='S'
        print('W',end='')
        xNow-=1
    elif arr[yNow+1][xNow]=='X' or arr[yNow+1][xNow]=='E':
        arr[yNow][xNow]='.'
        arr[yNow+1][xNow]='S'
        print('S',end='')
        yNow+=1
    else:
        arr[yNow][xNow]='.'
        arr[yNow-1][xNow]='S'
        print('N',end='')
        yNow-=1
    if yNow==yTarget and xNow==xTarget:
        belum = False
print() #budayakan akhiri dengan newline selalu