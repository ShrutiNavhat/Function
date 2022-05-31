# def a(b="1234abcd"):
#     i=1
#     c=""
#     while i<=len(b):
#         c=b[-i]
#         i=i+1
#         print(c,end="")
#     print()
# a()


def a(b=["abc","xyz","aba","1221"]):
    i=1
    while i<=len(b):
        j=0
        count=0
        while j<=1:
            if b[i][0]==b[i][-1]:
               count=count+1
            j=j+1   
        i=i+1
        print(count)
a()

# def a(b=(8,2,3,0,7)):
#     i=0
#     sum=0
#     while i<len(b):
#         sum=sum+b[i]
#         i=i+1
#     print(sum)
# a()


# def a(b=[1,2,3,3,3,3,4,5]):
#     i=0
#     c=[]
#     while i<len(b):
#         if b[i] not in c:
#             c.append(b[i])
#             return()
#         i=i+1
# print(a(c))

# def a(b):
#     return 5*b
# print(a(9))
# print(a(4))

