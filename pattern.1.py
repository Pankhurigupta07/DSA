
# def pattern1(n):
#     for i in range(n):
#         for j in range(n):
#             print("*", end="")

#         print("\n")

# n=int(input())
# pattern1(n)
    


# def pattern2(n):
#     for i in range(n+1):
#         for j in range(i):
#             print("*", end=" ")

#         print()

# n=int(input())
# pattern2(n)
    

# def pattern3(n):
#     for i in range(n+1):
#         for j in range(i):
#             print(j+1,end="")

#         print()

# n=int(input())
# pattern3(n)
   


# def pattern4(n):
#     for i in range(n+1):
#         for j in range(i):
#             print(i,end="")

#         print()

# n=int(input())
# pattern4(n)
   

# def pattern5(n):
#     for i in range(n):
#         for j in range(n-i):
#             print("*",end="")

#         print()

# n=int(input())
# pattern5(n)
  


# def pattern6(n):
#     for i in range(n):
#         for j in range(n-i):
#             print(j+1,end="")

#         print()

# n=int(input())
# pattern6(n)
  




# def pattern7(n):
#     for i in range(n):
#         for j in range(n-i-1):
#             print(" ",end="")
#         for k in range(2*i+1):
#             print("*", end="")
#         for l in range(n-i-1):
#             print(" ",end="")

#         print()
# n=int(input())
# pattern7(n)




# def pattern8(n):
#     for i in range(n):
#         for j in range(i):
#             print(" ",end="")
#         for k in range(2*n-2*i-1):
#             print("*", end="")
#         for l in range(i):
#             print(" ",end="")

#         print()

# n=int(input())
# pattern8(n)



# def pattern91(n):
#     for i in range(n):
#         for j in range(n-i-1):
#             print(" ",end="")
#         for k in range(2*i+1):
#             print("*", end="")
#         for l in range(n-i-1):
#             print(" ",end="")

#         print()



# def pattern92(n):
#     for i in range(n):
#         for j in range(i):
#             print(" ",end="")
#         for k in range(2*n-2*i-1):
#             print("*", end="")
#         for l in range(i):
#             print(" ",end="")

#         print()

# n=int(input())
# pattern91(n)
# pattern92(n)


# def pattern10(n):
#     for i in range(n):
#         for j in range(i+1):
#             print("*", end="")

#         print()
#     for k in range(n-1):
#         for l in range(n-k-1):
#             print("*", end="")

#         print()


# n= int(input())
# pattern10(n)


# def pattern11(n):
#     for i in range(n):
#         start=1
#         if(i%2==0):
#             start=1
#         else:
#             start=0
#         for j in range (i+1):
#             print(start,end="")
#             start=1-start
#         print()

# n=int(input())
# pattern11(n)




# def pattern12(n):
#     spaces=2*(n-1)
#     for i in range(n):
#         for j in range(i+1):
#             print(j+1, end="")

#         for k in range (spaces):
#             print(" ",end="")

        
#         for l in range(i+1, 0,-1):
#             print(l, end="")
#         print()
#         spaces=spaces-2

# n= int(input())
# pattern12(n)



# def pattern13(n):
#     num=1
#     for i in range (n):
#         for j in range(i+1):
#             print(num, end=" ")
#             num=num+1

#         print()
# n=int(input())
# pattern13(n)


# def pattern14(n):
#     letter=65
#     for i in range (n):
#         for j in range(letter,letter+i+1):
#             print(chr(j),end="")
            
#         print()
        
# n=int(input())
# pattern14(n)

# def pattern15(n):
#     letter=65
#     for i in range (n):
#         for j in range(letter,letter+n):
#             print(chr(j),end="")
            
#         print()
#         n=n-1
# n=int(input())
# pattern15(n)



# def pattern16(n):
#     letter=65
#     for i in range (n):
#         for j in range(i+1):
#             print(chr(letter),end="")
            
#         print()
#         letter=letter+1
# n=int(input())
# pattern16(n)



