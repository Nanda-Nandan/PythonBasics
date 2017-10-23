test="string"
def test1():
	if test=="number":
		print("test")
	elif test=="array":
		print("array")
	else:
		print("nothing")
	a, b=0, 1
	v = "exists" if a <b else "not exists"
	test2="this is no string"
	'''since there is no index by default for for loop in python we have to get it using enumerate function'''
	for i,item in enumerate(test2):
		print(i,item)
	else:
		print("else can be used with for or while loop,it will execute when loop will return false,either at complete of loop or without going into loop")
	'''Operators'''
	'''5/3=1.6666,5//3=1,5%3=2,divmod(5,3)=(1,2){which is a touple},num+=1{increment operator}'''
	x,y=5
	id(x)
	id(y)
	x==y
	'''true'''
	x is y
	'''false since everything in python is object x and y are also different object with different id,is operator checks for the id'''
	true and false
	false or true
	'''boolean operator'''
	true & false
	true | false
	'''bitwise boolean operator'''

	'''slice operator'''
	list=[1,2,3,4,5]
	list[2:4] 
	'''will give value 2,3,4,: operator slices the value'''
	list1[:]=range(100)
	'''o to 99'''
	list1[27:42:3]
	'''first argument starting index,second argument end index,3rd argument the gaps between two consecutive elements'''
	list1[27:42:3]=(50,50,50,50,50)
	'''we can assign using slice operator so that the value will be changed on real list'''


