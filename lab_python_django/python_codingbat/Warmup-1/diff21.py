def diff21(n):
	if n > 21:
		return 2 * abs(n-21)
	return abs(n-21)

print(diff21(19),
diff21(10),
diff21(21))
