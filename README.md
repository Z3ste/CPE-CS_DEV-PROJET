
# :space_invader: Space invader Xplorer 

## Introduction

> **Attaque sur le système solaire**
> Une mysterieuse entitée attaque le système solaire et projette d'anéantir le genre humain. Vous êtes Hercule, un pilote de vaisseau spatial au service de la planête terre. Vous êtes missionné pour stopper cette invasion alien.

Explorez l'espace, détruisez les vaisseaux aliens et sauvez la galaxie !

![The San Juan Mountains are beautiful!](/image/Screenshot_2.png "Une partie de jeu")

## Les fonctionnalitées

Fonctionnalité | Check
---------|----------
 Plusieurs types d'aliens | :white_check_mark:
 Plusieurs niveaux | :white_check_mark:
 Les fonds changent selon les niveaux | :white_check_mark:
 Animation d'explosion lors du tire | :white_check_mark:
 Parametres du jeu éditablent | :white_check_mark:
 Menu d'acceuil stylé | :white_check_mark:
  Reviser les partiels | :x:

#### Personnaliser les parametres du jeu

Il vous suffit de modifier les variables dans le fichier **constants.py**.

## Trailer

![The San Juan Mountains are beautiful!](/image/space_invaders.gif "Une partie de jeu")

## Cahier des charges

### L'objectif

Le but de ce TP est de développer votre propre version du célèbre jeu de shoot them up sorti en 1978 : **space invaders** :alien:\. Le développement de ce jeu se fera avec une interface graphique construite à partir du
module **Tkinter**. Vous avez pour cela 3 séances de 4 heures :alarm_clock:\. Vous travaillerez en binômes et programmerez en orienté objet. La notation portera autant sur les bonnes pratiques que sur le résultat final\.

### Les contraintes

* Le jeu sera programmé en langage orienté objet
* Le jeu devra présenter une implémentation de liste, une de file et une de pile
* Le rendu se fera sous la forme d’une archive contenant l’ensemble de vos fichiers.
* Dans cette archive se trouvera un fichier readme indiquant les règles du jeu et les spécificités de votre
implémentation, l’adresse de votre répertoire GIT, et où se trouvent les implémentations des structures
de données demandées
* La notation prendra autant en compte le respect des consignes que le résultat final. 

### Pour aller plus loin

Améliorations possibles, dans cet ordre ou dans un autre :
* Augmenter la vitesse des Aliens lorsqu’ils sont moins nombreux\.
* Gérer le passage de la soucoupe
* Créer plusieurs niveaux à votre jeu
* Ajouter une image de fond (différente pour chaque niveau)
* Gestion des meilleurs scores (avec inscription dans un fichier texte)
* Permettre à l’utilisateur de changer les touches de contrôle
* Mettre des cheat codes afin de gagner des vies supplémentaires
* Laisser parler votre imagination et n’hésitez pas à demander conseil à vos ainés qui auraient perdu un temps précieux à jouer à ce jeu !

### Respect des contraintes

#### Programmation orienté objet

Toutes les entités sont des objets.

#### La pile

La pile a été implementé au niveau de la gestion des threads engendré par les afters. Ils sont ajoutés avec _append_ et supprimés avec _pop_.

```
self.thread.append(self.area.after(500, self.refresh_img))
```

```
        while len(self.thread) != 0:
            print("[-] Closing threads...")
            thread = self.thread.pop(-1)
            self.area.after_cancel(thread)
        print("[-] All threads are closed")
``` 

#### La file

Nous n'avons pas trouvé d'implémentation d'une structure de donnée de type file... :disappointed:

## Auteur

Rami et Eliot, deux étudiants de CPE Lyon dans le cadre du projet de fin de module "python".

## Bugs

* Si les gif ont un fond noir, upgrader le module pillow ([issue ici](https://github.com/python-pillow/Pillow/issues/5755)).
* Le jeu met un peu de temps à se lancer, c'est normal.