def count_unique(input):
	dict = {}
	dict['a'] = 0
	dict['b'] = 0
	dict['c'] = 0
	dict['q'] = 0
	
	for i in input:
		if(i == 'a'):
			dict['a'] += 1
		elif (i == 'b'):
			dict['b'] += 1
		elif(i == 'c'):
			dict['c'] += 1
		elif(i == 'q'):
			dict['q'] += 1
	
	print sorted(dict.items(), key = lambda dict: dict[1], reverse=True)

def main():
	vec = ['a','b','a','b','b','c','c','q','q']
	count_unique(vec)


if __name__ == '__main__':
  main()