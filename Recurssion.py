# print name n times
def print_name(name,i):
    if(i==5):
        return
    else:
        print(name,end=" ")
        i=i+1
        print_name(name,i)

n=input()
i=0
print_name(n,i)