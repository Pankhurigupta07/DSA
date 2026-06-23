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

