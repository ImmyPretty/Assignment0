mixed_list = [256, 'kigali',250, 254, 'nairobi','kampala']

city_code=[]
cities=[]

for item in mixed_list:
	if type(item)==int:
		city_code.append(item)
	elif type(item)==str:
		cities.append(item)

print mixed_list
print city_code
print cities

list.sort(city_code)
print city_code

city_code.reverse ()
print city_code
cities.sort ()
print cities
cities.pop()
print cities