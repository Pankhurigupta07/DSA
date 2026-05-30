# count the digits 
# def count_digit(n):
#     count=0
#     while(n>0):
#         # lastdigit=n%10
#         count=count+1
#         n=n//10
#     return count
# n=int(input())
# print(count_digit(n))


#2nd type to solve the same question

# def count_digit(n):
#     count=int(log10(n)+1)
#     return count

# n=int(input())
# print(count_digit(n))

# reverse the numbers
# def reverse_input_numbers(n):
    
#     while(n>0):
#         lastdigit=n%10
#         print(lastdigit,end="")
#         n=n//10
    
# n=int(input())
# reverse_input_numbers(n)

#another way to solve same problem

# def reverse_input_numbers(n):
#     reverse=0
#     while(n>0):
#         lastdigit=n%10
#         n=n//10
#         reverse=(reverse*10)+lastdigit
#     return reverse

# n=int(input())
# print(reverse_input_numbers(n))



# def reverse_input_numbers(n):
#     reverse=0
#     while(n>0):
#         lastdigit=n%10
#         n=n//10
#         reverse=(reverse*10)+lastdigit
#     return reverse

# n=int(input())
# result=(reverse_input_numbers(n))
# if result==n:
#     print(True)
# else:
#     print(False)


# armstrong numbers

# def armstrong_number(n):
#     check_number=0
#     while(n>0):
#         lastdigit=n%10
#         new_lastdigit=(lastdigit)**3
#         check_number=check_number+new_lastdigit
#         n=n//10
#     return check_number

# n= int(input())
# result=armstrong_number(n)
# if(result==n):
#     print(True)
# else:
#     print(False)


# print all divisors

# def divisors(n):
#     for i in range(1,n+1):
#         if(n%i==0):
#             print(i,end=" ")
# n=int(input())
# divisors(n)                       # Time complexity=O(n)



# so here is the another way to solve same problem with minimum time complexity

# from math import sqrt
# def divisors(n):
#     l=[]
#     num=int(sqrt(n))
#     for i in range(1,num+1):
#         if(n%i==0):
#             l.append(i)
#             if((n//i)!=i):
#                 l.append(n//i)
#         l.sort()
#     return l
# n=int(input())
# print(divisors(n))        # Time complexity=O(sqrt(n))



# prime number
# from math import sqrt
# def prime_number(n):
#     l=[]
#     num=int(sqrt(n))
#     for i in range(1,num+1):
#         if(n%i==0):
#             l.append(i)
#             if((n//i)!=i):
#                 l.append(n//i)
#         l.sort()
#     return l
# n=int(input())
# result=prime_number(n)
# if(len(result)==2):
#     print("prime")
# else:
#     print("not prime")



# GCD/HCF
# from math import sqrt
# def HCF(n,m):
#     HCF=[]
#     list1=[]
#     list2=[]
#     new_n=int(sqrt(n))
#     new_m=int(sqrt(m))
#     for i in range(1,new_n+1):
#         if(n%i==0):
#             list1.append(i)
#             if((n//i)!=i):
#                 list1.append(n//i)
#     for j in range (1,new_m+1):
#         if(m%j==0):
#             list2.append(j)
#             if((m//j)!=j):
#                 list2.append(m//j)
    
#     for i in list1:
#         for j in list2:
#             if(i==j):
#                 HCF.append(i) 
#     return max(HCF)

# n=int(input())
# m=int(input())
# print(HCF(n,m))


# another way to solve same question       
# from math import sqrt
# def HCF(n,m):
#     minimum=min(n,m)
#     for i in range(minimum,0,-1):
#         if (n%i==0 and m%i==0):
#             print(i)
#             break

# n=int(input())
# m=int(input())
# HCF(n,m)


# by using equiledian alogrithm

# def HCF(a,b):
#     while(a>0 and b>0):
#         if(a>b):
#             a=a%b
#         else:
#             b=b%a
    
#     if(a==0):
#         return b
#     else:
#         return a
# a=int(input())
# b=int(input())
# print(HCF(a,b))
