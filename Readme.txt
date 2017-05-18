-----------KMEAN---------
descripteur utilisé: histogramme couleurs
paramètres du programme:
1-nombre de niveau pour l'échantillonage
2-nombre de cluster
résultat: la liste d'image de la base d'image avec le cluster associé
commande:./kmean 8 3
----------KNNGLOBAL------------
descripteurs utilisés: histogramme couleur et moment de Hu
paramètres du programme:
1- nom de l'image à classer
2- nombre de niveau pour l'échantillonage
3- nombre de voisins
4- le poids entre 0 et 1
commande: ./knnglobal obj1__10.png  8 10
résultat: la liste des k plus proches voisins ainsi que la distance par rapport à l'image
passée en entrée
----------KNNHU-----------
descripteurs utilisés:  moments de Hu d'ordre 8
paramètres du programme:
1-nom de l'image à classer
2- nombre de voisins

commande: ./knnhu obj2__10.png 10
résultat: la liste des k plus proches voisins ainsi que la distance par rapport à l'image
passée en entrée

----------KNN-----------
descripteurs utilisés:  histogramme couleur
paramètres du programme:
1-nom de l'image à classer
2- nombre de niveaux pour l'échantillonage
3- nombre de voisins

commande: ./knn obj1__10.png  8 10
résultat: la liste des k plus proches voisins ainsi que la distance par rapport à l'image
passée en entrée
----------knnlearn----------
descripteurs utilisés:  histogramme couleur
ce programme utilise une base d'apprentissage et effectue les tests sur tous
les éléments de la base test en utilisant l'algorithme knn. Puis une 
statistique est effectuée au fur et à mesure de l'évaluation des éléments
de la base test pour calculer le rappel et la précision
paramètres du programme:

1- nombre de niveaux pour l'échantillonage
2- nombre de voisins
commande: ./knnlearn 8 3
sortie: calcul du rappel et de la précision pour toutes les classes d'objets
