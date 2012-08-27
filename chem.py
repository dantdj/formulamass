import csv
import re


#Read in data and store it in dictionary
elemen_data = { element.lower():weight for element,weight in csv.reader(open("chem.csv", "rb"))}
formul_data = { element.lower():weight for element,weight in csv.reader(open("form.csv", "rb"))}

while True:
	choice = int(raw_input("Element name or Formula? (1/2): "))

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
		
		#Divide formula by capitals, append numbers to previous element, lookup weight
		def molecularWeight(formula):
			matches = re.findall(r"([A-Z][a-z]?)([0-9]*)", formula)
			return sum(float(formul_data.get(symbol.lower(), 0)) * (int(count) if count else 1)
						for (symbol, count) in matches)
		
		#Print results of function
		print "Total weight =", float(molecularWeight(formula))
		
		
		
	if choice == 0:
		break
