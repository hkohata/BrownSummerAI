import math as m
import random as r

result_1 = m.pow(2,4)
print("result_1 is " , result_1)

result_2 = m.sqrt(36)
print ("result_2 is ", result_2)

result_3 = r.randint(0,100)
print ("result_3 is" , result_3)

names = ("a", "b", "c", "d", "e", "f", "g")
print("Originl names: " , names)

r.shuffle(names)
print("Names after shuffle: " , names)

result_4 = r.choice(names)
print("Chosen name is: " , result_4)