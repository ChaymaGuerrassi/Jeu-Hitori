
##Tâche1 : Chargement des niveaux 

def lire_grille(nom_fichier):
    
    ''' Fonction qui prend en argument un fichier, et 
    le parcours en renvoyant une liste de listes décrivant 
    les valeurs des cellules de la grille.
    Param. reçu : nom_fichier : str
    Param. renvoyé : liste de listes : lst'''

    for x in range (0,len(fichier)):
        lst=[]
        for y in range (len(fichier[x])):
            if (fichier[x][y] != ' '):
    
                lst.append(fichier[x][y])
    
        liste_de_liste.append(lst)

    
    
def afficher_grille(grille):
    
    '''Fonction permettant d'afficher un plateau avec
    les valeurs 
    de la grille sur le terminal.
    Param. reçu : grille : lst
    Param. renvoyé : aucun '''
    
    for ligne in grille : 
        print()
        print('---+'*(len(grille)+1)) #Séparation des lignes
        print('|',end='')
        
        for elem in ligne:
            
            print(elem,'| ',end='') #Séparation des colonnes
            
    print()
    print('---+'*(len(grille)+1))        
           
            
def ecrire_grille(grille, nom_fichier):
    
    ''' Fonction qui sauvegarde une grille dans un fichier 
    donné en paramètre.
    Param. reçu : grille : lst
                : nom_fichier : str '''
    
    fic= open(nom_fichier, 'w')
    for ligne in grille :
        
        for i in ligne :
            
            fic.write(i+' ')
        fic.write('\n')
    
    fic.close()


##Tâche 2 : Moteur du jeu

def position(grille,element):
    
    '''Fonction renvoyant une liste de tuples représentant le numéro 
    de ligne et de colonne d'une valeur de la grille.
    Aussi, elle remplace les valeurs dont les coordonnées sont dans 
    noircies par None.
    Param. reçu : grille : lst
                : element : str
    Param. renvoyé : pos : lst'''
    
    pos=[]
    for i,j,val in cases_noircies :
        grille[i][j] = None
            
    for i in range (len(grille)):
        for j in range(len(grille[i])):
                
            if grille[i][j]==element:
                
                pos.append((i,j))
    return pos
        

def testligne_colonne(grille,element):
    
    ''' Cette fonction parcours la liste de listes de positions 
    de l'élément et renvoie False si la règle n°1 n'est pas 
    respectée et True sinon.
    Param. reçu : grille : lst
                : element : str
    Param. renvoyé : booléen '''
        
    list_pos = position(grille,element)
    
    for i in range(len(list_pos)-1):
                
        for j in range(len(list_pos[0])-1):
                    
            for r in range((len(list_pos)-i)-1):
                    
                if list_pos[i][j]== list_pos[i+r][j]: 
                    #parcours pour la première coordonnée(ligne)        
                    return False
                            
                            
                elif list_pos[i][j+1]== list_pos[i+r][j+1] : 
                    #parcours pour la deuxième coordonnée(colonne)
                    return False
                    
    return True 


def sans_conflit(grille,noircies):
    
    '''Fonction renvoyant True si la règle n°1 est vérifiée et 
    False sinon.
    Param. reçu : grille : lst
                : noircies : set
    Param. renvoyé : booléen'''
    
    
    for ligne in grille :
        for elem in ligne :
            
            if elem is not None: #Les cellules visibles 
                conflit = testligne_colonne(grille,elem)
    
    return conflit
    
    
def sans_voisines_noircies(grille,noircies):
    
    '''Fonction renvoyant True si la règle n°2 est vérifiée et 
    False sinon.
    Param. reçu : grille : lst
                : noircies : set
    Param. renvoyé : booléen'''
    
    for i,j,val in cases_noircies:
        grille[i][j]= None

    for ligne in range (len(grille)-2):
    
        for colonne in range(len(grille[ligne])-1):
            
            if grille[ligne][colonne] == grille[ligne][colonne+1] and grille[ligne][colonne]==None:
                
                return False
            
            elif  grille[ligne][colonne] == grille[ligne+1][colonne] and grille[ligne][colonne]==None:
                
                return False
    
    return True
    
        

def connexe(grille,noircies):
    
    '''Fonction renvoyant True si la règle n°3 est vérifiée et
     False sinon.
    Param. reçu : grille : lst
                : noircies : set
    Param. renvoyé : booléen'''
    
    def in_grille(grille, i, j):
        
        """Renvoie True si la case (i, j)
        est une case de la grille, False sinon.
        """
        return (-1 < i < len(grille) and -1 < j < len(grille[i]))
        
    def cellules_voisines(i, j):
        
        return [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
        
        
    def zone (grille,i,j,noircies,ensemble):
        
        """Parcours les cases non noircies et les stock dans un ensemble. Si le
        nombre d'éléments de l'ensemble est égal au nombre de case non noircies de la grille renvoi True, sinon False
        """
        
        for elem in cellules_voisines(i,j):
            
            if in_grille(grille,elem[0],elem[1]) is True and elem not in noircies and elem not in ensemble:
                ensemble.add(elem)
                zone(grille,elem[0],elem[1],noircies,ensemble)
                if len(ensemble) == len(grille)*len(grille[0])-len(noircies):
                    return True
                    
                
    i,j = 0,0            
    ensemble = set()              
    zone = zone(grille,i,j,noircies,ensemble)
    
    if zone is True:
        return True
    else:
        return False


##Tâche 3 : Interface Graphique  

def graph_grille(grille):

    """
    parcourt la grille en le faisant afficher sur 
    l'interface graphique
    """
    
    for  n in range (0,len(grille)):
        for m in range (0,len(grille[n])):

            rectangle(m*49,n*49,(m+1)*49,(n+1)*49,couleur='black', remplissage='', epaisseur=5, tag='')
            texte((m*49+(m+1)*49)/2, (n*49+(n+1)*49)/2, grille[n][m], couleur='black', ancrage='nw', police='Helvetica', taille=20, tag='')


def ajout_cases_noircies(grille,coord_x,coord_y):

    """
    ajoute une case noircie sur l'interface graphique
    """

    presence = 0

    n = 49
    if 0<coord_x<392 and 0<coord_y<392:
        
        coord_x = int(coord_x/n+1)
        coord_y = int(coord_y/n+1)
        j=coord_x
        i = coord_y
    
        if (j,i)==(coord_x,coord_y):
            rectangle((j*n)-n,(i*n)-n,j*n,i*n,couleur='black', remplissage='black', epaisseur=5, tag='')
        
            for (i2,j2,val2) in cases_noircies:
                if (i2 == i-1 and j2 == j-1):
                    presence = 1

            if (presence == 0):
                cases_noircies.append((i-1,j-1,grille[i-1][j-1]))
            print(cases_noircies)

    presence = 0
    mise_a_jour()
  

def victoire():

    """
    message de félicitation en cas de victoire
    """

    texte(120, 100,"Félicitations", couleur='red', ancrage='nw', police='Bradley Hand', taille=55, tag='')
    texte(70, 150,"Vous avez gagné", couleur='red', ancrage='nw', police='Bradley Hand', taille=50, tag='')
    texte(250, 200,"!", couleur='red', ancrage='nw', police='Bradley Hand', taille=50, tag='')
    mise_a_jour()


def menu():

    """
    affichage du menu comprenant les boutons : 
    Quitter, Recommencer, Autre grille et Annuler
    """

    rectangle(399, 40, 539, 80,couleur='black', remplissage='green', epaisseur=3, tag='')
    texte(434, 50,"Quitter", couleur='black', ancrage='nw', police='Bradley Hand', taille=22, tag='')
    

    rectangle(399, 110, 539, 150,couleur='black', remplissage='green', epaisseur=3, tag='')
    texte(404, 120,"Recommencer", couleur='black', ancrage='nw', police='Bradley Hand', taille=22, tag='')
    

    rectangle(399, 180, 539, 220,couleur='black', remplissage='green', epaisseur=3, tag='')
    texte(409, 190,"Autre grille", couleur='black', ancrage='nw', police='Bradley Hand', taille=22, tag='')


    rectangle(399, 250, 539, 290,couleur='black', remplissage='green', epaisseur=3, tag='')
    texte(429, 255,"Annuler", couleur='black', ancrage='nw', police='Bradley Hand', taille=22, tag='')
    mise_a_jour()


def annuler(noircies):
    
    """
    cette fonction annuler permet de supprimer le dernier élément de la liste
    cases_noircies et "superposer" une case blanche
    """
    
    if len(cases_noircies)> 0:
        (x,y,val) = cases_noircies[len(cases_noircies)-1]
        liste_de_liste[x][y] = val
        cases_noircies.pop(len(cases_noircies)-1)
        print(cases_noircies)

        rectangle(y*49,x*49,(y+1)*49,(x+1)*49,couleur='black', remplissage='white', epaisseur=5, tag='')
        texte((y*49+(y+1)*49)/2, (x*49+(x+1)*49)/2, val, couleur='black', ancrage='nw', police='Helvetica', taille=20, tag='')

    
    
    
##Tâche 4 : Solveur 
def resoudre(grille,noircies,i,j):
   
    '''fonction qui implemente une recherche automatique de solution 
    à partir de la configuration (i,j). Elle parcours les cellules une 
    par une et renvoie un ensemble de solution noircies si une solution 
    est trouvée et None sinon.
    Param. reçus : grille : lst
                 : noircies : set
                 : i, j : int
    Param. renvoyés : noircies : set
                    : None '''
    
    
    regle1 = sans_conflit(grille, noircies)
    regle2 = sans_voisines_noircies(grille, noircies)
#regle3 = connexe(grille, noircies)

                
    if sans_conflit(grille, noircies) and sans_voisines_noircies(grille, noircies) :
        #Base case 
        #ajouter connexe
        return True 
        

    elif sans_voisines_noircies(grille, noircies) == False or connexe(grille, noircies) == False :# ajouter connexe #Grille invalide
        return None 
    
    elif sans_conflit(grille, noircies) == False :#ajouter connexe
        
        cellule = grille[i][j]
        
        if testligne_colonne(grille, cellule):
            resoudre(grille, noircies,i+1,j)
            resoudre(grille, noircies, i, j+1)
             
        else :
            noircies.add((i,j))
            resoudre(grille, noircies,i+1,j)
            resoudre(grille, noircies, i, j+1)
            
    return noircies    
    

 
    
##Principal                
from upemtk import *

#grille =[[2,2,1,5,3],[2,3,1,4,5],[1,1,1,3,5],[1,3,5,4,2],[5,4,3,2,1]]

#noircies = {(2, 0), (0, 0), (3, 3), (2, 2), (3, 1), (0, 2), (1, 4)}
#grille = lire_grille('niveau2.txt')
#noircies = {(2, 0), (0, 0), (3, 3)}

#regle1 = sans_conflit(grille, noircies)
#regle2 = sans_voisines_noircies(grille, noircies)
#regle3 = connexe(grille, noircies)

#print(regle1,regle2, regle3)


#print(resoudre(grille, noircies, 0, 0))

liste_de_liste=[]
cases_noircies = []


cree_fenetre(549,392)

for n in range (1,6): 
    """
    cette boucle permet de faire afficher la possibilité des grilles à choisir
    """
    rectangle((n-1)*100, 0, n*100, 500,couleur='black', remplissage='green', epaisseur=5, tag='')
    texte(((n-1)*100+n*100)/2, 171.5, n, couleur='black', ancrage='nw', police='Helvetica', taille=40, tag='')

ev = attend_clic_gauche()


if (ev[0]<100):
    nom_grille = "niveau1.txt"
elif(ev[0]<200):
    nom_grille = "niveau2.txt"
elif(ev[0]<300):
    nom_grille = "niveau3.txt"
elif(ev[0]<400):
    nom_grille = "niveau4.txt"
else:
    nom_grille = "niveau5.txt"

fichier = open(nom_grille,'r').read()

fichier = fichier.split("\n")

efface_tout()
lire_grille(fichier)
efface_tout()
graph_grille(liste_de_liste)
menu()
mise_a_jour()


print(sans_conflit)
print(sans_voisines_noircies)





while (not(sans_voisines_noircies(liste_de_liste,cases_noircies)) or not(sans_conflit(liste_de_liste,cases_noircies))) or not connexe :


    (x,y) = attend_clic_gauche()

    if(399<x<539 and 40<y<80):	#Le bouton Quitter

        ferme_fenetre()

    elif(399<x<539 and 110<y<150):	#Le bouton Recommencer

        efface_tout()
        liste_de_liste =[]
        cases_noircies =[]
        lire_grille(fichier)
        efface_tout()
        graph_grille(liste_de_liste)
        cases_noircies =[]
        menu()

    elif(399<x<539 and 180<y<220):	#Le bouton Autre Grille

        efface_tout()
        liste_de_liste =[]
        cases_noircies = []
        for n in range (1,6): 
            rectangle((n-1)*100, 0, n*100, 500,couleur='black', remplissage='green', epaisseur=5, tag='')
            texte(((n-1)*100+n*100)/2, 171.5, n, couleur='black', ancrage='nw', police='Helvetica', taille=40, tag='')

        ev = attend_clic_gauche()


        if (ev[0]<100):
            nom_grille = "Grille/niveau1.txt"
        elif(ev[0]<200):
            nom_grille = "Grille/niveau2.txt"
        elif(ev[0]<300):
            nom_grille = "Grille/niveau3.txt"
        elif(ev[0]<400):
            nom_grille = "Grille/niveau4.txt"
        else:
            nom_grille = "Grille/niveau5.txt"

        fichier = open(nom_grille,'r').read()

        fichier = fichier.split("\n")

        efface_tout()
        lire_grille(fichier)
        efface_tout()
        graph_grille(liste_de_liste)
        menu()
        mise_a_jour()


        

        mise_a_jour()
    
    elif(399<x<539 and 250<y<290):	#Le boutton Annuler
        
        annuler(cases_noircies)
        mise_a_jour()

    else:			#Le cas où on appuye sur une case

        ajout_cases_noircies(liste_de_liste,x,y)
        sans_voisines_noircies(liste_de_liste,cases_noircies)
        mise_a_jour()

    print("liste_de_liste")
    afficher_grille(liste_de_liste)



efface_tout()
victoire()
attend_fermeture()


