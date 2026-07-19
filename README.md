# Advent of Code 2025 – École 42 Marseille

---

## 📚 Navigation

**[English Version](README.md)** | **[Version Française](README_FR.md)**

---

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
