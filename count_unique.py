def count_unique(input):
	dict = {} #create a dictionary to hold values and keys
	
	for i in input:		#iterate through the input list
		if i in dict:		#test if each element of the list is a key in the dictionary
			dict[i] += 1	#if so, increase the value of that key by one
		else:						# otherwise...
			dict[i] = 1		# make a new dictionary key with a value of 1
	
#print the tuples (items) in the dictionary, using the second value (dict[1]) of
#each tuple for sorting (representing the count), and sorting from highest to
#lowest (reverse = True)

	print sorted(dict.items(), key = lambda dict: dict[1], reverse=True)

#define a main function which will call the count_unique function above and 
#apply it to a vector of strings
def main():
	vec = ['a','b','a','b','b','c','c','q','q']
	count_unique(vec)
	vec2 = ['hat', 'hat','shoe','shoe','shoe', 'cane','smile']
	count_unique(vec2)
	vec3 = ['hello','how','are','you','doing','today', 'today', 'I','am','doing','well','how','are','you','doing']
	count_unique(vec3)

# boilerplate to run the main function with no command-line inputs
if __name__ == '__main__':
  main()