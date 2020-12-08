def part1(data):
	data = data.replace(":", " ")
	data = data.replace("-", " ")
	data = data.split()
	
	validCount = 0
	for i in range(0, len(data), 4):
		cnt = data[i+3].count(data[i+2])
		if cnt >= int(data[i]) and cnt <= int(data[i+1]):
			validCount += 1
	return validCount

def part2(data):
	data = data.replace(":", " ")
	data = data.replace("-", " ")
	data = data.split()
	validCount = 0
	for i in range(0, len(data), 4):
		num1 = int(data[i])-1
		num2 = int(data[i+1])-1
		string = data[i+3]
		letter = data[i+2]
		if (string[num1] == letter or string[num2] == letter) and not (string[num1] == letter and string[num2] == letter):
			validCount += 1
	return validCount