
# random module

import random

x=random.random()
print(x)

a=random.uniform(5, 10)
print(a)

b=random.randint(5, 10)
print(b)

liste=["a","b",3,"r",23,"df",6]

c=random.choice(liste)
print(c)

d=random.sample(range(10), k=3)
print(d)

random.shuffle(liste)
print(liste)