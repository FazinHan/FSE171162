#To increase readability, try using
#1. Proper Indentation
#2. Comments with the use of a function/variable

def freq(a):                                #the function that creates a frequecy distribution list. 
	bucket = []
	for i in range(26):
		check1 = a.count(chr(65+i))			#a count of all capital letters
		check2 = a.count(chr(97+i))			#all small letters
		if check1 != 0 or check2 != 0:
			b = check1 + check2				#finally, the case of inital string and number of special characters is lost here
		elif check1 == 0 and check2 == 0:
			b = 0
		bucket.append(b)
	return bucket							#Index 0 is counts of 'a', 25 is counts of 'z'
	
def distr(a):
	perc = []								#percentage occurence per letter
	for i in range(26):
		perc.append((a[i]/float(len(a)))*100)
	return perc	