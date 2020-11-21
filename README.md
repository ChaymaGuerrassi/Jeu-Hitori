# Jeu-Hitori
Jeu japonais Hitori codé en Python.

Règles et but du jeu
Sur certains aspects le jeu peut rappeler le Sudoku (grilles, chiffre unique en ligne et en colonne). La
résolution d'une grille se fait par la "coloration" de certaines de certaines cellules qui sont soumise à 3 conditions :
- il ne doit y avoir qu'un seul chiffre identique et non coloré sur une même ligne et une même colonne
- il ne peut y avoir 2 cellules colorées côte à côte (mais elles peuvent se toucher par leur diagonale),
- L’ensemble des cellules visibles doit être d’un seul tenant (il ne peut pas y avoir deux zones visibles
distinctes non reliées entre elles)
 
Afin de mener à bien notre projet, nous avons analysé les besoins en matière de fonctions et de stockage de
données. Pour les données de base, le choix de liste (type : lst) semblait le plus approprié pour notre projet
pour la facilité de stockage de données dans des cases.

L'implementation d'un solveur avec un algorithme de Backtracking est bien avancée mais pas vraiment aboutie.
