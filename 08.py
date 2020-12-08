def part1(data):
	data = data.split("\n")
	tot = 0
	i = 0
	called = []
	
	while (i >= 0 and i < len(data)):
		if i in called:
			return tot
		else:
			called.append(i)
		if data[i][:3] == "nop":
			i += 1
		elif data[i][:3] == "acc":
			tot += int(data[i][4:])
			i += 1
		else:
			i += int(data[i][4:])

	return tot

def part2(data1):

	data = data1.split("\n")

	for q in range(len(data)):
		data = data1.split("\n")
		tot = 0
		i = 0
		called = []
		
		if "nop" in data[q]:

			data[q] = data[q].replace("nop", "jmp")

		
		elif "jmp" in data[q]:

			data[q] = data[q].replace("jmp", "nop")


		while (i >= 0 and i < len(data)):
			if i in called:
				break
			else:
				called.append(i)
			if data[i][:3] == "nop":
				i += 1
			elif data[i][:3] == "acc":
				tot += int(data[i][4:])
				i += 1
			else:
				i += int(data[i][4:])
		if i >= len(data):
			return tot
			
	return "broke"


	
	
		
def part2test(data, i):
	pass