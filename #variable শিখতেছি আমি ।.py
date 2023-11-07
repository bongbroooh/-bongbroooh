#variable শিখতেছি আমি ।
#১ ঘন্টা করে শিখব আর তামিম শাহারিয়ার শুবিন স্যারের বইটা শেষ করব
#sum of two numbers using variable named num1 and num2
import turtle as rn
num1 = 3
num2 = 6
result = num1 + num2
print(result)

# variable type such as integer , string and float
# int + int = int , int + float = float but int + str = error and float + srt = error


#now  allpying this valriable types
# integer / int
n1 = 4
n2 = 5
s = n1+n2
print(s)


#for string datatype , have to use (" ") or ('') for declaring its a str datatype to the computer otherwise it will not work
#string / str
name1 = "Bangladesh"
name2 = "India"
print(name1 , name2)
print(name2)

#float datatype is used for decimale . তার মানে ফ্লোট ডেটাটাইপ দশমিক এর জন্য ব্যবহৃত হয় ।
#float
float1 = 3.89
float2 = 4.5
resf = float1 + num2 #num2 is from the integer datatype decleared firstly
print(resf)
print(float2)


#day 2: Conditional Logic
#Using comperison operators
dn = 3
fb = 4
print(dn<fb)

Num1 = input("Input Num1 : ")
Num2 = input("Input num2 : ")
print(Num1>Num2)

#if is done i mean conditional stepments are done 
#lets creat a turtle file



rn.bgcolor("#ff00ff") #this is for back-ground color
rn.shape("triangle") #this is for the corsur shape
rn.speed()

#line 8-15 is for the 250x100 rectangle
rn.forward(250)
rn.left(90)
rn.forward(100)
rn.left(90)
rn.forward(250)
rn.left(90)
rn.forward(100)
rn.left(90)

rn.circle(50) #for the circle

#line 19-26 is for the handle of the gun 
rn.left(180+70)
rn.forward(150)
rn.right(90)
rn.forward(100)
rn.right(90)
rn.forward(200)
rn.left(180+110)
rn.forward(100)

rn.exitonclick() #this is for the click to exit the code 