#-------------------------------------------------------------------
print('----------------------- day  13 ---------------------------')
#-------------------------------------------------------------------
#A list Allows duplicate members,written with square brackets [].
list1=[ "ftoon" , 13 , 13.1 ]
print(list1)
list2=[13 , 14 , 15 , 16 , 17 , 18 , 19]
print(list1[0])
print(list1[-1])
for x in list2:
 print(x)
list1[2]= 'day'
print(list1)
del list1
del list2[0]
print(list2)

#-------------------------------------------------------------------
print('----------------------- day  14 ---------------------------')
#-------------------------------------------------------------------
mylist = ['i' , 'w' , 'i' , 'l' , 'l' , 'd' , 'o']
print(mylist[1:5])
print('i' in mylist)
if 'd' in mylist:
 print('i do it ')
w = ['don\'t stop '] * 2      # repeat item twice
print(w)
all= mylist + w
print(all)
# activity
integer= [ 2, 4, 6, 8, ]
float1= [ 0.25, 0.5 , 0.75 ]
allin=integer + float1
print(allin)

#-------------------------------------------------------------------
print('----------------------- day  15 ---------------------------')
#-------------------------------------------------------------------

list3=['Abdillah' , 'Emtessar' , 'Roaa' , 'Lina']
print(len(list3))
list3.append('my role model')      #To add an item to the end 
list3.insert(-1,'you are')         #To add an item at the specified index
print(list3)

list3.remove('you are')            #removes the specified item
print(list3)                       #if there many item have the same value 'remove' it will deledt the first item
list3.pop(4)                       # removes the specified index
print(list3)                       # the last item will remove if index is not specified
list3.clear()                      #method to empties the list.
print(list3)
# another method is 'del list2[0]'
'''
i cannot copy a list by typing list2 = list1, because: list2 will only be a reference
to list1, and changes made in list1 will automatically also be made in list2.
'''
list3=['Abdillah' , 'Emtessar' , 'Roaa' , 'Lina']

lis = list3.copy()                 #to copy list to another list lits exance
list3.append(4)
print("copy() function \n", lis)
print(list3)

lis = list3
lis.pop()
print("copy by equal sign\n" ,  list3)
print(lis)

num= list(list2)                    #Another way to make a copy
print(num)

go=list(('shooping','school','uni','hospital'))   #another way is list() to make a new list.

f=list(range(4))                    #print list in 4 items begin from 0
h=list(range(1,15,3))               #print list in ranfg between 1 to 15 and the increses by 3 [start,stop,step]
print(f)                            
print(h)                           
h.extend(f)
print(f)

go.extend(num)                      # add element of list to the list 
print(go)
                            
print(go.index('uni'))              #return the index of the item in the list

go.reverse()                        # revers the elemint list
print (go)

h.sort()                            #doesn't work with int and str element
print(h)           

print (h.count(1))                  #number of Refined element with the specified value


#-------------------------------------------------------------------
print('----------------------- day  16 ---------------------------')
#-------------------------------------------------------------------

# tuple is a collection which is ordered and unchangeable. like list but with round brackets ().
# cannot change or add or remove its values.unchangeable

frutestuple=('apple', 'orange','banana', 'mango')
emptytuple=()
onetintuple=(8,)    #if tuple has one element must be write with ,
tuple1=(3 , 5.2 , "ftoon" , "لا يمكن تغييرها")
print(frutestuple)
print(emptytuple)
print(onetintuple)
print(frutestuple[1])
for c in frutestuple:
          print(c)
del onetintuple
print(frutestuple[1:3])


#-------------------------------------------------------------------
print('----------------------- day  17 ---------------------------')
#-------------------------------------------------------------------

#To determine if an item is present in a tuple .

if "apple" in frutestuple and 'cherry' in frutestuple :
 print('yes, it is in tuple')

# repeat an item in a tuple, use the * operator
#must e typr , after item to understand it tuple
new=( 'good job',)*3
print(new + frutestuple)
x= (3,4,5,6)
x+=(1,2,3)
print(x)

# how many items a tuple has
print(len(x))

#another way to make tuple
#first round brackets to parameter of tuple function
#the second round brackets to like tuple
mytuple=tuple(('mac','asus','lenovo','dell'))
print(mytuple)

#example tople convert from element list to tuple 
thislist = [3,4,4,4,5,6,'A','B']
thistuple = tuple(thislist)
print(thistuple)
print(thislist)

print(thistuple.count(4))
print(thistuple.index("B"))
print(max(x),min(x),sum(x))

#-------------------------------------------------------------------
print('----------------------- day  18 & 19 ---------------------------')
#-------------------------------------------------------------------
#first
L=['black','red','yellow', 'green']
L.append('pruple')
L.insert(0,'bink')
L.remove('black')
L.reverse()
print(L)

tuple = ('java','python', 'swift')
print( 'python' in tuple )
