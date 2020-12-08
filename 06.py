def part1(data):
	total = 0
	for i in data.split("\n\n"):
		for q in range(len(i)):
			if i.index(i[q]) == q and i[q].isalpha():
				total += 1
	return total

def part2(data):
	total = 0
	for i in data.split("\n\n"):
		dic = {}
		i = i.split()
		for q in i:
			for x in range(len(q)):
				if q.index(q[x]) == x and q[x].isalpha():
					if q[x] not in dic:
						dic[q[x]] = 1
					else:
						dic[q[x]] += 1
		for q in dic:
			if dic[q] == len(i):
				total += 1
	return total
