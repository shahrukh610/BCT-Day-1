ans=int(input("Enter a number: "))
a=0
for i  in range(1,ans+1):
    if(ans%i==0):
        a+=1
        i+=1
if(a==2):
    print(ans,"is a prime number ")
else:
    print(ans,"is not a prime number ")
