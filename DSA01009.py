# DSA01009 xâu AB đặc biệt
import re

def nhap():
    inp = input().split()
    return int(inp[0]), int(inp[1])

def xuat(xau):
    kq = ""
    for i in xau:
        kq = kq + chr(ord('A') + i)
    print(kq)

def sinh(xau):
    n = len(xau)
    j = n - 1
    while(xau[j] == 1 and j >= 0):
        xau[j] = 0
        j -= 1
    if(j < 0):
        return True
    xau[j] = 1
    return False

def xu_ly(n, k):
    dung = False
    xau = [0 for i in range(n)]
    sub_str = "".join(['0' for i in range(k)])
    while( not dung):
        if(len(re.findall('(?='+ sub_str + ')',"".join(str(i) for i in xau))) == 1):
            xuat(xau)
        dung = sinh(xau)

if __name__ == "__main__":
    n , k= nhap()
    xu_ly(n, k)
