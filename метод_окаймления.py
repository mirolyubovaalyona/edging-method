import numpy as np
from math import sqrt



def f(a, n):
    x=[0]*n
    dx=[0]*n
    c=[0]*n
    c[0]=-a[1][2]/a[1][1]
    dx[0]=c[0]
    for k in range (n):
        x[i][i]=1/x[i][i]
        for j in range(n):
            if j>1:
                a[i][j]=a[i][j]*a[i][i]
        for l in range(n):
            for k in range(n):
                if i!=k:
                    if l>i:
                        a[k][l]=a[k][l]-a[k][i]*a[i][l]
     
        return x




a=[[2, 1, 4],
[8, -3, 2],
[4, 11, -1]]

a=np.array(a)

b=[5, 4, -3]

n=len(b)


q=np.linalg.inv(a)
r=(q.dot(a)).round(8)

print(q)
print(r)


y=q.transpose().dot(b)

x=[0]*n
for i in range(n-1, -1, -1):
    s=0
    for k in range(n-1, i, -1):
        s = s+ r[i][k]*x[k]
    x[i] = (y[i] - s)/r[i][i]

 
x=np.linalg.solve(r, y)
print("x:", x)

print(np.linalg.solve(a, b))

