# tập con kế tiếp

def nhap():
    temp = input().split()
    n = int(temp[0])
    k = int(temp[1])
    xau = input().split()
    return n, k, xau

def xu_ly(n, k, a):
    i = k - 1
    #  tại vì mảng điền từ index 0
    while i >= 0 and int(a[i] )== n-k+i+1:
        i -= 1
    if(i >= 0):
        a[i] = int(a[i]) + 1
    else :
        i += 1
        a[i] = 1
    for j in range(i+1,k):
        a[j] = a[j-1] + 1


def xuat(a):
    kq = ""
    for i in a:
        kq = kq + str(i) + " "
    print(kq)


if __name__ == "__main__":
    t = int(input())
    kq = ""
    while(t > 0):
        n, k, xau = nhap()
        xu_ly(n, k, xau)
        xuat(xau)
        t -= 1