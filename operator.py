#Operator
print("# Arithmetic Operators #")

x = 2
y = 5

print( x + y )  #Addition
print( x - y )  #Subtraction
print( x * y )  #Multiplication
print( x / y )  #Divition 
print( x % y )  #Modulus
print( x ** y)  #Exponention
print(x // y )  #Floor divition
print("\n")
print("# Assignment Operator #")

x = 5          #x=5
print(x)       

x +=3          #x=x+3
print(x)

x -=3          #x=x-3
print(x)

x *=3          #x=x*3
print(x)

x /=3          #x=x/3
print(x)

x %=3          #x=x%3
print(x)

x //=3         #x=x//3
print(x)

x=2
x **=3         #x=x**3
print(x)

x = 5
x &=3          #x=x&3 
print(x)       #(0101 & 0011 = 0001 = 1 )

x |=3          #x=x|3 
print(x)       #(0001 | 0011 = 0011 = 3 )

x = 4
x^=3           #x= x^3
print(x)       #(0100 ^ 0011 = 0111 = 7)

x>>=3          #x=x>>3
print(x)       #(0111 >> 3  = 0000)

x=1
x<<=3          #x=x<<3
print(x)       #(0001<< 3   = 1000)

print("\n")
print("# Comparision Operator #")

y=10
print(x==y)   
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
print("\n")
print("# Logical Operation #")

print(x>3 and x<10)       #Returns true if both statements are true
print(x>5 or  x<4)        #Rerurns true if one of the statement is true 
print(not(x>3 and x<10))  #Revere the result, returns False if the result is true 
print("\n")
print("# Identity operators #")
#is

x = ["xiaomi","oppo"]     #Return true if both variable are the same object            
y = ["xiaomi","oppo"]
z = x
print(x is z)             #return True becasue z is the same object as x 
print(x is y)             #return False because x is no the same object as u,even if they have the same content 
print(x == y)             #to demonstrate the different between "is" and "==":this comparison retrun True because x is equal to y
print("\n")
#is not                   #Return true if both variable are not the same object 

print(x is not z)         #return False because z is the same object as x
print(x is not y)         #return True because x is not the same object as y,even if they have the same content 
print(x != y)             #to demonstrate the different between "is not" and "!=": this comparison returns False because x is equal to y
print("\n")

print("# Membership operators #")

x=["xiaomi","oppo"]
print("oppo"in x)         #Returns True if a sequence with the specifieed value is present in the object 

print("vivo"not in x)     #Return True if a sequence with the specified value is not present in  the object 
print("\n")

print("# Bitwise operator #")
x=10
y=4
print(x&y)             #AND:(1010 & 0100 = 0000 =0 )
print(x|y)             #OR:(1010 | 0100 = 1110 =14)
print(x^y)             #XOR:(1010 ^ 0100 = 1110 = 14)
print(~x)              #NOT:~1010 =-(1010+1)=-1011=-11(Decimal) Returns 1,s complement of the number 
print(x>>1)            #Right shift (1010>>1 = 0101)
print(x<<1)            #Left shift  (1010<<1 = 0001 0100 = 20)
