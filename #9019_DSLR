#9019
#ap0-2-7
import sys
input = sys.stdin.readline
from collections import deque ,defaultdict
def stf (start): #start to find
		#d
    d=str(int((start*2)% 10000))
    d='0'*(4-len(d)) +d 
		#s
    if start ==0:
        s='9999'
    else:
        s= str(start-1 )
        s='0'*(4-len(s)) +s
		#l,r
    str_start= '0'*(4-len(str(start))) +str(start) #아마 4자리수가 아니면 되도록 만들어줘야 할거임.
    l= (str_start[1]+str_start[2]+str_start[3]+str_start[0])
    r= (str_start[3]+str_start[0]+str_start[1]+str_start[2])
    return s,l,r,d

def fts (start): #find to start
		#d
    if (start%2)==1:
        rd='-1'
        rd2='-1'
    else :
        rd=str(int((start/2))) #만약에 홀수면 넘어가야함.
        rd='0'*(4-len(rd)) +rd
        rd2=str(int((start+10000)/2))  #문제점 start가 1000이면 이전값은 500이냐 5500이냐.
        rd2='0'*(4-len(rd2)) +rd2
		#s
    if start ==9999:
        rs='0000'
    else: 
        rs= str(start+1 )
        rs='0'*(4-len(rs)) +rs
		#l,r
    str_start='0'*(4-len(str(start))) +str(start) 
    rr= (str_start[1]+str_start[2]+str_start[3]+str_start[0])
    rl= (str_start[3]+str_start[0]+str_start[1]+str_start[2]) 
    return rs,rl,rr,rd,rd2

it=int(input().rstrip())
lis={0:'S',1:'L',2:'R',3:'D',4:'D'} #iterator순서에 맞춰 dict으로 저장 #for i에서 쓰려는 목적 
for i in range(it):
    k= list(map(int,input().rstrip().split()))
    start=k[0] 
    str_start='0'*(4-len(str(start))) +str(start)

    find=k[1]
    str_find='0'*(4-len(str(find))) +str(find)

    DD=defaultdict(list)
    DD2=defaultdict(list)
#[log,D]: DSLR연산으로 나온 값인경우,연산 전의 부모값을 가져오고 
#그 값이 어떤 연산으로 나온 값인지 저장
    DD[str_start]=["0",'0'] 
    DD2[str_find]=["0",'0']

#순회용 deque
    lis2=deque([start])
    lis3=deque([find])
    sig=True
    while sig :

        size=len(lis2)
        for _ in range (size) :
            start=int(lis2.popleft())
            str_start='0'*(4-len(str(start))) +str(start)#무조건 4자리 문자열로 만들어야함.
            S,L,R,D =stf (start)
            group=[S,L,R,D]
            for i in range(4):
                if len(DD[group[i]])!= 0 : #이미 값이 들어있는 노드인경우
                    continue
                DD[group[i]]=[str_start,lis[i]] #아니면 값 입력.
                if len(DD2[group[i]])!=0 : #만약 다른 DD에서 같은 노드 값이 들어있는 경우
                    kkk=i #그 때의 i값 가져오기
                    sig= False #종료조건
                    break
                lis2.append(group[i])
            if sig ==False : 
                break
         #중간에서 find까지의 연산, 중간에서 start까지의 연산저장.
        if sig ==False : 
            ans=''
            tt=group[kkk] #두 알고리즘이 중간에 만난 지점.
            while int(tt) != k[0]: #start 값을 찾을때까지 실행
                ans= DD[tt][1] + ans #연산값 추가하기
                tt = DD[tt][0] #부모 노드 가져오기
            tt=group[kkk] #초기화
            while int(tt) != k[1]: #find값을 찾을때까지 실행
                ans+= DD2[tt][1] 
                tt = DD2[tt][0] 
            print(ans.strip('0'))
            break 
        
        size=len(lis3) 
        for _ in range (size) :
            find=int(lis3.popleft())
            str_find='0'*(4-len(str(find))) +str(find)
            RS,RL,RR,RD,RD2 = fts (find)
						#find값이 홀수 인지 아닌지 판단. 홀수면 D연산을 안한거.
            if RD == '-1' :
                group2=[RS,RL,RR]
            else :
                group2=[RS,RL,RR,RD,RD2]

            for i in range(len(group2)):
                if len(DD2[group2[i]]) != 0 :
                    continue
                DD2[group2[i]]=[str_find,lis[i]]
                if len(DD[group2[i]])!=0 :
                    kkk=i
                    sig= False
                    break
                lis3.append(group2[i])
            if sig ==False : 
                break

        if sig ==False : 
            ans=''
            tt=group2[kkk]  
            while int(tt) != k[0]: 
                ans= DD[tt][1] + ans
                tt = DD[tt][0] 
            tt=group2[kkk]
            while int(tt) != k[1]:
                ans+= DD2[tt][1] 
                tt = DD2[tt][0] 
            print(ans.strip('0'))
            break