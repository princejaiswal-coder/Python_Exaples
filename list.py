#list examples
import random

random_num = random.randint(1,5)

fruits = ["Apple","Mango","Strawberry","Coconut","Banana","Grapes"]

# We Can Change The Value Inside The List !!
fruits[0] = "Pineapple"

# We Can Add Words To The List
fruits.append("This Is Added Word !!")

# We Can Add List To The Fruits List
fruits.extend(["This Is Added List","1",2,True,False])

print(fruits)
