a=int(input("Enter a number: "))
sum=0
temp=a
while(a>=1):
   result=a%10
   sum+=result**3
   a=int(a/10)
if(sum == temp):
       print("It is a armstrong number")
else:
       print("It is not a armstrong number")
