# noi day
def nhap():
    input()
    return list(map(int, input().split()))


def xu_ly(ls):
    ls.sort()
    sum = 0
    while len(ls) != 1:
        a = ls.pop(0)
        b = ls.pop(0)
        sum = sum +a + b
        ls.append(a+b)
        ls.sort()
    return sum

if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        print(xu_ly(nhap()))
        t -= 1