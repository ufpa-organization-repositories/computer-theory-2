def insertionSort(arr):

	for index in range(1, len(arr)):

		chave = arr[index]
		j = index-1
		while j >=0 and chave < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
		array[j+1] = chave

array = [10, 8, 20, 9, 15]
insertionSort(array)
for i in range(len(array)):
	print ("%d" %array[i])
