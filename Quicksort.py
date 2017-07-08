def partition(sample,start,end):
	pivot=sample[end]
	index=start
	current=start
	while(current<end):
		if(sample[current]<=pivot):
			sample[index],sample[current]=sample[current],sample[index]
			index+=1
		current+=1
	sample[index],sample[end]=sample[end],sample[index]
	return index

def quicksort(sample, start, end):
	if(start<end):
		index=partition(sample,start,end)
		quicksort(sample,start,index-1)
		quicksort(sample,index+1,end)

length=input("Enter number of elements")
sample=[]
i=0
while(i<length):
	numb=input("Enter number")
	sample.append(numb)
	i=i+1
quicksort(sample,0,length-1)
print sample
