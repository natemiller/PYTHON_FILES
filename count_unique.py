def count_unique(input):
	count_a = 0
	count_b = 0
	count_c = 0
	count_q = 0
	
	for i in input:
		if(i == 'a'):
			count_a += 1
		elif (i == 'b'):
			count_b += 1
		elif(i == 'c'):
			count_c += 1
		elif(i == 'q'):
			count_q += 1
	
	x = [count_a, count_b, count_c, count_q]
	
	print(x)

def main():
	vec =['a','b','a','b','b','c','c','q','q']
	count_unique(vec)


if __name__ == '__main__':
  main()