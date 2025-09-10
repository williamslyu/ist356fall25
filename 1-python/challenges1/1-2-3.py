
colors = []

while True:
    color = input("Enter a color (or 'quit' to stop): ").strip().lower()

    if color == "quit":
        break

    if color not in colors:
        colors.append(color)

    print("Current list of colors:", colors)

