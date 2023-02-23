from datetime import datetime


f = open("listEtudiant.txt","a")
f.close()

mydatetime = datetime.now()
jour=mydatetime.strftime("%Y-%m-%d")
heure=mydatetime.strftime("%H:%M")

def ajouterEtudiant():
    f=open("listEtudiant.txt","a")
    nom=input("Donner le Nom \n")
    prenom=input("Donner le Prenom \n")

    
    f.write("\n")
    f.write(str(nom)+" "+ str(prenom)+" "+ str(jour)+" "+ str(heure))
    f.close()
    print("Etudiant enregistrer avec succes \n")
    

def listerEtudiant():
    f=open("listEtudiant.txt","r")
    print("Liste des etudiants \n")
    for x in f:
        print(x)
    f.close()
    
def rechercheEtudiant():
    f=open("listEtudiant.txt","r")
    nomRecherche = input("Entree le nom l'etudiant a afficher \n")

    if nomRecherche in f.read():
        print(nomRecherche, "est dans la liste\n")
    else:
        print(nomRecherche,"n'est pas dans la liste\n")
    f.close()


def menu():
    print("1- Ajouter un etudiant !")
    print("2- Rechercher un etudiant !")
    print("3- voir la liste des etudiants !")
    print("4- Quitter!")
    
    choix = input("Qu'est ce tu veux faire 1, 2, 3, 4\n")
    
    if choix == "1":
        ajouterEtudiant()
        menu()
    elif choix == "2":
        rechercheEtudiant()
        menu()
    elif choix =="3":
        listerEtudiant()
        menu()
    elif choix =="4":
        print("Au revoir")
    else:
        print("Votre est invalide .")
        

menu()