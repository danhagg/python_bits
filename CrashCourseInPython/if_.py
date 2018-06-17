cars = ['Audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car.lower() == 'audi':
        print(car.upper())
    else:
        print(car.title())

# using not "!"
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies")

# testing for numerical comparison
age = 18
if age == 18:
    print("true")

# checking multiple conditions "and" "or"
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 <= 21:
    print("yeah, in both cases")

if age_0 == 21 or age_1 >= 17:
    print("ja, a single one")

#check if a value is in list with "in"
if "mushrooms" in requested_topping:
    print ("yeah we got mushrooms")

#checking if value is "not in" a list + "else"
banned_users = ['andrew', 'susie', 'marlon']
user = 'andrew'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
else:
    print(user.title() + ", you\'ve been banned, dickhead")

#if, elif, else
age_movie = 12
if age_movie < 4:
    print("Free admission")
elif age_movie < 18:
    print("thats a tenner")
else:
    print("Its 20 fer adults")

#can be done more efficiently? where you only type one print statement
age1 = 13
if age1 < 4:
    price = 0
elif age1 < 18:
    price = 5
else:
    price = 10
print ("your admission is " + str(price) + "!")

#python does not require the final else block of code, eg a final elif instead
# elif age >= 65:
# price = 5

#if list_name: #returns True if list is not empty
    #for item in list_name:
        #do code
