def kadaneAlgorithm(n,arr):
    sum_num = 0
    max_sum = 0
    for i in range(n):
        sum_num += arr[i];   #maximum ending here
        if arr[i] > sum_num:
            sum_num = arr[i]
        if max_sum < sum_num:     #comparing maximum ending here , maximum so far
            max_sum = sum_num
    return max_sum
 
size = int(input())   
l = [int(x) for x in input().split()]
max_sm = kadaneAlgorithm(size,l)
print(max_sm)
