def nhap():
    input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cv = list(zip(a,b))
    return cv


def xu_ly(ls):
    ls = sorted(ls, key = lambda x: x[1])
    i = 0
    j = 1
    dem = 1
    l = len(ls)
    while j != l:
        if ls[i][1] <= ls[j][0]:
            dem = dem + 1
            i = j
        j = j  + 1

    return dem


if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        print(xu_ly(nhap()))
        t -= 1