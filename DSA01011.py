# DSA01011 hoán vị chuỗi số


def nhap():
    inp = input().split()
    l = []
    l[:0] = inp[1]
    return l

def dao(a,b) :
    return b, a

def xu_ly(a):
    n = len(a) - 1
    j = n - 1
    # vị trí có chỉ số j đầu tiên thỏa mãn aj < aj+1
    while j >= 0 and a[j] >= a[j + 1]:
        j -= 1
    if j < 0:
        return "BIGGEST"
    k = n
    # ak là số nhỏ nhất còn lớn hơn aj
    while a[k] < a[j]:
        k -= 1
    # Đổi chỗ aj cho ak
    a[j], a[k] = dao(a[j], a[k])
    r = j + 1
    s = n
    # Lật ngược đoạn aj+1, …, an.
    while r <= s:
        a[r], a[s] = dao(a[r], a[s])
        r += 1
        s -= 1
    return "".join(a)
if __name__ == "__main__":
    t = int(input())
    for i in range(1, t+1) :
        xau = nhap()
        print(i, xu_ly(xau))