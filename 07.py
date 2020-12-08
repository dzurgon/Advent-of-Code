def part1(data):
	dic = {}
	viewed = []
	for i in data.split("\n"):
		i = i.split()
		dic[i[0] + " " + i[1]] = [i[q] + " " + i[q+1] if "no" not in i else "-1" for q in range(5, len(i), 4) ]
	def recurse():
		for i in dic:
			for q in dic[i]:
				if (q in viewed or "shiny gold" in dic[i]) and i not in viewed:
					viewed.append(i)
					recurse()
	recurse()
	return len(viewed)
	
def part2(data):
	dic = {}
	for i in data.split("\n"):
		i = i.split()
		dic[i[0] + " " + i[1]] = dict([(i[q] + " " + i[q+1], int(i[q-1])) if "no" not in i else ("null", None) for q in range(5, len(i), 4)])
	def recurse(key="shiny gold", total =1):
		for i in dic[key]:
			if "null" not in dic[key]:
				total += dic[key][i]* recurse(i)
		return total
	return recurse()-1