def part1(data):
	data = data.split()
	for i in range(25, len(data)):
		correct = False
		curLis = [int(data[q]) for q in range(i-25, i)]
		for q in range(i-25, i):
			if int(data[i]) - int(data[q]) in curLis:
				correct = True
				break
		if correct == False:
			return int(data[i]) 


def part2(data):
	invalid = part1(data)
	data = [int(i) for i in data.split()]
	for i in range(len(data)):
		tot = 0
		possible = []
		for q in range(i, len(data)):
			possible.append(data[q])
			tot += data[q]
			if tot == invalid:
				return min(possible) + max(possible)
			if tot > invalid:
				break
