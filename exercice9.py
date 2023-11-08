dict = {}

chaine = input("Donner une chaine : ")
last_chaine = list(filter(lambda x: x.isalpha(),"".join(chaine.split(" "))))
nombres_des_chars = len(last_chaine)
print(f"Le nombre des caractère : {nombres_des_chars}")

for char in last_chaine:
    if char not in dict:
        dict[char] = 1
    else:
        dict[char] += 1

for key,val in dict.items():
    print(f"{key} : {(val/nombres_des_chars)*100}%")
