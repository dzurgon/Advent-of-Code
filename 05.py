def part1(data):
	data = data.split()
	maxRow = 0
	for i in data:
		row = [0, 128]
		col = [0, 8]
		for q in i[:7]:
			if q == "B":
				row[0] = (row[1]+ row[0]) // 2
			else:
				row[1] = (row[1] + row[0]) // 2
		for q in i[7:]:
			if q == "R":
				col[0] = (col[0] + col[1]) // 2
			else:
				col[1] = (col[0] + col[1]) // 2
		if row[0] * 8 + col[1] > maxRow:
			maxRow = row[0] * 8 + col[0]
	return maxRow

def part2(data):
	data = data.split()
	seats = []
	for i in data:
		row = [0, 128]
		col = [0, 8]
		for q in i[:7]:
			if q == "B":
				row[0] = (row[1]+ row[0]) // 2
			else:
				row[1] = (row[1] + row[0]) // 2
		for q in i[7:]:
			if q == "R":
				col[0] = (col[0] + col[1]) // 2
			else:
				col[1] = (col[0] + col[1]) // 2
		seats.append(row[0] * 8 + col[0])
	for i in range(len(data)):
		if i not in seats and i + 1 in seats and i - 1 in seats:
			return(i)
		


