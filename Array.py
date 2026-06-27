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
