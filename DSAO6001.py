# sapxep sen ke
import itertools
def nhap():
    input()
    return list(map(int, input().split()))

def xu_ly(ls):
    a = sorted(ls, reverse=True)
    b = sorted(ls)
    lim = len(ls)//2
    ls = list(zip(a,b))[:lim]
    ls  = list(itertools.chain(*ls))
    ls.append(a[lim]) if len(a) %2 else None
    return ls
if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        ls = xu_ly(nhap())
        print(*ls, sep=" ")
        t -= 1