#!/bin/python3

#PrintString

print("string test")
print("""testt
est""")
print ('\n') #New line

print("Math time:")
print (50+50) #Add
print (50-50) #Subtract
print (50*50) #Multiply
print (50/50) #Divide
print (50+50-50*50/50) #PEMDAS
print (50**2) # Exponents
print (60%6) #modulo
print (50//6) #Number without residue

print ('\n') #New line

#Vars and methods
print("fun with methods and variables")
quote = "All is fair in love and war"
print (len (quote)) #Length
print (quote.upper()) #Uppercase
print (quote.lower()) #Lowercase
print (quote.title()) #Title

name = "Heath"
age = 29 # int int(29)
gpa = 3.7 #float float(3.7)

print (int(age))
print(int(29.9)) #does not round up, just removes whats after the point

print("My name is " + name + " and I am " + str(age) + " years old")

print ('\n') #New line
age +=1
print (age)

birthday = 1

age += birthday

print (age)
print ('\n') #New line
#Functions
print("Now some functions:")
def who_am_i():
	name = "heath"
	age = 29
	print("My name is " + name + " and I am " + str(age) + " years old")
who_am_i()

#Add in some parameters
def add_one_hundred(num):
	print(num+100)
add_one_hundred(100)

#Add in multiple parameters
def add (x,y):
	print(x+y)
add (7,7)
add (305,207)

#Using return

def multiply (x,y):
	return x*y

print(multiply(7,7))

def sqroot(x):
	return x** .5
print(sqroot(64))

print ('\n') #New line

#Bool expression

print ("Boolean expression:") 
bool1=True
bool2= 3*3 ==9
bool3 = False
bool4 = 3+3 !=9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5=("True")
print(type(bool5))

#Relational and boolean operations
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >=7 
less_than_equal_to = 7 <= 7
print (greater_than,less_than,greater_than_equal_to,less_than_equal_to)

test_and = (7>5) and (6 < 7)
test_or = (7<5) or (5 < 7)
test_not = not True

print (test_and,test_or,test_not)

print ('\n') #New line

#Conditional statements
print ("Conditional statements")

def soda (money):
	if money>=2:
		return "you got yourself a soda"
	else:
		return "no soda for you"
print(soda(1))
print(soda(3))
print ('\n') #New line
def alcohol(age,money):
	if (age >=21) and (money >=5):
		return ("we're gettin tipsy")
	elif (age >=21) and (money <=5):
		return ("come back with more money")
	elif (age <=21) and (money <=5):
		return ("Nice try kid")
	else:
		return ("You are too poor and too young")
print (alcohol(21,5))
print (alcohol(21,4))
print (alcohol(20,4))

print ('\n') #New line

#Lists

print ("Lists have brakets:")
movies = ["When Harry Met Sally", "The Hangover", "The perks of being a wallflower",
"THe Exoricst"]
print(movies[0])
print(movies[0:3])
print(movies[1:])
print(movies[:1])
print(movies[-1])
print(len(movies))
movies.append("JAWS")
print(movies)
movies.pop() #Remove last item on the list
print(movies)
movies.pop(1) #Remove 2nd item on the list
print(movies)

movies = ["When Harry Met Sally", "The Hangover", "The perks of being a wallflower",
"THe Exoricst"]
person = ["Heath", "Jake", "Leah","Jeff"]
combined = zip(movies,person) #combined the 2 lists
print(list(combined))

#Tuples
print("Tuples have parentheses and cannot change")
grades= ("A", "B", "C", "D", "F")
print(grades[1])

#Looping
print ("For loops - start to finish of iterate:")
vegetables = ["cucumber", "spinach" ,"cabbage"]
for x in vegetables:
	print(x)
print("While loops - Execute as long as True:")
i=1
while i<10:
	print(i)
	i+=1





