# sinh tổ hợp

def nhap():
    s = input().split()
    return int(s[0]), int(s[1])

def xuat(a):
    print("".join(str(a[i]) for i in  range(1, len(a))), end=" ")

def sinh(n, k, a):
    j = k
    while(j > 0 and int(a[j]) == n-k+j):
        j -= 1
    if(j == 0):
        return True
    a[j] += 1
    for i in range(j+1, k +1):
        a[i] = a[i-1] + 1
    return False

def xu_ly(n, k):
    xau = [i for i in range(0, k+1)]
    dung = False
    while( not dung):
        xuat(xau)
        dung = sinh(n, k, xau)

if __name__ == "__main__":
    t = int(input())
    kq = ""
    while(t > 0):
        n, k = nhap()
        xu_ly(n , k)
        t -= 1