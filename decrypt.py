def decrypt_line(line, key):

array1 = []

    for i in line:
	
		if i.isupper(): #for uppercase characters A-Z
		
			line - key % 26
			
		if i.islower(): #for lowercase characters a-z
		
			line - key % 26
		
		if i.ispunct(): #for punctuation !@#$%^&*()-_=+`~[]\{}|;':",./<>?
		
			line - key % 32 #need to check values for key encryption
			
		if i.isdigit(): #for digits 0-9
		
			line - key % 10
		
	
	return line #need to put this into an array
	
	decrypt_line()