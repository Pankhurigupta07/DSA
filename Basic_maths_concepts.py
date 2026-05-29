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

    
  
