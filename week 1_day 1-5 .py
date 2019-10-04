#--------------------------------- day 1 & 2 ----------------------------------
print("hi i'm futun")                            #the syntax for print(object(s), separator=separator, end=end, file=file, flush=flush)
print("Hello", "how are you?", sep=" ---")       #https://www.w3schools.com/python/ref_func_print.asp
print("\U0001f600")                              # print emoji must be start with backslash and replace “+” with “000” using unicode table
print("\N{grinning face}")                       #to print any emoji using CLDR SHORT NAME must be type backslash and  "N"
                                                 #print(emoji.emojize(":grinning_face_with_big_eyes:"))
                                                 #to print by using emojize() function requires the CLDR short name but doesn't work 
 # exit()                                        # to exit from python shell and if I write it in middle it should be getting out and skip the other lines
"""
this for comment than one line 

""" 
#--------------------------------- day 3 ----------------------------------
x= 6
y= 9
if y>x :                                         # function, loop etc.) starts with indentation and ends with the first unindented line lik braces in c++
 print (x)        

_single1, double2 =  'hi' , "hi" 
print ( _single1 , double2 , sep="=")            #the single quotes equal to double 

e = "\U0001F648"
print("I like python" + e )                      # to print variable with text use + between it 
 
A , B , C , D = "string" , "string" , 5 , 6 

print(A + B ) 
print(C + D )                                    # CANNOT PRINT STRING + INT

#--------------------------------- day 4 ----------------------------------                

q = -43502279102548                              #int positive or nigative and long without decimals
p =  448461548.588                               #float positive or negative and decimals,"e" to indicate the power of 10
r = 3+4j                                         #complex "j" as the imaginary part,cannot change "j"
print (type(p))                                  # verify type of variables
r.real                                           # print only real part 
r.imag
s = complex(p)                                   # convert from type to type but cannot conver from complex to another type  
print (s) 

import random                                    #call random,it is module in python
print (" random number ",random.randrange(1,100))  #display a random number from 1 to 9

from random import randint                        #another method to callrandom
print(randint(1,10))                              #int random number
#--------------------------------- day 5 ----------------------------------  

x , y , z = "apple" ,  "orange" , "limon"

basket = x + y + z

print(basket)
print(len(basket))

x = basket[0:len(x)]                               #len() return number of letter
y = basket[len(x):len(x)+len(y)] 
z = basket[len(x)+len(y): len (basket)]
print (x, y, z , sep='\n')


print(" leason 1 to 5 are done ")  
print(" thank you saudi developer orgnizathion " + "\U0001F497")  


