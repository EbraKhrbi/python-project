a=int (input("enter number:"))
group=[1,5,8,3,3]
if a in group:
 print(True)
else:
 print(False)
# 6
a=[1,2,3,3,3,3,4,5]
print(set(a))
# 7
a=input("enter:")
x=""
z=len(a)
for i in a:
 x+=a[z-1]
 z=z-1
d=x
print(d)
if d==a:
 print(True)
else:
 print(False)
# 8
num= int (input("enter number"))
md=1
for i in range(1,num+1):
 md=md*i
 print(md)
# 9
class rectangle:
 def __init__(self,length,width):
 self.length=length
 self.width=width
 def area_rectangle (self,length,width):
 area=length*width
 return area
 def mference_rectangle (self,length,width):
 mference1=2*(length+width)
 return mference1
x=int (input("enter length"))
y=int (input("enter width"))
rectangle1=rectangle(x,y)