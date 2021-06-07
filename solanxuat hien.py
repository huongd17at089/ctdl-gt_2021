from collections import OrderedDict

def nhap():
    input()
    return list(map(int,input().split()))


def xuat(ls):
    s = ""
    for x, i in ls.items():
        s = s + (str(x) + " ")*i
    print(s)

def xu_ly(ls):
    dic = {}
    for x in ls:
        dic[x] = dic.get(x, 0) + 1
    dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    return dic

if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        xuat(xu_ly(nhap()))
        t -= 1