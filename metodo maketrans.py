string = "This website is for losers LOL!"
vocals = "AaEeIiOoUu"
def disemvowel(string):

	vocals = "AaEeIiOoUu"
	result =""
	
	for i in string:
		count = 0
		for j in vocals:
			if i != j:
				count = count + 1
		else:
			pass
		if count == 10:
			result += i

	return result

# asi de facil es con el metodo translate
maketrans = string.maketrans(vocals,"          ")
print(maketrans)
result =  string.translate(maketrans)
print(result)

