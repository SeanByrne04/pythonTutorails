import random

for x in range(0,10):
    print(x,' ', end="")
#repeats 10 times 0 - 9

#cycle through a list
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
for y in grocery_list:
    print(y)

#define a list to go through
for x in [2,4,6,8,10]:
    print(x)

num_list=[[1,2,3],[10,20,30],[100,200,300]]
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])


random_num = random.randrange(0,100)
#a random number from 1 to 100

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)
#prints a random number from 1 to 100 until it reaches 15
        




        
            
        
    
    


