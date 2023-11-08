ch = "un bon étudient est celui qui révise chaque jour son cours"

ch1 = ch.split(" ")[1]
print(f"ch1 = {ch1}")

ch2 = " ".join(ch.split(" ")[0:2]) +" "+ (ch.split(" ")[1]*2)

print(ch2)