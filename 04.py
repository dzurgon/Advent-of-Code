def part1(data):

	data = data.split("\n\n")
	correct = 0
	for i in data:
		if "hgt" in i and "byr" in i and "ecl" in i and "pid" in i and "hcl" in i and "eyr" in i and "iyr" in i:
			correct += 1
	
	return correct

def part2(data):

	# separates each entry into a list of entries
	data = data.split("\n\n")
	criteria = []

	# adds all the entries with the correct amount of fields into a new list (part1)
	for i in data:
		if "hgt" in i and "byr" in i and "ecl" in i and "pid" in i and "hcl" in i and "eyr" in i and "iyr" in i:
			criteria.append(i) # added to the new list 'criteria'

	# creates a 2d array with key : value pairs net to each other in the list
	criteria = [i.replace(":", " ").replace("\n", " ").split() for i in criteria]
	correct = 0
	for i in criteria:
			# indexes each field in the list, and sets a variable to the next item in the list for easy reference
			hgt = i[i.index("hgt") + 1]
			byr = i[i.index("byr") + 1]
			eyr = i[i.index("eyr") + 1]
			ecl = i[i.index("ecl") + 1]
			pid = i[i.index("pid") + 1]
			hcl = i[i.index("hcl") + 1]
			iyr = i[i.index("iyr") + 1]

			# all of the booleans for each field
			hgtBool = (hgt[-2:] == "cm" and int(hgt[:-2]) >= 150 and  int(hgt[:-2]) <= 193 or hgt[-2:] == "in" and int(hgt[:-2]) >= 59 and  int(hgt[:-2]) <= 76)
			byrBool = (int(byr) >= 1920 and int(byr) <= 2002)
			eyrBool = (int(eyr) >= 2020 and int(eyr) <= 2030)
			iyrBool = (int(iyr) >= 2010 and int(iyr) <= 2020)
			eclBool = (len(ecl) == 3 and "ambblubrngrygrnhzloth".find(ecl) % 3 == 0)
			pidBool = (pid.isdigit() and len(pid) == 9)
			hclBool = (hcl.find("#") == 0 and len(hcl) == 7)
			if hclBool:
				for i in hcl[1:]:
					if i not in "abcdef0123456789":
						hclBool = False
						break
	
			# if all boolean variables are true, add 1 to the correct amount of entries
			if (hgtBool and byrBool and eyrBool and iyrBool and eclBool and pidBool and hclBool):
				correct += 1
	#return the correct amount of entries
	return correct
