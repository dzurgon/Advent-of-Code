def part1(data):
	data = data.split()
	x = 0
	treeCount = 0
	for i in range(1, len(data)):
		x += 3
		if x > 30:
			x -= 31
		if data[i][x] == '#':
			treeCount += 1

	return treeCount
			
def part2(data):
	data = data.split()
	tup = ((1,1),(3,1),(5,1),(7,1),(1,2))
	mult = 1
	for i in range(len(tup)):
		treeCount = 0
		x = 0
		for q in range(1, len(data), tup[i][1]):
			x += tup[i][0]
			if x > 30:
				x -= 31

			if data[q][x] == '#':
				treeCount += 1
		mult *= treeCount
	return mult
