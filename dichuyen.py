
def nhap():
   m = {"X": 0, ".": 1}
   n = int(input())
   x = []
   for i in range(0,n):
       row = list(map(lambda x: m[x] ,input()))
       x.append(row)
   a, b, c, d = list(map(int,input().split()))
   return n, a, b, c, d, x

def xu_ly(n, a, b, c, d, X):
    xx = [0,-1,0,1]
    yy = [-1,0,1,0]
    queue = []
    queue.append((a,b,0, -1))
    while queue:
        curr = queue.pop(0)
        print(curr)
        for i in range(4):
            x = curr[0] + xx[i]
            y = curr[1] + yy[i]
            if x >= 0 and x < n and y >= 0 and y < n and X[x][y]:
                if((x,y) == (c,d)) :
                    return curr[2]
                queue.append((x, y, curr[2] + int(bool(curr[3] != i%2)), i%2))
                # X[x][y] = 0

if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        n, a, b, c, d, x = nhap()
        print(0)  if (a,b) == (c,d) else print(xu_ly(n, a, b, c, d, x))
        t -= 1
