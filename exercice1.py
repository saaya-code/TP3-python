Nb_jours=[31,28,31,30,31,30,31,31,30,31,30,31]
Mois=["janvier","Février","Mars","Avril","Mai","Juin","juillet","Aout","Septembre","Octobre","Novembre","Décember"]
Mois_affiche = map(lambda x: "'"+x+"'",Mois)
print(",".join(Mois_affiche ))
T3 = []

for i in range(0,len(Nb_jours)):
    T3.append(Mois[i])
    T3.append(Nb_jours[i])


print(T3)