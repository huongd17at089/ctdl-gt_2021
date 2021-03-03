# nhị phân kế tiếp

def nhap():
    a = []
    a[:0] = input()
    return a

def xuat(a):
    print("".join(str(elem) for elem in a))

def xu_ly(a):
    n = len(a) -1
    while(n >= 0 and int(a[n]) == 1):
        a[n] = 0
        n -= 1
    if n < 0 :
        return
    a[n] = 1


if __name__ == "__main__":
    t = int(input())
    kq = ""
    while(t > 0):
        xau = nhap()
        xu_ly(xau)
        xuat(xau)
        t -= 1