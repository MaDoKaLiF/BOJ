#10026
#ap0-2-6
import sys
input = sys.stdin.readline
from collections import deque

#색맹이 아닌사람 R,G를 다르게 취급함.  
def maze(k1,k2,log):
    lis2=deque([[k1,k2]])
    while lis2 :
        n=lis2.popleft()
        group = ([n[0]+1,n[1]],[n[0],n[1]+1],[n[0]-1,n[1]],[n[0],n[1]-1] )
        for i,j in group :
            if 0 <= i < it and 0 <= j < it:  
                if lis3[i*it+j] == False : #이미 지나간 노드인경우
                    continue
                elif lis[i][j] == log : #지나가지 않았고 같은 노드인경우
                    lis2.append([i,j]) #그 때만 deque에 추가
                    lis3[i*it+j] = False  
 #색맹인 사람. R,G를 같이 취급함.     
def maze2(k1,k2,log):
    lis2=deque([[k1,k2]])
    while lis2 :
        n=lis2.popleft()
        group = ([n[0]+1,n[1]],[n[0],n[1]+1],[n[0]-1,n[1]],[n[0],n[1]-1] )
        if log=='B': #위와 동일
            for i,j in group :
                if 0 <= i < it and 0 <= j < it:  
                    if lis3[i*it+j] == True : 
                        continue
                    elif lis[i][j] == log : 
                        lis2.append([i,j])
                        lis3[i*it+j] = True  
        elif log== "R" or log=='G' :
            for i,j in group :
                if 0 <= i < it and 0 <= j < it:  
                    if lis3[i*it+j] == True : #이미 지나간 경우
                        continue
                    elif lis[i][j] != 'B' :  #지나가지 않았고 같은 노드인경우
                        lis2.append([i,j])
                        lis3[i*it+j] = True 
                
#변수 정의
it=int(input().rstrip())
lis=[]  
lis3=[True]*(it**2)
depth=0
depth2=0
for i in range(it):
    k= list(map(str,list(input().rstrip()))) 
    lis.append(k) 

#색맹이 아닌경우
#lis3의 True를 모두 False로 뒤집음.
for i in range(len(lis3)):
    k1=i//it #행 값
    k2=i-k1*it #열 값
    log=lis[k1][k2] #해당 행렬의 값
    if lis3[i] == True : 
        depth+=1
        lis3[i] =False
        maze(k1,k2,log)
    
#색맹인 경우  
#lis3의 False를 모두 True로 뒤집음.  
for i in range(len(lis3)):
    k1=i//it
    k2=i-k1*it
    log=lis[k1][k2]
    if lis3[i] == False :
        depth2+=1
        lis3[i]= True
        maze2(k1,k2,log)
        
print(str(depth)+' '+str(depth2))