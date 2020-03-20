def front3(str):
	if len(str) < 3:
		return str * 3
	return str[:3] * 3
	'''front_end = 3
    if len(str) < front_end:
        front_end = len(str)
    front = str[:front_end]
    return front * 3 # front + front + front'''


print(
front3('Java'),
front3('chocolate'),
front3('abc')
)
