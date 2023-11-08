A = [[1,22,34],[3, 34, 4],[4,7,88]]
B = [[10,5,19],[11,8,9],[4,6,6]]

somme = [[A[i][j] + B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]
print(somme)

A_B = [[A[i][j] - B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]
print(A_B)

Formule = [[(3*A[i][j]) + (10*B[i][j])  for j in range(len(A[0]))] for i in range(len(A))] 
print(Formule)