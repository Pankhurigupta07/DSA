
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
    

def pattern3(n):
    for i in range(n+1):
        for j in range(i):
            print(j+1,end="")

        print()

n=int(input())
pattern3(n)
   
