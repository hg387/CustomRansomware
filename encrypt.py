def encrypt_line(line, key):


array1 = []

    for i in line:
	
		if i.isupper():
		
			line + key % 26
			
		if i.islower():
		
			line + key % 26
		
		if i.ispunct():
		
			line + key % 19 #need to check values for key encryption
			
		if i.isdigit():
		
			line + key % 10
		
	
	return line #need to put this into an array
	
	encrypt_line()