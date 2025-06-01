#Bubble_sort
def my_sort(a,reverse=0):
	for i in range(len(a)-1):
		for j in range(0,len(a)-i-1):
			if a[j]>a[j+1] and reverse==0:
				a[j],a[j+1]=a[j+1],a[j]
			if a[j]<a[j+1] and reverse==1:
				a[j],a[j+1]=a[j+1],a[j]
	print(a)

a=[6,4,2,4,5,89,0,3]
my_sort(a,reverse=0)
			
	
