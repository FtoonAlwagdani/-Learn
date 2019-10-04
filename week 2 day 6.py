#-------------------------------------------------------------------
print('----------------------- day 6 ---------------------------')
#-------------------------------------------------------------------

x = 2
y = 3.5
z = '13'
g = '13.5'

print ("int >> convert int , float or int str to integer ::")
print (int (x) , int (x+x))
print (int (y) , int (y+y))
print (int (z) , int (z+z))
print ("float >> convert int , float or str to float :")
print(float (x) , float (x+x))
print(float (y) , float (y+y) )
print(float (z) , float (z+z))
print(float (g))
print ("str >> convert int , float or str to string :")
print (str(x) , str(x+x))
print (str(y) , str(y+y))
print (str(z) , str(z+z))
print (str(g) , str(g+g))
 
#-------------------------------------------------------------------
print('----------------------- day 7 ---------------------------')
#-------------------------------------------------------------------

print("hello", 'hello')
A = "100dayprogramming"
B = """her i can write multiline string using three single or double quotes"""
print( A , B )
#Strings are arrays of bytes representing Unicode characters
#Square brackets can be used to access elements of the string
print(A[0 : 3])
print(A[3 : ])
print(A[-1])

#-------------------------------------------------------------------
print('----------------------- day 8 ---------------------------')
#-------------------------------------------------------------------
S = ' We will do it '
s = ' i\'m '                    #to print qoutes 
r = f"{S} {s} futun"            # = print(S + s)
print(s)
print(r)
print(S.strip())                #without  whitespace from end and beginning
print(S.lstrip())               #without  whitespace from left can changre to right use r
print(len(S))                   #length string
print(S.find("wil"))            #find index of this char
print("wil" in S )              #return boolean true or false
print("wil" not in S )
print(S.lower())                #string in lower case
print(S.upper())                #string in upper case
print(S.title())                #first char is upper
print(S.replace("We", "i"))     #replace string
print(S.split( ))               #split string and return as array
print(S.split( )[1])            


#-------------------------------------------------------------------
print('----------------------- day 9 ---------------------------')
#-------------------------------------------------------------------

#places number in the string where the placeholders { } are.

text = 'we on {} from {} day programming'
numb = 100
day  = 9
rem  = 81
text1 = 'we on {0} from {2} day programming Remainder {1} '
print(text.format(day , numb))
print(text1.format(day , rem , numb ))


#-------------------------------------------------------------------
print('----------------------- day  10 ---------------------------')
#-------------------------------------------------------------------

x = 8
y = 4
#Python Arithmetic Operators
print('addition        :' , x+y)
print('subtraction     :' , x-y)
print('multiplication  :' , x*y)
print('divison         :' , x/y)   #with float
print('floor divison   :' , x//y)  # integer
print('modulus         :' , x%y)   #remainder
print('exponentiation  :' , x**y)

#Python Assignment Operators
x = 2
x**=2
print(x)
x&=4              #bitwise and
print(x)
x|=2              #bitwise or
print(x)
x^=2              #bitwise xor
print(x)
x>>=2             #bitwise shift right
print(x)
x<<=2             #bitwise shift left
print(x)

#Python Comparison Operators

x ,y = 10 , 5
print('10==5',x==y)
print('10!=5',x!=y)
print('10>5',x>y)
print('10<5',x<y)
print('10>=5',x>=y)
print('10<=5',x<=y)

#-------------------------------------------------------------------
print('----------------------- day  11 ---------------------------')
#-------------------------------------------------------------------

k = 12
#Python Logical Operators

print (not(k>13 or k==12))  #and or not
# Python Identity Operators
# 'is' and 'is not'they are the same object, with the same memory location.  
f= {'apple', ' banana'}
g= {'apple', ' banana'}
p=f
i=g
print (f is g)
print (f is p)
print (g is not p)
#Python Membership Operators
print('apple' in f)

#-------------------------------------------------------------------
print('----------------------- day  12 ---------------------------')
#-------------------------------------------------------------------

order ="Please, I want {} sandwishes and {} donutes "
q= order.replace('i','We').format(5,7).replace('a','A')
print(q)

