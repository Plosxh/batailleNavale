 !! La version final du jeu se trouve dans la branche "jeu" !!

Grille Taille variable ( env 2 tests ) cas normale, cas limite
Placer n'importe quel bâteau sur la grille. test bâteaux implaçable/grille pleine etc...
Lancer missiles (x,y)
2 Joueurs

Contrainte potentielles :

Grille : ajout îles
Bâteaux : contraintes bâteaux
Missiles : Rayon etc...

############################

Remarques générales :
il faudrait ajouter un .gitignore pour éviter d'avoir "__pycache__" qui encombre le dépôt
Il faut faire réduire la complexité de vos tests unitaires, et en faire beaucoup plus !
Attention à la casse et à la nomenclature en général, il faut en fixer une au début du projet et s'y tenir (cela vaut aussi pour les noms de fichiers)
Préférer "import A" à "from A import *" quand il y en a beaucoup à faire, le code est ainsi plus long mais plus facilement compréhensible
Si je ne m'abuse, votre structure de classes ne permet pas, à partir de l'objet Jeu, de toucher un bateau à partir de ses coordonnées ( exemple : je tire en (3,4) ), ce qui vous posera des problèmes si vous voulez implémenter une partie complète.

Bon point cependant : vous utilisez bien les fonctionnalités Python (modules, exceptions) et les principes d'encapsulation.