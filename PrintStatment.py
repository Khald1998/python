print("Hello")
print('C')
print("7")
x = 5
print(x)
print("Hello \n")
#print("Hello")
print("No line above")
print("Between "+ "the " + "lines ")
print("Between"+' '+"the" +' '+ "lines2")
print("1", end = ' ')
print("2", end = ' ')
print("3")
print("A line of text.\n".rstrip())
#------
txt = "     banana     "

x = txt.rstrip() #Remove any white spaces at the end of the string:

print("of all fruits", x, "is my favorite")
#------
txt = "banana,,,,,ssqqqww....."

x = txt.rstrip(",.qsw") #Remove the trailing characters if they are commas, s, q, or w:



print(x)