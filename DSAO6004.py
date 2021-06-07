


def nhap():
    input()
    a = input().strip().split()
    b = input().strip().split()
    return set(a),set(b)

def xuat():
    pass

def xu_ly(a, b):
    union = sorted(b.union(a))
    intersection = sorted(a.intersection(b))
    return union, intersection

if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        a, b = xu_ly(*nhap())
        print(*a, sep=" ")
        print(*b, sep=" ")
        t -= 1