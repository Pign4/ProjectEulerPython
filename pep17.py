# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

import time

def lettercount(n):
	count = 0
	string = str(n)
	if len(string) == 3:
		count += ntol[int(string[0])] + 7		#7 for "hundred"
		if string[-1] == string[-2] == "0":
			return count
		else:
			count += 3							#3 for "and"
	if string[-2] == "1":
		return count + ntol[10+int(string[-1])]
	else:
		if string[-1] != "0":
			count += ntol[int(string[-1])]
		return count + nntol[int(string[-2])]

if __name__ == '__main__':
    start_time = time.time()

    ntol = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]		#1 to 19
    nntol = [0,3,6,6,5,5,5,7,6,6]		#0, 10, 20 ... 90

    s = 11 + sum(ntol)								#11 for "one thousand"
    for number in range(20,1000):
    	s += lettercount(number)
    print(s)

    print("--- {} seconds ---".format(time.time() - start_time))
