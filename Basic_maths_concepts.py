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


    



        



    
  
