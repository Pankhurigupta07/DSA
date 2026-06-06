arr_size=int(input())
arr=list(map(int,input().split()[:arr_size]))

# pre calculation
hash_size=int(input())


hash_arr=[0]* hash_size

for i in range (arr_size):
    number=arr[i]
    hash_arr[number]+=1

# fetching
q=int(input())

while(q>0):
    number=int(input())
    print(hash_arr[number])

    q-=1