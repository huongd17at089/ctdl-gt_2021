def nhap():
    input()
    return list(map(int, input().split()))



def xu_ly(ls):
    M = 1e9 + 7
    sum = 0
    for ind , a in enumerate(sorted(ls)):
        sum = (sum + a*ind%M)%M
    return int(sum)

if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        print(xu_ly(nhap()))
        t -= 1