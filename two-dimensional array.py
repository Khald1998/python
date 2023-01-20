# Creates a list containing 5 lists, each of 8 items, all set to 0
w, h = 3, 3
Matrix = [[0 for x in range(w)] for y in range(h)]
Matrix[0][0] = 1
Matrix[1][1] = 5
Matrix[2][2] = 9

#----
print(Matrix)
temp=""
for i in range(0, 3):
    for j in range(0, 3):
        #print(Matrix[i][j])
        temp +=str(Matrix[i][j])
    temp += "\n"
print(temp)
