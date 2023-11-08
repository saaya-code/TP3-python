taille = int(input("Donner la taille de la liste : "))

while taille < 0:
    taille = int(input("Donner la taille de la liste (positive) : "))
t = []
for i in range(0, taille):
    x = int(input(f"Donner le t[{i}] : "))
    t.append(x)


print(f"La somme de la liste : {sum(t)}")
print(f"La valeur max de la liste = {max(t)}")
print(f"La valeur min de la liste = {min(t)}")

