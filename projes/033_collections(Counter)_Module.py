#Counter Module

from collections import Counter
import random

liste1=random.sample(range(10), k=6)
liste2=random.sample(range(10), k=6)
liste3=random.sample(range(10), k=6)
liste4=random.sample(range(10), k=6)

listelerin_listesi=[liste1,liste2,liste3,liste4]
listelerin_toplami=liste1+liste2+liste3+liste4

print(listelerin_listesi)
print(listelerin_toplami)

print(Counter(listelerin_toplami))

print(Counter(listelerin_toplami).most_common(1))