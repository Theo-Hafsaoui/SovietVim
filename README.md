# SovietVim
```   / ____|          (_)    | \ \    / (_)                      -. .
  | (___   _____   ___  ___| |\ \  / / _ _ __ ___          _____   ',' ,
   \___ \ / _ \ \ / / |/ _ \ __\ \/ / | | '_ ` _ \      ,'     ,'   ', ',
   ____) | (_) \ V /| |  __/ |_ \  /  | | | | | | |   ,'     ,'      |  |
  |_____/ \___/ \_/ |_|\___|\__| \/   |_|_| |_| |_|  \       \       |  |
                               INFO    TOULON          \ /^\   \    ,' ,'
                                                             \   \ ,' ,'
                                                       / ~-.___\.-'  ,'
                                                     /   .______.- ~ \
                                                   /   /'          \   \
                                                   \./               \/'
                                                   
```

## Introduction
La cellule du KGB, comme vous le savez maintenant, est spécialisée dans l'infiltration informatique, le hacking, et la filouterie de réseaux. Suite à de nombreuses escarmouches de nos camarades, une vulnérabilité au sein du réseau de la NSA a été mise en évidence. Malheureusement, beaucoup des failles ont été résolues. Néanmoins, heureusement pour nous, une brèche existe encore sur le fichier `brake_liability`. Nous le savons : depuis ce fichier, un chemin de lien existe. Utilisez-le pour arriver à l'objectif `trace_et` et décoder le code secret du camarade (décédé) infiltré.

Il y a cependant une contrainte : un outil trop développé attirerait l'attention. Aussi, pour réussir, vous devrez utiliser le puissant outil VIM. Ne vous en faites pas, camarade, vous trouverez toutes les informations nécessaires plus bas. Bonne chance, camarade.

## Contraintes :
- Maximum de 30 commandes.
- Mouvement limité par commande, à vous de découvrir la joie de le découvrir !
- Limité aux commandes ci-dessous.

## Opérateurs de mouvement
- `hjkl` : Ce sont les opérateurs de mouvement classique, on peut les comparer aux flèches du clavier.
- `f[c]` : `f` pour forward, se téléporte directement à la prochaine occurrence du caract��re.
- `gg` : Va en haut du document.
- `G` : Va en bas du document.
- `gf` : Va vers le lien sur le curseur.

## Opérateurs d'édition
- `dd` : Supprime la ligne.
- `x` : Supprime le caractère sous le curseur.
- `$` : Pour la fin de la ligne.
- `0` : Pour le début de la ligne.
- `{` et `}` : Pour se déplacer d'un paragraphe à l'autre.

Pour d'autres commandes, utiliser `:help` pour plus d'informations. Exemple : `:help g?`

## Vim, un langage
Vim et sa syntaxe se rapprochent d'un langage. En effet, si parfois certaines commandes semblent presque cryptiques, d'autres possèdent une clarté presque surréelle. Prenons par exemple l'opérateur de mouvement `i` pour "inside". Maintenant, devinez cette commande : `di(`. Ici, `d` pour delete, `i` pour inside, et `(` pour... parenthèse. Une fois réunis, on obtient "delete inside parenthèses", ce que fait exactement cette commande. Ce n'est pas une coïncidence, c'est la manière dont Vim a été conçu. On peut par exemple ajouter à notre vocabulaire `c` pour "change", et on obtient "change inside parenthèses". Plus notre vocabulaire s'enrichit, plus notre capacité d'édition devient puissante.
