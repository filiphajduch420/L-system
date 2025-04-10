import math
import matplotlib.pyplot as plt

def generate_lsystem(axiom, rules, iterations):
    """Generuje řetězec L-systému po zadaném počtu iterací."""
    result = axiom
    for _ in range(iterations):
        next_result = ""
        for symbol in result:
            # Nahraď symbol podle pravidel, nebo ponech původní
            next_result += rules.get(symbol, symbol)
        result = next_result
    return result

def draw_lsystem(instructions, angle_deg):
    """Interpretuje instrukce L-systému pomocí jednoduché turtle grafiky."""
    # Počáteční souřadnice a úhel
    x, y = 0.0, 0.0
    angle = 0.0

    # Zásobník pro ukládání stavu
    stack = []

    # Seznam čar pro vykreslení
    lines = []

    # Definice znaků pro různé akce
    draw = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # Kreslení
    move = "abcdefghijklmnopqrstuvwxyz"           # Pohyb bez kreslení
    ignore = "VWXvwxYZyz"                         # Ignorované znaky

    for cmd in instructions:
        match cmd:
            # Nakresli úsečku
            case c if c in draw:
                x_new = x + math.cos(math.radians(angle))
                y_new = y + math.sin(math.radians(angle))
                lines.append(((x, y), (x_new, y_new)))
                x, y = x_new, y_new

            # Pohni se vpřed bez kreslení
            case c if c in move:
                x += math.cos(math.radians(angle))
                y += math.sin(math.radians(angle))

            # Nedělej nic
            case c if c in ignore:
                pass

            # Otoč se doleva
            case "+":
                angle += angle_deg

            # Otoč se doprava
            case "-":
                angle -= angle_deg

            # Otoč se čelem vzad
            case "|":
                angle += 180

            # Ulož stav
            case "[":
                stack.append((x, y, angle))

            # Obnov stav
            case "]":
                x, y, angle = stack.pop()

            # Výchozí – ignoruj neznámé znaky
            case _:
                pass

    # Vykresli všechny čáry
    for (x1, y1), (x2, y2) in lines:
        plt.plot([x1, x2], [y1, y2], color="black")

    # Nastavení os a zobrazení grafu
    plt.axis("equal")
    plt.axis("off")
    plt.show()

def process_lsystem(axiom, rules, angle, iterations):
    """Generuje a vykresluje L-systém."""
    for i in range(iterations + 1):
        # Generování aktuálního řetězce L-systému
        current = generate_lsystem(axiom, rules, i)
        print(f"Iterace {i}: {current}")
        # Vykreslení aktuálního stavu L-systému
        draw_lsystem(current, angle)