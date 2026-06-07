# number hashing

# arr_size=int(input())
# arr=list(map(int,input().split()[:arr_size]))

# # pre calculation
# hash_size=int(input())


# hash_arr=[0]* hash_size

# for i in range (arr_size):
#     number=arr[i]
#     hash_arr[number]+=1

# # fetching
# q=int(input())

# result=[]
# while(q>0):
#     number=int(input())
    
#     result.append(f"{number} : {hash_arr[number]}")
#     q-=1

# print(result)

# character hashing 

# arr_size=int(input())
# arr=input().split()[:arr_size]

# # pre calculation

# hash=[0]*26

# for i in range (arr_size):
#     char=arr[i]
#     hash[ord(char) - ord('a')]+=1

# # fetching
# q=int(input())

# result=[]
# while(q>0):
#     character=input()
    
#     result.append(f"{character} : {hash[ord(character) - ord('a')]}")
#     q-=1

# print(result)


