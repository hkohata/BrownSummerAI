from math import pow as power
from math import sqrt as root
from random import randint as randomint
from random import shuffle as shuf
from random import choice as choose

result_1 = power(2,4)
print("result_1 is " , result_1)

result_2 = root(36)
print ("result_2 is ", result_2)

result_3 = randomint(0,100)
print ("result_3 is" , result_3)

names = ("a", "b", "c", "d", "e", "f", "g")
print("Originl names: " , names)

shuf(names)
print("Names after shuffle: " , names)

result_4 = choose(names)
print("Chosen name is: " , result_4)