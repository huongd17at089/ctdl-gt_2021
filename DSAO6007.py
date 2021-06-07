# sap xep lien tuc
def nhap():
    input()
    return list(map(int, input().strip().split()))


def xu_ly(ls):
    sorted_ls = sorted(ls)
    begin = 0
    end = 0
    n = len(ls)
    for i in range(n):
        if not begin and ls[i] != sorted_ls[i] :
            begin = i + 1
        if not end and   ls[n-i-1] != sorted_ls[n-i-1]:
            end = n-i
        if (begin and end ) or i > n-i-1:
            break
    return begin, end

if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        a, b = xu_ly(nhap())
        print(a, b)
        t -= 1