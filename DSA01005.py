# sinh hoán vị


def nhap():
    return int(input())

def xuat(a):
    print("".join(str(i) for i in a), end =" ")

def dao(a,b):
    return b, a

def sinh(a):
    n = len(a) - 1
    i = n - 1
    while i >=0 and a[i] >= a[i+1]:
        i -= 1
    if i < 0:
        return True
    k = n
    while a[k] < a[i]:
        k -= 1
    a[k] , a[i] = dao(a[k] , a[i])
    r = i + 1
    s = n
    while( r <= s) :
        a[r], a[s] = dao(a[r], a[s])
        r += 1
        s -= 1
    return False



def xu_ly(n):
    xau = [i for i in range(1,n+1)]
    dung = False
    while( not dung):
        xuat(xau)
        dung = sinh(xau)


if __name__ == "__main__":
    t = int(input())
    kq = ""
    while(t > 0):
        n = nhap()
        xu_ly(n)
        t -= 1