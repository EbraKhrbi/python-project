a=[53,32,19,79,25,5,47]

max = a[0]
min = a[0]
d = 0
for i in a:
    if i > max:
        max = i
    if i < min:
        min = i
print("max= ",max,"min = ,min")     

###############################################################

a=int(input("enter number 1"))
b=int(input("enter number 2"))
c=a/b
if a%b==0:
 print(True)
else: a%b==1
print(False) 
################################################################## 
a=[]
print(type(a))

##############################################################

numbers =[386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,
162,785,219,918,237,412,566,826,248,866,950,626,949,687,217,
815,67,104,58,512,24,892,894,767,553,81,379,843,831,445,742,717,958,743,527]
for i in numbers:
    if i%2==0:
        print(i)
        if i ==237:
            break
########################################################################

a=int(input("enter number :"))       
group=[1,5,8,3,3]
if a in group:
    print(True)
else:
    print(False)  
###############################################################

a=[1,2,3,3,3,3,4,5]
print(set(a))
###########################################################

a=input("enter")
x=""
z=len(a)
for i in a:
    x+=a[z-1]
    z=z-1 
    d=x
    print(True)
else:
    print(False)
##########################################################################

num=int(input("enter number"))
md=1
for i in range(1,num+1):
    md=md*i
    print(md)
##############################################################################

class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area_rectangle(self,lenth,width):
        area=lenth*width
        return  rectangle                

x=int (input("enter lenth"))
y=int (input(" enter width"))
rectangle=rectangle(x,y)

print(rectangle.area_rectangle(x,y))
#####################################################

p=3.1415
class circle:
    def __init__(self,p,radius):
        self.p=p
        self.radius=radius
    def circle__area(self,p,radius):
        area=p*radius*radius
        return area
    def circle__circle(self,p,radius): 
        mference=2*p*radius
        return mference
r=float(input("enter radius"))
circle=circle(p,r)
print(circle.circle_area(p,r)) 
print(circle.circle_mference(p,r))          

###############################################################