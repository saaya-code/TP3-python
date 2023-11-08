string_input = input("Donner une chaine : ")

voyelles = list(filter(lambda x: x.lower() in ["a","e","o","i","u","y"],string_input))
others = list(filter(lambda x: x.lower() not in ["a","e","o","i","u","y"] and x.isalpha(),string_input))

print(f"Le nombre des voyelles : {len(voyelles)}")
print(f"le nombre des consonnes : {len(others)}")