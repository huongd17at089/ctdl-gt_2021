# DSA01010 tập quân sự
import functools

def nhap():
    temp = input().split()
    n = int(temp[0])
    k = int(temp[1])
    xau = [int(i) for i in input().split()]
    return n, k, xau

def xu_ly(n, k, xau):
    a = xau.copy()
    i = k - 1
    #  tại vì mảng điền từ index 0
    while i >= 0 and a[i] == n-k+i+1:
        i -= 1
    if(i < 0):
        return k
    a[i] = a[i] + 1
    for j in range(i+1,k):
        a[j] = a[j-1] + 1
    count = 0
    for i in xau:
        if (i not in a):
            count += 1
    return count


def xuat(a):
    for i in a:
        print(i, end =" ")


if __name__ == "__main__":
    t = int(input())
    kq = ""
    while(t > 0):
        n, k, xau = nhap()
        print(xu_ly(n, k, xau))
        t -= 1