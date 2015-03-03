numbers=[1,2,3,4,5,6,7,8,9]
even_only=[]
odd_only=[]
for x in numbers:
	if x%2 !=1:
		even_only.append(x)
	else:
		odd_only.append(x)
		

print even_only
print odd_only

print sum(even_only)

print sum(odd_only)

print even_only[3]

print odd_only[4]