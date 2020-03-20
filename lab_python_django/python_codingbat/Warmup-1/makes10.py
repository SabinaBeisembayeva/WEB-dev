def makes10(a, b):
	#return (a == 10 or b == 10) or (a + b == 10)
	if a == 10 or b == 10 or a + b == 10:
		return True
	return False


print(
makes10(9, 10),
makes10(9, 9),
makes10(1, 9))
