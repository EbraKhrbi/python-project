print("الطالب / حافظ ضيف الله صالح الشب ")
print(" السؤال الاول")
y=[53,32,19,79,25,5,47]
print(" the minimum ",min(y))
print(" the maximum ", max(y))
max=y[0]
min=y[0]
for j in y:
	if j>max:
		max=j
	if j<min:
		min=j
print (" max =  ",max, " min =  ",min)
print("السؤال الثاني")
x=30
y=25
if x%5==0:
	print(True)
else:
	print(False)
if y%2==0:
	print(True)
else:
	print(False)
print("السؤال الثالث")
qoute=[17,'hafed',8.20,]
print(type(qoute))
print("السؤال الرابع")
numbers = [386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,512,24,892,894,767,553,81,379,843,831,445,742,717,958,743,527]
for x in numbers:
	if x%2==0:
	 print(x)
	if x==237:
		break
print("السؤال الخامس")
array=[1,5,8,3,3]
if 7 in array:
	print(True)
else:
	print(False)
print("السؤال السادس")
list_1=[1,2,3,3,3,3,4,5]
list_2 = list_1
print(set(list_2))
print("السؤال السابع")
word="level"
print(word[0:])
print(word[-5:])
if word == "level":
    print('Palindrome')
else:
	print(' Not palindrome')
print("السؤال الثامن")
num =int(input(" Enter the number : "))
import math
print("the factorial number is = ",math.factorial(num))
print("السؤال التاسع")
class length_width:
	length=0
	width=0
	area_rectangle=0
	def shwo_length_and_width (self):
		print(f" the length is {self.length}, the width is {self.width}, the Area rectangle is {self.area_rectangle}")
st1=length_width ()
st1.length =7
st1.width=9
st1.area_rectangle=7*9
st1.shwo_length_and_width()
print("السؤال العاشر")
class circle:
	radius=0
	area_circle=0
	circum=0
	def shwo_Area_and_radius_circle (self):
		print(f" the Radius circle is {self.radius}, the Area circle is {self.area_circle}, the circumference circle is {self.circum}")
st1=circle ()
st1.radius =8
st1.area_circle=3.14*8*8
st1.circum=2*3.14*8
st1.shwo_Area_and_radius_circle()