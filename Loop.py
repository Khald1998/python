# while loop
count = 0
while (count < 3):
    print("Hello",count)
    count = count + 1
#---
# combining else with while
count = 0
while (count < 3):
    count = count + 1
    print("Hello2")
else:
    print("In Else Block")
#---
# Iterating over range 0 to n-1

n = 4
for i in range(0, n):
    print(i)