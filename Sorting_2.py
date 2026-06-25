# merge sort
# def merge(arr,low,mid,high):
#     left=low
#     right=mid+1
#     temp=[]
#     while(left<=mid and right<=high):
#         if(arr[left]<=arr[right]):
#             temp.append(arr[left])
#             left+=1
#         else:
#             temp.append(arr[right])
#             right+=1

#     while(left<=mid):
#         temp.append(arr[left])
#         left+=1

#     while(right<=high):
#         temp.append(arr[right])
#         right+=1
    
#     for i in range(len(temp)):
#         arr[low+i]=temp[i]

# def merge_sort(arr,low,high):
#     if (low>=high):
#         return
#     mid=(low+high)//2
#     merge_sort(arr,low,mid)
#     merge_sort(arr,mid+1,high)
#     merge(arr,low,mid,high)
#     return arr

# arr=[int(x) for x in input().split()]
# n=len(arr)
# print("Sorted Array:", merge_sort(arr,0,n-1))

#best average and worst tc=O(nlogn)
#space complexity=O(n)


# recursive bubble sort
# def bubble_sort_rec(arr, n):
    
#     if n == 1:
#         return

#     swapped = False
    
#     for i in range(n - 1):
#         if arr[i] > arr[i + 1]:
#             arr[i], arr[i + 1] = arr[i + 1], arr[i]
#             swapped = True  
    
#     if not swapped:
#         return

#     bubble_sort_rec(arr, n - 1)

# arr = [int(x) for x in input().split()]
# bubble_sort_rec(arr, len(arr))
# print("Sorted Array:", arr)  
#s