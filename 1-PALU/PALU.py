import numpy as np

def PALU(A):
    cA = np.array(A)
    dimensions = np.shape(A)

    if(dimensions[0] != dimensions[1]):
        return print("La Matriz ingresada no es cuadrada")

    L = np.eye(dimensions[0])
    U = np.eye(dimensions[0])
    print("Matriz Original \n" + str(cA))
    for j in range(0,dimensions[0]):
        for i in range(j+1,dimensions[0]):
            L[i,j] = cA[i,j]/cA[j,j]
            print("L: \n" + str(L))
            cA[i,0:] = cA[i,0:] - (L[i,j] * cA[j,0:])
            print("A: \n" + str(cA))
    
    if(L*U == A):
        print("Resultado correcto")
            


A  = np.array([
    [3,-7,-2],
    [-3,5,1],
    [6,-4,0]
])

# A[2,0:] = A[2,0:]  * 2 
# print(A)

# PALU(A)

a = np.array([
        (1,2,3),
        (4,5,6)
    ])

print(a[0:,2])