# insertion sort 

# def selection_sort(arr):
#     n=len(arr)
#     for i in range(n-1):
#         mini=i
#         for j in range(i,n):
#             if arr[j]<arr[mini]:
#                 arr[mini],arr[j]=arr[j],arr[mini]
#     return arr

# arr=[int(x) for x in input().split()]
# print(selection_sort(arr))

# best, worst,average time complexity of selection sort is O(n^2)

# bubble sort

def bubble_sort(arr):
    n=len(arr)
    
    for i in range(n-1,0,-1):
       
        didswap=0
        for j in range(i):
            if(arr[j]>arr[j+1]):
                arr[j+1],arr[j]=arr[j],arr[j+1]
                didswap=1
        
        if didswap==0: 
            break

    return arr  

arr=[int(x) for x in input().split()]
print(bubble_sort(arr))

# worst time complexity= O(n^2)
# best time complexity=O(n)