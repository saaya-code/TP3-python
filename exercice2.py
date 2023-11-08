Semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
print("***Premier methode****")
for i in range(0, len(Semaine)):
    print(Semaine[i])

print("***deuxieme methode****")

for jour in Semaine:
    print(jour)
print("*"*16)

A=["lundi","mardi"]
B=["mercredi","jeudi"]
C=["vendredi","samedi","dimanche"]
Liste_A = A + B[1:] + C
print(Liste_A)
Liste_B = A + B + C[0:1]
Liste_B.sort(reverse=True)
print(Liste_B)