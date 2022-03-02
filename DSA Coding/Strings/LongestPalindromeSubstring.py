
def printSubStr(str, low, high):
	
	for i in range(low, high + 1):
		print(str[i], end = "")

def longestPalSubstr(str):

	n = len(str)

	maxLength = 1
	start = 0
	for i in range(n):
		for j in range(i, n):
			flag = 1
			
			for k in range(0, ((j - i) // 2) + 1):
				if (str[i + k] != str[j - k]):
					flag = 0

			if (flag != 0 and (j - i + 1) > maxLength):
				start = i
				maxLength = j - i + 1
				
	
	printSubStr(str, start, start + maxLength - 1)

if __name__ == '__main__':
	str = input()	
	longestPalSubstr(str)







