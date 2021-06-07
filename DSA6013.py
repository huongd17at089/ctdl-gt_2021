# so lan xuat hien

if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        n , x = input().strip().split()
        ls = input().strip().split()
        ls = list(filter(lambda a: a == x, ls))
        n = len(ls)
        print(n) if n else print(-1)
        t -= 1