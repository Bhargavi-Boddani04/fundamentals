#Arithmetic Operators
print("****************Aritmetic program started**************************")

#Addition
num_1=20
num_2=40
result=num_1+num_2
print("addition of num1,num2 is",result)

#num1=int(input("Enter num_1 value is "))
#num2=int(input("Enter num_2 value is "))
print("sum of value num3 is ",num_1+num_2)

#Subtract
print("subtract value is",num_1-num_2)
#multiplication
print("multiplication value is ",num_1*num_2)
#Division
print("Division value is",num_1/num_2)
#floor Division
print("floor division value is",num_1//num_2)
#Modulas value
print("Modulas value is",num_1%num_2)
#Exponential value
print("Exponential value is",num_1**num_2)
print("*********************Arithmetic program ended*****************")

#Assignment operators
print("********assignment operator program started")

num_1+=4
num_2+=4
print("added 4 to num_1",num_1)
print("added 4 to num_2",num_2)

num_1*=3
num_2*=3
print("Multiply 3 to num_1",num_1)
print("Multiply 3 to num_2",num_2)

print("*************assignment operator program ended***********")

#comparision operators
print("********Comparision operator program started***********")

apple=200
banana=50
grapes=50
print(apple==apple)
print(grapes==banana)
print(apple!=banana)
print(apple>banana)

print("*************comparision operator program ended**************")

#logical operators
print("*****************logical operator program started***************")
username="Bhargavi"
password=2345
print(username=="Bhargavi"and password==2345)
print(username=="devi"and password==2345)
print(username=="Bhargavi"and password==2345)

print("*********************logical operator program ended*******************")


#identity operators
print("********************Identity operator program started******************")
sample1=["Bhargavi",2,3,4]
sample2=["Devi,2,3,4"]
print(id(sample1))
print(id(sample2))
print(sample1 is sample2)
print(sample1 is not sample2)

print("****************identity operator program ended****************")

#Membership operators
print("*****************Membership operator program started*********************")
fruits=["Apple,Mango,Grapes"]
print("apple"in fruits)
print("Mango"in fruits)
print("Grapes"in fruits)
print("carrot"not in fruits)

print("*****************Membership opertor program ended*********************")

#F-string
print("*******************F-string program started*******************")
product_cost=300

discount=20
result=product_cost*(discount/100)
product_cost-=result
print(product_cost)
print(f"discount given {discount}% and final discount{result} and total cost after discount{product_cost}/-")
print("*****************F-string program ended***************")

#coding exercise
#calculate area of Rectangular 
length=20.30
width=4.0
print("Rectangular area",length*width)
length+=2
width-=2
print("Length incremental,width decremental updated Rectangular area",length*width)

#temperature calculation
celsius=float(input("Enter temperature in Celsius"))
F_result=(celsius*(7/5))+32
print(f"Temperature in {celsius} 'C Celsius converted to Fahrenheit {F_result}'F")

#Calculate simple  intrest
principal=float(input("Enter the rate of intrest per annum:"))
rate=float(input("Enter the time period(in years)"))
time=float(input("Enter time period(in years)"))
simple_intrest=(principal*rate*time)/100
print(f"simple_intrest is:{simple_intrest}")

#concatenate two strings
first_name=input("enter first name")
last_name=input("enter last name")
print("firstname lastname is ",first_name+last_name)

#convert distance kilometers to miles
kilometers=float(input("Enter kilometers"))
conversion_factor=0.236581
miles=kilometers*conversion_factor
print(f"{kilometers}kilometers converted to miles {miles}")


      
