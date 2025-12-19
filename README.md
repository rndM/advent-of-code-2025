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

  - Pour les jours codés en C, les Makefiles de chaque dossier créent un exécutable nommé `dayNN` (ex. `day01`).
  - Ajustez le nom de l'exécutable si nécessaire selon le `Makefile` du jour.

  ### Instructions Python

  Exemple pour les jours où la solution est en Python :

    ```bash
    cd 02
    python3 giftShop.py
    ```

  - **Notes** : 
    - Les scripts sont exécutables directement si les permissions sont définies.

## Notes

- Les solutions sont personnelles et ne sont pas nécessairement optimisées, l'Advent of Code est avant tout une activité ludique. 
- Certains jours pourront inclure des approches alternatives, des essais complémentaires... 

## Liens utiles

- [Site officiel Advent of Code 2025](https://adventofcode.com/2025)
- [École 42 Marseille](https://42marseille.com)

---

*Ce projet est maintenu dans le cadre de ma formation à l'École 42. Les énoncés et données d'input appartiennent à Advent of Code.*

---

# Advent of Code 2025 – École 42 Marseille

This repository contains my solutions to the [Advent of Code 2025](https://adventofcode.com/2025) problems, completed as part of my training at École 42 Marseille.

## Repository Structure

Each day contains:
- Solutions in C or Python (in a single `.c` file or with utility functions)

## Compilation and Execution

  ### C Instructions: 

- **Compile a day (from the day's folder)**

  ```bash
  cd 01
  make
  ```

- **Run the generated executable**

  ```bash
  ./01/day01           # executable created by the Makefile
  ```

- **Notes**

  - For days coded in C, the Makefiles in each folder create an executable named `dayNN` (e.g., `day01`).
  - Adjust the executable name if necessary according to the day's `Makefile`.

  ### Python Instructions

  Example for days where the solution is in Python:

    ```bash
    cd 02
    python3 giftShop.py
    ```

  - **Notes**:
    - Scripts are directly executable if permissions are set.

## Notes

- The solutions are personal and not necessarily optimized; Advent of Code is primarily a fun activity.
- Some days may include alternative approaches, additional experiments... 

## Useful Links

- [Official Advent of Code 2025 Site](https://adventofcode.com/2025)
- [École 42 Marseille](https://42marseille.com)

---

*This project is maintained as part of my training at École 42. The problem statements and input data belong to Advent of Code.*
