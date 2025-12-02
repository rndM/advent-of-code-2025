def main():

    with open('input.txt', 'r') as f:
        contenu = f.read().strip()

    print(f"{contenu}")

    ranges = contenu.split(',')
    print(f"\n nb de lignes: {len(ranges)}")

    print("\nDetail des lignes:")
    for i, r in enumerate(ranges):
        print(f"  ligne {i+1}: '{r}'")

if __name__ == "__main__":
    main()
