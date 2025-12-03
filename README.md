# Advent of Code 2025 – École 42 Marseille

Ce dépôt contient mes solutions aux problèmes de l'[Advent of Code 2025](https://adventofcode.com/2025), réalisées dans le cadre de ma formation à l'École 42 Marseille.

## Structure du dépôt

Chaque jour contient :
- Les solutions en C ou en Python (dans un seul fichier `.c` ou avec des fonctions utilitaires)

## Compilation et exécution

  ### Instructions en C :

- **Compiler un jour (depuis le dossier du jour)**

  ```bash
  cd 01
  make
  ```

- **Exécuter l'exécutable généré**

  ```bash
  ./01/day01           # exécutable créé par le Makefile
  ```

- **Remarques**

  - Pour les jous codés en C, les Makefiles de chaque dossier créent un exécutable nommé `dayNN` (ex. `day01`).
  - Ajustez le nom de l'exécutable si nécessaire selon le `Makefile` du jour.

  ### Instructions Python

  Pour les jours où la solution est en Python :

    ```bash
    cd 02
    python3 ids.py
    ```

  - **Notes** :
    - Les scripts sont exécutables directement si les permissions sont définies.

## Notes

- Les solutions sont personnelles et ne sont pas nécessairement optimisées, l'Advent of Code est avant tout une activité ludique.
- Certains jours pourront inclure des approches alternatives, des essais complémentaire ...

## Liens utiles

- [Site officiel Advent of Code 2025](https://adventofcode.com/2025)
- [École 42 Marseille](https://42marseille.com)

---

*Ce projet est maintenu dans le cadre de ma formation à l'École 42. Les énoncés et données d'input appartiennent à Advent of Code.*
