#  hoán vị ngược

def nhap():
    return int(input())

def xuat(a):
    print("".join(str(i) for i in a), end =" ")

def dao(a,b):
    return b, a

def sinh(a):
    n = len(a) - 1
    i = 0
    while i < n and a[i] >= a[i + 1]:
        i += 1
    # print(i)
    if i == 0:
        return True
    k = 0
    while a[k] < a[i]:
        k += 1
    # print(k)
    a[k], a[i] = dao(a[k], a[i])
    r = i - 1
    s = 0
    while (r >= s):
        a[r], a[s] = dao(a[r], a[s])
        r -= 1
        s += 1
    return False

def xu_ly(n):
    xau = [i for i in range(n, 0, -1)]
    # print(xau)
    kq = ""
    dung = False
    while( not dung):
        # xuat(xau)
        kq = kq + "".join(str(i) for i in xau) + " "
        dung = sinh(xau)
        # dung = True
    return kq
if __name__ == "__main__":
    t = int(input())
    kq = ""
    while(t > 0):
        n = nhap()
        kq = xu_ly(n)
        print(kq)
        t -= 1

