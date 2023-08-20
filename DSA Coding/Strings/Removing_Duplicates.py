class Solution:
	def removeDups(self, S):		
		st = ''
		for ch in S:
		    if ch not in st:
		        st += ch
		return st
		        
