#16928
#ap0-2-8
import sys
input = sys.stdin.readline
from collections import deque 
lis=[0]*100
lis2=deque([1])
cnt=0
find=True

#보드판 만들기
for i in range(100):
    lis[i]=i+1
k= list(map(int,input().rstrip().split()))
for i in range(k[0]+k[1]):
    ins= list(map(int,input().rstrip().split()))
    lis[ins[0]-1]=ins[1]

while find:
    size=len(lis2)
    for _ in range(size) :
        start=lis2.popleft()
        max=0
        for j in range(1,7):
            load=start+j
            if load == 100 :
                find=False
                break
                
            if load== lis[load-1] :
                max=load
            else :
                lis2.append(lis[load-1])
        if max != 0 :
            lis2.append(lis[max-1])
        if find == False :
            break 
    cnt+=1  
print(cnt)