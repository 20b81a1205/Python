num=int(input("enter a number:"))
temp=num
digits=0
while temp!=0 :
    digits+=1
    temp=temp//10
sum=0
t=num
while num>0 :
    r=num%10
    sum+= r**digits
    num=num//10
if t==sum :
    print("num is amstrong")
else :
    print("num is not amstrong")
