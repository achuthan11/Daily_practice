#Day1 
#lowercase:
word=input()
print(word.lower()

#Detect Capital:
word=input()
if word.isupper():
    print("true")
elif word[1:].islower():
    print("true")
else:
    print("false")

#Number of segments:
sentence=input()
print(sentence.count(" ")+1)

#Day2 
#Domain name:
link=input()
print(link[link.find("www")+4:])

#String to url:
inp=input()
ans="https://"
ans+=inp
ans=ans.replace("#",".",2)
ans=ans.replace("#","/")
ans+='/'
print(ans)

#Maximum possible integer:
def sum_of_digits(n):
    n=str(n)
    sum=0
    for i in n:
        sum+=int(i)
    return sum
number=int(input())
sum_of=0
ans=0
for i in range(1,number+1):
    temp=sum_of_digits(i)
    if temp>sum_of:
        sum_of=temp
        ans=i
print(ans)

#Day 3
#Missing alphabets:
ls=[0]*26
sentence=input()
for i in sentence:
    ls[ord(i)-97]=1
for i in range(len(ls)):
    if ls[i]==0:
        print(chr(i+97),end="")

#Day 4
#Height checker:
height=input()
heightList=list(height)
heightList.sort()
ans=0
for i in range(len(height)):
    if height[i]!=heightList[i]:
        ans+=1
print(ans)

#Stack operations:
n=input()
ls=[]
for i in n[:-2]:
    if i.isdigit():
        ls.append(int(i))
#print(ls)
ans=[]
for i in range(1,ls[-1]+1):
    if i in ls:
        ans.append("Push")
    else:
        ans.append("Push")
        ans.append("Pop")
print("[",end="")
for i in range(len(ans)):
    if i==len(ans)-1:
        print("\"{}\"".format(ans[i]),end="]")
    else:
        print("\"{}\",".format(ans[i]),end="")

#Day 5 
#Ransom Note
from collections import Counter
a=Counter(input())
b=Counter(input())
if a&b==a:
    print("true")
else:
    print("false")

#Count the negative numbers:
ls=input().split("#")
ans=0
for i in range(len(ls)):
    for j in ls[i].split(" "):
        if int(j)<0:
            ans+=1        
print(ans)