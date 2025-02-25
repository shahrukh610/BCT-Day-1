a=int(input("Enter a number: "))
sum=0
temp=a
l=len(str(a))
print(l)
while temp>0:
    result=temp%10
    sum=sum+(result*(10**(l-1)))
    temp=temp//10
    l-=1
if(a==sum):
        print(a,"Palindrome number")
else:
        print(a,"Not a Palindrome number")
