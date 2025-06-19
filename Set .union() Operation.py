num_1 = int(input())
lis_1 = set(map(int,input().split()))
num_2 = int(input())
lis_2 = set(map(int,input().split()))

print(len(lis_1.union(lis_2)))
