import random
nbre_aleatoire = random.randint(1,100)
essai = 0

while True: 
    print("1:"  "Niveau facile vous n'avez que 10 essais")
    print("2:"  "Niveau Difficile vous n'avez que 5 essais")
    try:
        niveau = int(input("entrez 1 ou 2 pour votre niveau choisir"))
    except:
        print('entrez 1 ou 2')
        continue
    if niveau < 1  or niveau > 2:
        print('entrez 1 ou 2')
        continue
    break

if niveau == 1:
    essai_total = 10
else :
    essai_total = 5

while essai < essai_total:
    print('devinez le nombre entre 1 et 100')
    try:
        nombre = int(input('devinez le nombre'))
        
    except:
        print('entrez un nombre compris entre 1 et 100')
        continue
    
    if nombre < 1 or nombre >100:
        print('entrez un nombre compris entre 1 et 100')
        continue
    essai += 1
    
    if nombre < nbre_aleatoire:
        print(f"C'est plus petit !, votre essaie est de {essai}")
    elif nombre > nbre_aleatoire:
        print(f"C'est plus grand !, votre essaie est de '{essai}")
    else :
        print("Bravo!!!!")
        print(f"votre nobre d'essai est de de, votre essaie est de {essai}")
        break
if niveau == 1 and essai == 10:
    print(f"Vous avez atteint la limite des essais qui est de :, {essai_total}")
elif niveau== 2 and essai == 5:
    print(f"Vous avez atteint la limite des essais qui est de :, {essai_total}" )
    


    