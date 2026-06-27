# optimal approch

# largest element in array

# n=int(input())
# arr=list(map(int,input().split()[:n]))
# largest=max(arr)
# print(largest)


#optimal solution. TC-> O(n) SC-> O(1)

# def largest_element(arr):
#     largest=arr[0]
#     n=len(arr)
#     for i in range(1,n):
#         if (arr[i]>largest):
#             largest=arr[i]

#     print(largest)


# arr = [int(x) for x in input().split()]

# largest_element(arr)


# brute force solution mein sorting karte hai
# TC-> O(NLogN)
#SC -> O(1)

# def largest_element(arr):
#     num=arr[0]
#     n=len(arr)
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i]>arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]
                
#     return arr[n-1]
#     # n=len(arr)
#     # arr.sort()
#     # largest=arr[n-1]
#     # return largest

# arr= [int(x) for x in input().split()]
# print(largest_element(arr))


# second largest element in array
#brute force 
# time complexity=O(n+nlogn)

# def second_largest_element(arr,n):
#     for i in range(n-1):
#         mini=i
#         for j in range(i,n):
#             if(arr[j]<arr[mini]):
#                 arr[mini],arr[j]=arr[j],arr[mini]
#     for k in range(n-2,-1,-1):
#         if(arr[k+1]!=arr[k]):
#             second_largest_element=arr[k]
#             break

#     return second_largest_element


# arr=[int(x) for x in input().split()]
# print(second_largest_element(arr,len(arr)))


# better approch
# O(2n) time complexity

# def second_largest_element(arr,n):
#     largest=arr[0]
#     for i in range(n):
#         if(arr[i]>largest):
#             largest=arr[i]

#     second_largest=-1
#     for j in range(n):
#         if(arr[j]>second_largest and arr[j]!=largest):
#             second_largest=arr[j]

#     return second_largest

# arr=[int(x) for x in input().split()]
# print(second_largest_element(arr,len(arr)))


# optimal solution
# tc-> O(n)

# def second_largest_element(arr,n):
#     # if n<2:
#     #     return-1
#     largest=arr[0]
#     second_largest=-1
#     for i in range(1,n):
#         if(arr[i]>largest):
#             second_largest=largest
#             largest=arr[i]

#         elif arr[i] >second_largest and arr[i]!=largest :
#             second_largest=arr[i]

#     return second_largest

# second smallest
# tc->O(n)
# def second_smallest_element(arr,n):
#     # if n<2:
#     #     return-1
#     smallest=arr[0]
#     second_smallest=float('inf')
#     for i in range(1,n):
#         if(arr[i]<smallest):
#             second_smallest=smallest
#             smallest=arr[i]

#         elif arr[i]<second_smallest and arr[i]!=smallest :
#             second_smallest=arr[i]

#     return second_smallest

# arr=[int(x) for x in input().split()]
# print("second largest:",second_largest_element(arr,len(arr)))
# print("second smallest:",second_smallest_element(arr,len(arr)))



