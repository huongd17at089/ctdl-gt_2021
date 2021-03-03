# xâu AB độ dài n



def nhap():
    return int(input())

def xuat(xau):
    kq = ""
    for i in xau:
        kq = kq + chr(ord('A') + i)
    print(kq, end=" ")

def sinh(xau):
    n = len(xau)
    j = n - 1
    while(xau[j] == 1 and j > 0):
        j -= 1
    xau[j] = 1
    for i in range(j+1,n):
        xau[i] = 0
    if j == 0:
        return  True
    return False

def xu_ly(n):
    dung = False
    xau = [0 for i in range(n)]
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