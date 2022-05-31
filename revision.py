# a=int(input("enter the number :"))
# b=int(input("enter the number :"))
# if a>b:
#     print(a," is max no")
# else:
#     print(b," is max no")





# a=int(input("enter the number :"))
# b=int(input("enter the number :"))
# c=int(input("enter the number :"))
# if a>b and a>c : 
#     print(a,"is max num")
# elif b>a and b>c:
#     print(b," is max num")
# else:
#     print(c,"is max num")




# a=int(input("enter the number :"))
# if a%4==0:
#     print(a,"it is leap year")


# a=input("enter the word :")
# if a>="a" and a<="z"  :
#     print(a,"lower case")     
# else:
#     print(a,"upper case")

# a=int(input("enter the number 1:"))
# b=int(input("enter the number 2:"))
# c=int(input("enter the number 3:"))
# if a>b and a>c:
#     print(a,"max  num")
# elif b>a and b>c:
#     print(b,"max  num")
# else:
#     print(c,"max  num")

# num=int(input("enter the number:"))
# if num>0:
#     print("positive number")
# elif num<0:
#     print("negative number")
# else:
#     print("zero")

# num=(int(input("enter the number:")))
# if num%5==0 and num%11==0:
#     print("divisible")
# else:
#     print("not divisible")


# a=[23,34,96,89]
# i=0
# sum=0
# sum1=0
# while i<len(a):
#     if a[i]%2==0:
#         print(a[i],"even num")
#         sum=sum+a[i]
#     if a[i]%2!=0:
#         print(a[i],"odd num")
#         sum1=sum1+a[i]
#     i=i+1
# print(sum+sum1)

# a=[1,2,3,4]
# i=0
# b=0
# c=[]
# while i<len(a):
#     d=a[i]+b
#     b=d
#     c.append(d)
#     i=i+1
# print(c)
# a=[1,2,2,3,4,5]
# b=[2,4,8,9,10,12]
# i=0
# c=[]
# while i<len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i=i+1
# print(c)


# a=[1,7,2,3,4,5]
# i=0
# b=0
# c=[]
# while i<len(a):
#     if a[i]>  b:
#         b=a[i]
#         print(b)
#     i=i+1
# # print(b)

# a=[110,123000,4500,5060,2300]
# i=0
# while i<len(a):
#     if a[i]==0:
#         print()
#     else:
#         print(a[i])
#     i=i+1


# i=1
# while i<=100:
#     print(i,"=",i*i+i)
#     i=i+1


# a=[1,2,3,[1,4,6],[7],[9],3]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             j=j+1
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)
# c=0
# d=[]
# while i<len(b):
#     if b[i]>c:
#         c=b[i]
#         d.append(c)
#     i=i+1
# print(d)

# a=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=1
# b=0
# while i<len(a):
#     if a[i]>b:
#         b=a[i]
#     i=i+1
# print(b) 


# i=5
# while i>=1:
#     j=0
#     while j<=5-i:
#         print(" ",end=" ")
#         j=j+1
#     b=1
#     while b<=i:
#         print("*",end=" ")
#         b=b+1
#     print()


#     i=i-1


# i=1
# while i<=10:
#     j=0
#     while j<100:
#         print(j+i,end=" ")
#         j=j+10
#     print()
#     i=i+1

# a=[1,2,3,4,5,6,7]
# i=0
# b=0
# while i<len(a):
#     if i[i]==b:
#       b=a[i]
#       print(a[i],b)
#     i=i+2




# a="take me to the moon"
# i=0
# b=[]
# while i<len(a):
#     b.append(a[i])
#     i=i+1
# print(b)
# s=1
# count=0
# while s<len(b):
#     print(b[-s]==4)
#     count=count+1
#     s=s+1
#     break
# print(count)





# print("1")
# i=1
# # x=1
# while i<=4:
#     j=1
#     while j<=i:
#         print("1","0",end=" ")
#         j=j+1
#     # print(x)
#     print()
    # i=i+1