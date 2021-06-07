# tập con bằng nhau

def nhap():
    int(input())
    return input().split()

def xuat():
    pass

def xu_ly(a):
    s = 0
    for i in a:
        s = s + int(i)
    return s%2==0

if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        arr = nhap()
        kq = xu_ly(arr)
        print("YES") if kq == True else print("NO")
        t -= 1