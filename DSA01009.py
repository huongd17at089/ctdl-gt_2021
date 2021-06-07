# DSA01009 xâu AB đặc biệt
import re

def nhap():
    inp = input().split()
    return int(inp[0]), int(inp[1])

def xuat(xau):
    kq = ""
    for i in xau:
        kq = kq + chr(ord('A') + i)
    return kq

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

def check(a, k):
    dem0 = 0
    demsub = 0
    for i in a:
        if i == 0:
            dem0 += 1
        # if dem0 > k:
        #     return False
        if dem0 == k:
            demsub += 1
            dem0 = 0
    return demsub == 1


def xu_ly(n, k):
    dung = False
    xau = [0 for i in range(n)]
    sub_str = "".join(['0' for i in range(k)])
    kq = []
    while( not dung):
        if(len(re.findall('(?='+ sub_str + ')',"".join(str(i) for i in xau))) == 1):
            a = [chr(ord('A') + i ) for i in xau]
            kq.append("".join(a))
        dung = sinh(xau)
    return kq

if __name__ == "__main__":
    n , k= nhap()
    kq = xu_ly(n, k)
    print(len(kq))
    for i in kq:
        print(i)

num = 123
sub_str = "1"*k
bin_num = bin(num)[2:]
print(len(re.findall('(?='+ sub_str + ')',"".join(str(i) for i in bin_num))) == 1)