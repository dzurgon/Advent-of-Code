

def part1(data):
	data = [int(i) for i in data.split()]
	for i in range(len(data)):
		if (2020 - data[i]) in data:
			return (2020 - data[i]) * data[i]
	
def part2(data):
	data = [int(i) for i in data.split()]
	for i in range(len(data)):
		for j in range(i+1, len(data)):
			for q in range(i+2, len(data)):
				if data[i] + data[j] + data[q] == 2020:
					return data[i]*data[j]*data[q]