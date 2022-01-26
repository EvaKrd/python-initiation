y = int(input("Choisir une colonne de 1 à 5 ") )
x = int(input("Choisir une ligne de 1 à 5 2 ") )

if x and y==4:
    print("Touché")
elif x==4 and y!=4 or y==4 and x!=4:
    print("En vue")
else:
    print("A l'eau") 
    
