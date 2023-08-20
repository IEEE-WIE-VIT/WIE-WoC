def countOddSum(ar, n):
	result = 0
	for i in range(n):
		val = 0
		for j in range(i, n-1): 
			val = val + ar[j]
			if (val % 2 != 0):
				result +=1

	return (result)

l = int(input())
ar = [int(x) for x in input().split()]
print(str(countOddSum(ar, l+1)))


