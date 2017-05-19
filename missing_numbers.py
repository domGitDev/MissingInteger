

def find_missing(A, m, B, n):
	""" This function find missing numbers in A using B
		param A: list
		param m: int
		param B: list
		param n: int
		return: sorted list
	"""
	
	def validate():
		if not A or not B:
			return False
		if m > n or m < 0 or n < 0:
			return False 
		if not isinstance(A, (list, tuple, set)):
			raise TypeError(
				'Expected list or tuple. A is %s and B is %s.' 
				% (type(A), type(B)))
		return True
	
	if not validate():
		return None
			
	A = sorted(A)
	B = sorted(B)
	missing = set()
	j = 0
		
	for val in B:
		if j > m:
			missing.add(val)
		elif val != A[j]:
			missing.add(val)
			# occurrency in A is greater than in B
			while prev == A[j]:
				j += 1
		else:
			j += 1
			 
	return sorted(mssing)

