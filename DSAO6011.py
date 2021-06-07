# # tong gan 0 nhat
# import math
# from itertools import zip_longest
# def nhap():
#     input()
#     return list(map(int, input().strip().split()))
#
# def xu_ly(ls):
#     a = list(filter(lambda x: x > 0, ls)).sort() or []
#     b = sorted(list(filter(lambda x: x < 0, ls))) or []
#     cap_tong = list(zip_longest(a, b, fillvalue=math.inf))
#     temp = min(list(map(lambda x : math.fabs(x[0] + x[1]), cap_tong)))
#     if 0 in ls:
#         if not a :
#             m = min(b[0], b[0] + b[1])
#         elif not b :
#             m = min(a[0], a[0] + a[1])
#         else:
#             m = min(a[0], b[0], temp)
#     else:
#         if not a :
#             m = b[0] + b[1]
#         elif not b :
#             m = a[0] + a[1]
#         else:
#             m = temp
#
#     # cap_tong = list(zip_longest(a, b, fillvalue=math.inf))
#     # m = min(list(map(lambda x : math.fabs(x[0] + x[1]), cap_tong)))
#     # return m
# if __name__ == "__main__":
#     t = int(input())
#     while(t > 0):
#         print (xu_ly(nhap()))
#         t -= 1