
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


# def pattern17(n):
#     letter=65
#     for i in range(n):
#         for j in range(n-i-1):
#             print(" ",end="")
#         for k in range(letter,letter+i+1,1):
#             print(chr(k),end="")
#         for p in range(letter+i-1,letter-1,-1):
#             print(chr(p),end="")
#         for l in  range(n-i-1):
#             print(" ",end="")

#         print()
# n=int(input())
# pattern17(n)   

# def pattern18(n):
#     letter=69
#     for i in range(n):
#         for j in range(letter-i,letter+1):
#             print(chr(j),end="")
#         print()
# n=int(input())
# pattern18(n)

#pattern19
# def pattern19_1(n):
#     for i in range(n):
#         # stars
#         for j in range(n-i):
#             print("*",end="")

#         # spaces
#         space=2*i
#         for k in range(space):
#             print(" ",end="")

#         # stars
#         for l in range(n-i):
#             print("*",end="")

#         print()

# def pattern19_2(n):
#     for i in range(n):
#         # stars
#         for j in range(i+1):
#             print("*",end="")

#         # spaces
#         spaces=2*(n-1)-2*i
#         for k in range (spaces):
#             print(" ",end="")

#         # stars
#         for l in range(i+1):
#             print("*",end="")

#         print()

# n=int(input())
# pattern19_1(n)
# pattern19_2(n)

#pattern 20
# def pattern20_1(n):
#     for i in range(n):
#         # stars
#         for j in range(i+1):
#             print("*",end="")

#         # spaces
#         spaces=2*(n-1)-2*i
#         for k in range (spaces):
#             print(" ",end="")

#         # stars
#         for l in range(i+1):
#             print("*",end="")

#         print()

# def pattern20_2(n):
#     for i in range(n-1):
#         # stars
#         for j in range(n-i-1):
#             print("*",end="")

#         # spaces
#         space=2*i+2
#         for k in range(space):
#             print(" ",end="")

#         # stars
#         for l in range(n-i-1):
#             print("*",end="")

#         print()

# n= int(input())
# pattern20_1(n)
# pattern20_2(n)




#pattern21

# def pattern21(n):
#     for i in range(n):
#         for j in range(n):
#             if(i==0 or i==n-1 or j==0 or j==n-1):
#                 print("*", end="")
#             else:
#                 print(" ",end="")
#         print()
            
# n=int(input())
# pattern21(n)



# def pattern22(n):
#     for i in range(n):
#         for j in range(n):
#             if(i==0 or i==n-1 or j==0 or j==n-1):
#                 print(n-3,end="")
#             elif(i==1 or i==n-2 or j==1 or j==n-2):
#                 print(n-4,end="")
#             elif(i==2 or i==n-3 or j==2 or j==n-3):
#                 print(n-5,end="")
#             else:
#                 print(n-6,end="")
#         print()
        
# n=int(input())
# pattern22(n)




# def pattern22(n):
#     for i in range(2*n-1):
#         for j in range(2*n-1):
#             top=i
#             left=j
#             right=(2*n-2)-j
#             bottom=(2*n-2)-i
#             print(n-min(min(top,bottom),min(left,right)),end="")
#         print()

# n=int(input())
# pattern22(n)
