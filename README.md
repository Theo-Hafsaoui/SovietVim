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
## intro
La cellule du kgb comme vous le savez maintenant a pour specialiter l'infiltration informatique, le hacking, la filouterie de reseaux.
Suite a de nombreuse escarmouche de nos kamarad une vulnerabilie dur reseaux de la nsa a etait mis en evidence 
malheureusement beaucoup des faille ont etait resolut, neamons et heuresuement pour nous une breche 
existe encore sur le fichier brake_liability nous le savons depuis ce fichier un chemin de lien existe utuliser le 
pour arriver a l'objetif trace_et et decoder le code secret du kamarad (deceder) infiltrer.
Il y a cependant une contraint un outils trop developer attirer l'attention aussi pour reussir vous
devrez utuliser le puissant outils VIM, ne vous en faite pas kamarade vous trouverez toute les information
necessaire plus bas, bonne chance kamarad.

## Contrainte:
  max 30 commande
  mouvement limiter par commande, a vous la joie de le decouvrir !
  et limiter au commande ci deesous

## operateur de mouvement
<ul>
  <li>hjkl:se sont les operateur de mouvement classique on peut les comparer au fleche du clavier
  <li>f[c] f pour forward se tp directement a l aprochine ocurence du chararctere
  <li>gg va en haut du document
  <li>G va en bas du document
  <li>gf va vers le lien sur le curseur
  <li>operateur d'edition
  <li>dd  supprime la ligne
  <li>x supprime le chractere sous le curseur
  <li>$ pour la fin de la ligne
  <li>0 pour le debut de la ligne
  <li>{ et } pour se deplacer d'un paragraphe a l'autre
</ul>
Il y a d'autre commande qui se devine pour des info utuliser help  exemple: ":help g?"

## vim un langage
  vim est sa syntax se rapproche d'un lanage en effet si parafois certaine command son presque cryptique
  d'autre sont clarte presque surelle pour notre exemple prenons l'operateur de mouvemt i pour inside
  maintenat deviner cette commande di(... ici c'est d pour delete i pour inside et ) pour... parenthese une
  fois reunis ontobtient delete inside parenthese ce que fais exactement cette commande d'ailleur ce n'est
  pas une coincidence c'est la maniere dont est realiser vim on peut par exemple rajouter a notre vocabulair 
  c pour change et on obtien change inside parenthese plus notre vocabulair s'enrichie plus notre capacite d'edition
  deviens puissante
