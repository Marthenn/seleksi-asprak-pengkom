# Python
# Nama      : Bintang Dwi Marthen
# Nim       : 13521144
# Test Case : 1,2,3

def F(x,y):
    if x==0:
        return y+1
    if y==0:
        return F(x-1,1)
    return F(x-1,F(x,y-1))

x = int(input("Masukkan x: "))
y = int(input("Masukkan y: "))
print("Nilai F({},{}) = {}".format(x,y,F(x,y)))