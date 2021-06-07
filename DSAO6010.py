# sap xep chu so
import re
def nhap():
    input()
    return input()

def xu_ly(str):
    return sorted(set(re.sub(r'\s', "", str)))

if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        ls = xu_ly(nhap())
        print(*ls, sep=" ")
        t -= 1