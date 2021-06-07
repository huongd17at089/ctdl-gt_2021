# dãy con liên tiếp tổng max

def nhap():
    input()
    return [int(x) for x in input().split()]

def xu_ly(l):
    ls = [l[0]]
    m = l[0]
    for i in range (1, len(l)):
        m = max(m + l[i], l[i-1] + l[i])
        ls.append(m)
    return max(ls);

if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        l = nhap()
        print(max(max(l), xu_ly(l)))
        t -= 1