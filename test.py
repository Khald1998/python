import pandas as pd
import numpy as np
from sklearn import linear_model
#===================================================================================
# This is only for testing
def print_matrix(Title, M):
    print(Title)
    for row in M:
        print([round(x,3)+0 for x in row])
        
def print_matrices(Action, Title1, M1, Title2, M2):
    print(Action)
    print(Title1, '\t'*int(len(M1)/2)+"\t"*len(M1), Title2)
    for i in range(len(M1)):
        row1 = ['{0:+7.3f}'.format(x) for x in M1[i]]
        row2 = ['{0:+7.3f}'.format(x) for x in M2[i]]
        print(row1,'\t', row2)
        
def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)

    return A

def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]

    return MC

def matrix_multiply(A,B):
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        print('Number of A columns must equal number of B rows.')

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C
#===================================================================================    
x_Data = [] #all values of X(s) in order
y_Data = [] #all values of Y(s) in order

flag1 = False
while(not flag1):
    n = int(input('Enter the model size n, (the maximum model size is 200): \n'))
    if(1 <= n and n <= 200):
        flag1 = True
    else:
        print('Wrong input, enter again')    
 
flag2 = False
while(not flag2):
    t = int(input('Enter training size, (must be >= n): \n')) 
    if(n <= t):
        flag2 = True
    else:
        print('Wrong input, enter again')      
  
#===================================================================================    
# Here we make the synthetic data
data = {
        'y': np.random.ranf(t) + np.random.randint(0, 10, t)     
        }
for j in data.get('y'):
    y_Data.append(round(j, 6))
ar = []
for i in range(1, n+1):

    st = 'x' + str(i)
    ar.append(st)
    data[st] = np.random.ranf(t) + np.random.randint(0, 10, t)
    for j in data.get(st):
        x_Data.append(round(j, 6))
  
df = pd.DataFrame(data)
print("df\n",df,"\n")
   

x = df[ar]
y = df['y']
# with sklearn
#===================================================================================    
 # Here we make the linear_model
 
regr = linear_model.LinearRegression()
regr.fit(x, y)

print('B0: ', regr.intercept_)
index = 1
for i in regr.coef_:
    print('B' + str(index) + ': ', round(i,6))
    index = index + 1
print('\n')

#===================================================================================
#The algorithem

modelSize = n+1 #The reason why we add 1 to the modil size is because we will consider X0 since it is not included in the model size before
tSize = t #The training data 
Y_matrix = [0 for j in range(tSize)] 
X_matrix = [[0 for i in range(modelSize)] for j in range(tSize)]
X_matrixT = [[0 for i in range(tSize)] for j in range(modelSize)] # This is X matrix but transpose matrix
I = [[0 for i in range(modelSize)] for j in range(modelSize)] # This is Identity matrix
I2 = [[0 for i in range(modelSize)] for j in range(modelSize)] # a copy of Identity matrix
A= [[0 for i in range(modelSize)] for j in range(modelSize)] # This is the matrix that should be inverted and it is the result of the matrix multiplication of X and its transpose
A2 = [[0 for i in range(modelSize)] for j in range(modelSize)] # a copy of A
matrix_m2 = [[0 for i in range(tSize)] for j in range(modelSize)] # the result of the matrix multiplication of A and X transpose
matrix_B = [0 for j in range(modelSize)] # output
#===================================================================================

for i in range(modelSize): # making I
    I[i][i]=1
#print_matrix('\n\n\nI', I)

for i in range(tSize): # Read data 
    Y_matrix[i]=y_Data[i]
print('\n\n\n Y_matrix\n',Y_matrix)
new_x_data=[]
#===================================================================================
#Here we add X0 to the data 
for i in range(tSize):
    new_x_data.append(1) 

for i in range(len(x_Data)):
    new_x_data.append(x_Data[i])
#===================================================================================
for i in range(modelSize):#read data
    for j in range(tSize):
        #print(new_x_data[i*(tSize)+j]," ",i*(tSize)+j)
        X_matrix[j][i]= new_x_data[i*(tSize)+j]
        X_matrixT[i][j]= new_x_data[i*(tSize)+j]
#print_matrix('\n\n\n X_matrix', X_matrix)
#print_matrix('\n\n\n X_matrixT', X_matrixT)

#===================================================================================
# matrix mult between X and X transpose
for i in range(len(X_matrixT)):
    for j in range(len(X_matrix[0])):
        for k in range(len(X_matrix)):
            A[i][j]+= round(X_matrixT[i][k]*X_matrix[k][j],6)
            A2[i][j]+= round(X_matrixT[i][k]*X_matrix[k][j],6)
#print_matrix('\n\n\n A', A)
#print_matrix('\n\n\n A2', A2)

#===================================================================================

# here we do the invers


fd = 0 # fd stands for focus diagonal OR the current diagonal
fdScaler = 1. / A[fd][fd]

for j in range(len(A)): # using j to indicate cycling thru columns
    A[fd][j] = fdScaler * A[fd][j]
    I[fd][j] = fdScaler * I[fd][j]

indices = list(range(len(A)))

for i in indices[0:fd] + indices[fd+1:]: # *** skip row with fd in it.
    crScaler = A[i][fd] # cr stands for "current row".
    for j in range(len(A)): # cr - crScaler * fdRow, but one element at a time.
        A[i][j] = A[i][j] - crScaler * A[fd][j]
        I[i][j] = I[i][j] - crScaler * I[fd][j]

indices = list(range(len(A))) # to allow flexible row referencing ***


for fd in range(1,len(A)): # fd stands for focus diagonal
    fdScaler = 1.0 / A[fd][fd]


    # FIRST: scale fd row with fd inverse. 
    for j in range(len(A)): # Use j to indicate column looping.
        A[fd][j] *= fdScaler
        I[fd][j] *= fdScaler  


    for i in indices[:fd] + indices[fd+1:]: # *** skip row with fd in it.
        crScaler = A[i][fd] # cr stands for "current row".
        for j in range(len(A)): # cr - crScaler * fdRow, but one element at a time.
            A[i][j] = A[i][j] - crScaler * A[fd][j]
            I[i][j] = I[i][j] - crScaler * I[fd][j]

#print_matrix('\n\n\n I', I)


#print_matrix('Proof of Inversion', matrix_multiply(A2,I))





for i in range(len(I)):
    for j in range(len(X_matrixT[0])):
        for k in range(len(X_matrixT)):
            matrix_m2[i][j]+= I[i][k]*X_matrixT[k][j]
#print_matrix('\n\n\n matrix_m2', matrix_m2)

for i in range(modelSize):
    for k in range(tSize):
        matrix_B[i]+= matrix_m2[i][k]*Y_matrix[k]            
ind=0
print('\n')
for i in matrix_B:
    print('B' + str(ind) + ': ', round(i,6))
    ind+=1



        
    

