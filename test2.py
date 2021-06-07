# tap k tong s

def nhap():
    s = input().split()
    return int(s[0]), int(s[1]), int(s[2])

# def xuat(a):
#     print("".join(str(a[i]) for i in  range(1, len(a))), end=" ")

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

def xu_ly(n, k, s):
    dem = 0
    xau = [i for i in range(0, k+1)]
    dung = False
    while( not dung):
        # xuat(xau)
        if(sum(xau) == s):
            dem += 1
        # kq = kq + "".join(str(xau[i]) for i in  range(1, len(xau))) + " "
        dung = sinh(n, k, xau)
    return dem
if __name__ == "__main__":
    # t = int(input())
    # kq = ""
    s = input().split()
    while(s):
        n, k , s = nhap()
        if( n == 0 and s == 0 and k == 0):
            break;
        print(xu_ly(n , k, s))
        # t -= 1