a = input('How many people do you need for Section A? Each ticket cost $150 ')
a = int(a)
b = 150
total = a * b

print ('You need ' , a , ' tickets for Section A. It will cost you ', total)


c = 3
d = 100
total2 = c * d
print ('You need ' , c , ' tickets for Section B. It will cost you ', total2)

import random
e = random.randint (1,10)
f = 50
total3 = e * f

print ('You need ' , e , ' tickets for Section C. It will cost you ', total3)

total4 = total + total2 + total3
print ('Your total is ' , total4)
z = .1
total5 = total4 - total4 * z 
print ('You will now be considered for a 10% discount')
if total4 > 1000:
    print ('Congratulations! You will recieve a 10% discount')
    print ('You bought' , a , 'tickets for section A' , c , 'tickets for section B, and ' , e , 'tickets for section C')
    print ('Your final total is ' , total5)
elif total4 < 1000:
    print ('Sorry, You are not able to recieve a 10% discount')
    print ('You bought' , a , 'tickets for section A' , c , 'tickets for section B, and ' , e , 'tickets for section C')
    print ('Your final total is ' , total4)


