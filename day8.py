# num = [1,2,3,4,5,6]
# num.append(755)
# print(num)

num = []
even = []
odd = []
div = []
#Create list of 100 numbers
for i in range(1, 101):
        num.append(i)
print('list of numbers', num)

#Create list of Even and Odd numbers
for j in range(1,101):
        if j % 2 == 0:
            even.append(j)
        elif j % 2 != 0:
            odd.append(j) 
print('list of even numbers', even)
print('list of odd numbers', odd)

# Create list of numbers divisible by 3 & 5 numbers
for k in range(1,101):
      if k % 3 == 0 and k % 5 == 0:
            div.append(k)
print('divisible by 5 & 3 numbers',div)