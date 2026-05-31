# print name n times
# def print_name(name,i):
#     if(i==5):
#         return
#     else:
#         print(name,end=" ")
#         i=i+1
#         print_name(name,i)

# n=input()
# i=0
# print_name(n,i)              # time complexity and sc=O(n)



# print 1 to n
# def print_number(i,n):
#     if(i>n):
#         return
#     print(i)
#     i=i+1
#     print_number(i,n)

# n=int(input())
# print_number(1,n)


# print from n to 1
# def print_number(n,i):
#     if(n<i):
#         return
#     print(n)
#     n=n-1
#     print_number(n,i)

# n=int(input())
# print_number(n,1)


# print 1 to n using recursion with backtracking

# def print_number(i,n):
#     if (i<1):
#         return
    
#     print_number(i-1,n)
#     print(i)

# n=int(input())
# print_number(n,n)


# print n to 1 using recursion with backtracking

# def print_number(i,n):
#     if(i>n):
#         return
#     print_number(i+1,n)
#     print(i)

# n=int(input())
# print_number(1,n)

# sum of n numbers 

# def sum_n_numbers(i,n,sum):
#     if(i>n):
#         return

#     sum=sum+i
#     sum_n_numbers(i+1,n,sum)
#     if(i==n):
#         print(sum)
    
# n=int(input())
# sum=0
# sum_n_numbers(1,n,sum)

# another way, parameterize way
# def sum_n_num(i,sum):
#     if(i<1):
#         print(sum)
#         return
#     sum_n_num(i-1, sum+i)
# n=int(input())
# sum=0
# sum_n_num(n,sum)

# another way using functional method

# def sum_n_nums(n):
#     if(n==0):
#         return 0
    
#     return n+sum_n_nums(n-1)

# n=int(input())
# print(sum_n_nums(n))


# factorial 

# def fact(n):
#     if(n==0):
#         return 1
    
#     return n*fact(n-1)

# n=int(input())
# print(fact(n))

# reverse the array using 2 pointers
# def reverse_array(i,j,n):
#     if(i>=j):
#         return

#     temp=n[i]
#     n[i]=n[j]
#     n[j]=temp
#     reverse_array(i+1,j-1,n)
   

# n=list(map(int,input().split()))
# j=len(n)-1
# i=0

# reverse_array(i,j,n)
# print(n)

# reverse the array using one pointer

# def reverse_array(i,n,arr):
#     if(i>=n//2):
#         return
#     arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
#     reverse_array(i+1,n,arr)

# arr=list(map(int,(input().split())))
# i=0
# n=len(arr)
# reverse_array(i,n,arr)
# print(arr)



# string is palindrome

# def palindrome(i,n,string):
#     if(i>=n//2):
#         return True

#     if string[i]!=string[n-i-1]:
#         return False
#     return palindrome(i+1,n,string)
    
# string=input()
# i=0
# n=len(string)
# print(palindrome(i,n,string))


