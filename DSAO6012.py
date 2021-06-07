# k phan tu lon nhat

if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        n , k = list(map(int, input().strip().split()))
        ls = sorted(list(map(int, input().strip().split())), reverse=True)
        print(*ls[:k], sep=" ")
        t -= 1