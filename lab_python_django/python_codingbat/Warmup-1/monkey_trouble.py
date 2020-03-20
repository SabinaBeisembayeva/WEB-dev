def monkey_trouble(a_smile, b_smile):
	if a_smile == b_smile:
		return True
	return False
	#Alternative
	#return a_smile == b_smile
print(
monkey_trouble(True, True),
monkey_trouble(False, False),
monkey_trouble(True, False)) #True True False
