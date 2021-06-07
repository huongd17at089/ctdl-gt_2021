# DSA01015

def nhap():
    a = input().split()
    return int(a[0]), int(a[1])

def xuat(a):
    print("".join(str(elem*9) for elem in a), end=" ")

def sinh(a):
    n = len(a) -1
    while(n >= 0 and int(a[n]) == 1):
        a[n] = 0
        n -= 1
    if n < 0 :
        return True
    a[n] = 1
    return False

def xu_ly(n, k):
    xau = [0 for i in range(n)]
    dung = False
    while( not dung):
        if( sum(xau) == k):
            xuat(xau)
        dung = sinh(xau)


if __name__ == "__main__":
    t = int(input())
    kq = ""
    while(t > 0):
        n, k = nhap()
        xu_ly(n, k)
        t -= 1