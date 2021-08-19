age = 30   #sets an integer value
if age > 16 :
    print('You are old enough to drive')
else :
    ('You are not old enough to drive')

if age >= 21 :
    print('You are old enough to drive a tractor trailer')
elif age >= 16 :
    ('You are old enough to drive a car')
else : print('You are not old enough to drive')

if ((age >= 1)and(age <= 18)):
    print('you get a birthday')
elif((age == 21)or(age >= 65)) :
    print('you get a birthday')
elif not(age == 30) :
    print("You don't get a birthday")
else :
    print('You get a birthday party')
