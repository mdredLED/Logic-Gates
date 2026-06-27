def mulgear(ifnot, geartype, *inputs):
	if (type(ifnot) != bool) or (type(geartype) != str) or not (all(type(item) in (bool,) for item in inputs)):
		print("У тебя в 'инвентировать?' [0] не булевское, в 'тип вентиля?' [1] не строка либо в вводах [+2] что то не булевское.")
		return None
	geartype=geartype.lower()
	if not geartype in ["buf", "or", "and", "xor"]:
		print(f"Вентили: buf, or, and, xor и их отрицательные аналоги. А теперь скажи где ты увидел свой '{geartype}'?")
		return None
	result = False
	if geartype == "buf":
		if sum(inputs) >= 1:
			result = True
	elif geartype == "and":
		if sum(inputs) == len(inputs):
			result = True
	elif geartype == "or":
		if sum(inputs) >= 1:
			result = True
	elif geartype == "xor":
		if sum(inputs) % 2 == 0 and sum(inputs) >= 1:
			result = True
	if ifnot == True:
		return not result
	return result
