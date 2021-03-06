import csv
import re

#Divide formula by capitals, append numbers to previous element, lookup weight
def molecularWeight(formula):
        # Match either element + number or something in brackets + number
        # [^\)] means anything but a closing bracket.
        matches = re.findall(r"([A-Z][a-z]?|\([^\)]+\))([0-9]*)", formula)
        weight = 0.0
        for (symbol, count) in matches:
                if (symbol[0] == "("):
                        # This is a bracketed expression. get molecular weight of its gut
                        weight += molecularWeight(symbol[1:-1]) * (int(count) if count else 1)
                else:
                        # It's an element. Proceed as needed.
                        weight += float(formul_data.get(symbol.lower(), 0)) * (int(count) if count else 1)
        return weight
						
#Read in data and store it in dictionary
elemen_data = { element.lower():weight for element,weight in csv.reader(open("chem.csv", "rb"))}
formul_data = { element.lower():weight for element,weight in csv.reader(open("form.csv", "rb"))}

while True:
	try:
		choice = int(raw_input("Element name or Formula? (1/2): "))
	except ValueError:
		print "Make sure you enter either 1 or 2!"
		continue

	if choice == 1:
		elements = {}
		numberOfPrompts = int(raw_input("Enter total amount of elements: "))
		for i in range(numberOfPrompts):
			# will prompt "Enter Element 1: " on the first iteration
			userInput = raw_input("Enter Element %s: " % (i+1, )) 
			elements[userInput] = float(elemen_data.get(userInput.lower()))
		for element in elements.keys():
			weightSum = 0
			for weight in elements.values():
				weightSum += weight
			
		print "Total weight =" ,weightSum
			
	if choice == 2:
		formula = raw_input("Enter formula: ")

		#Print results of function
		print "Total weight =", float(molecularWeight(formula))
		
	if choice == 3:
		numberOfPrompts = int(raw_input("Enter total amount of formulae: "))
		for i in range(numberOfPrompts):
			# will prompt "Enter formula 1: " on the first iteration
			formula = raw_input("Enter formula %s: " % (i+1, )) 
							
		print "Total weight = ", float(molecularWeight(formula))
			
	if choice == 0:
		break
