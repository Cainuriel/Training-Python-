
# queremos ordenar esta lista ascendentemente
# pero solo UNA VEZ. 
l = [9,8,7,6,5,4,3,2,1]

def bubblesort_once(l):
	move = 0
	size = len(l)
	order = []
	for i in l:
		order.append(i)
		print(i)
	for i in range(size-1):

		if order[i] > order[i+1]:

			order[i], order[i+1] = order[i+1], order[i]

		else:
			pass

	return order


print(bubblesort_once(l))

