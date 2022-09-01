# Python
# Nama      : Bintang Dwi Marthen
# Nim       : 13521144
# Test Case : 1,2,3

def minimal(a,b):
    if a>b:
        return b
    return a

n = int(input("Masukkan panjang string: "))
s = input("Masukkan string: ")
ans = 0
jlhO=jlhN=jlhL=jlhI=jlhE=0

for i in range(n):
    if s[i]=='O':
        jlhO+=1
    elif s[i]=='N':
        jlhN+=1
    elif s[i]=='L':
        jlhL+=1
    elif s[i]=='I':
        jlhI+=1
    elif s[i]=='E':
        jlhE+=1

ans = minimal(jlhO,minimal(jlhE,minimal(jlhL,minimal(jlhI,int(jlhN/2)))))

print("Jumlah kata ONLINE yang dapat dibentuk:",ans)