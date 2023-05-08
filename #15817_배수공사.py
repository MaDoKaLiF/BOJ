#15817
#ap0-2-22
import sys 
input = sys.stdin.readline
def sub(lis2):
    for i in range(num):
        if i!=0:
            lis2=lis3.copy()

        if lis[i][0]*lis[i][1]+1 > w+1 :
            c1=w+1
        else :
            c1=lis[i][0]*lis[i][1]+1

        for j in range(lis[i][0],c1):
            lis3[j]+=lis3[j-lis[i][0]]
        for j in range(c1,w+1):
            for k in range(1,lis[i][1]+1): #개수
                if j>= lis[i][0]*k:
                    lis3[j]+= lis2[j-lis[i][0]*k]
                else :
                    break
    print(lis3[-1])

num,w =map(int, input().rstrip().split())
lis=[]
for _ in range(num) :
    nw , ct =list(map(int, input().rstrip().split()))
    lis.append([nw,ct])
lis3=[0]*(w+1)
lis2=[0]*(w+1)
lis3[0]=1
sub(lis2)