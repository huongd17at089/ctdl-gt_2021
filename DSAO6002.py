# sap xep tri tuyet doi
import math

if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        _, x = list(map(int, input().split()))
        ls = list(map(int, input().split()))
        res = sorted(ls, key=lambda a: math.fabs(x-a))
        print(*res, sep=" ")
        t -= 1

