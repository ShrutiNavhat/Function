# def a():
#   b=int(input("enter the number :"))
#   i=1
#   while i<=10:
#     print(b,"=",b*i)
#     i=i+1
# a()


def a():
    i=1
    c=[]
    d=[]
    e=[]
    while i<=30:
        if i<=5:
           c.append(i*i)
        if i>=25:
            d.append(i*i)
        i=i+1
    e.append(c)
    e.append(d)
    print(e)
a()


# a=[1,2,3,4,5]
# i=0
# count=0
# b=[]
# while i<len(a):
#     b.append(a[i])
#     if count==2:
#         b.append(6)
#     count+=1
#     i+=1
# print(b)

# a="shrutinavhat"
# i=0
# d=1
# b=int(input("enter the number :"))
# c=[]
# while i<len(a):
#     c.append(a[i])
#     c.append(d*b)
#     i=i+1
#     d=d+1
# print(c)



# def a(b,c,opreter):
#     if opreter=="+":
#         print(b+c)
#     elif opreter=="-":
#         print(b-c)
#     elif opreter=="*":
#         print(b*c)
#     elif opreter=="/":
#         print(b/c)
#     elif opreter=="//":
#         print(b//c)
#     elif opreter=="%":
#         print(b%c)
#     else:
        
#         print("no")
# a(4,6,"*")


# def a(name,age):
#     print(name,age)
# a("shruti",17)

# def fun1(*a):
#     for i in a:
#         print(i)
# fun1(20,40,60)
# fun1(80,100)

# def a(a,b):
#     return (a+b ,a-b)
# add,sub=a(3,5)
# print(add,sub)




# def a(a,b):
#     return(a*b,a/b)
# mul,div=a(4,2)
# print(mul,div)

# def a(name,salary=9000):
#     print("name",name,"salary",salary)
# a("shruti",500)
# a("dhanu")


# def a(a,b):
#     squar=a**2
#     def add(a,b):
#         return(a+b)
#     add=add(a,b)
#     return(a+5)
# b=a(3,20)
# print(b)