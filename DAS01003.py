# Hoán vị kế tiếp

def nhap():
    int(input())
    xau = input().split()
    return xau

def dao(a,b) :
    return b, a

def hv_ke_tiep(a):
    n = len(a) - 1
    j =  n-1
    # vị trí có chỉ số j đầu tiên thỏa mãn aj < aj+1
    while j >= 0 and a[j] >= a[j+1]:
        j -= 1
    if j >= 0 :
        k = n
        # ak là số nhỏ nhất còn lớn hơn aj
        while a[k] < a[j]:
            k -= 1
        # Đổi chỗ aj cho ak
        a[j] , a[k] = dao(a[j], a[k])
        r = j + 1
        s = n
        # Lật ngược đoạn aj+1, …, an.
        while r <= s:
            a[r], a[s] = dao(a[r], a[s])
            r += 1
            s -= 1




if __name__ == "__main__":
    t = int(input())
    kq = ""
    while(t > 0):
        hoan_vi = nhap()
        hv_ke_tiep(hoan_vi)
        for i in hoan_vi:
            kq = kq + str(i) + " "
        print(kq)
        t -= 1