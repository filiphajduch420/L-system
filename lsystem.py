import math
import matplotlib.pyplot as plt
import os

def generate_lsystem(axiom, rules, iterations):
    """
    Generuje řetězec L-systému po stanoveném počtu iterací.

    Args:
        axiom (str): Počáteční řetězec L-systému.
        rules (dict): Slovník produkčních pravidel pro L-systém.
        iterations (int): Počet iterací pro aplikaci pravidel.

    Returns:
        str: Výsledný řetězec L-systému po určených iteracích.
    """
    result = axiom
    for _ in range(iterations):
        next_result = ""
        for symbol in result:
            # Nahrazení symbolu podle pravidel nebo ponechání beze změny
            next_result += rules.get(symbol, symbol)
        result = next_result
    return result

def draw_lsystem(instructions, angle_deg, rules, iterations, output_dir, identifier):
    """
    Vykreslí L-systém na základě vygenerovaných instrukcí a uloží jej jako obrázek.

    Args:
        instructions (str): Řetězec L-systému, který bude interpretován pro kreslení.
        angle_deg (float): Úhel ve stupních pro otáčení.
        rules (dict): Produkční pravidla L-systému.
        iterations (int): Aktuální iterace L-systému.
        output_dir (str): Adresář, kam bude obrázek uložen.
        identifier (str): Jedinečný identifikátor pro pojmenování souboru obrázku.
    """
    # Počáteční souřadnice a úhel
    x, y = 0.0, 0.0
    angle = 0.0

    # Zásobník pro ukládání stavu (pozice a úhlu)
    stack = []

    # Seznam čar pro kreslení
    lines = []

    # Definice znaků pro akce
    draw = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # Znaky pro kreslení
    move = "abcdefghijklmnopqrstuvwxyz"           # Znaky pro přesun bez kreslení
    ignore = "VWXvwxYZyz"                         # Znaky k ignorování

    for cmd in instructions:
        match cmd:
            case c if c in draw:
                # Nakreslení čáry v aktuálním směru
                x_new = x + math.cos(math.radians(angle))
                y_new = y + math.sin(math.radians(angle))
                lines.append(((x, y), (x_new, y_new)))
                x, y = x_new, y_new
            case c if c in move:
                # Přesun bez kreslení
                x += math.cos(math.radians(angle))
                y += math.sin(math.radians(angle))
            case c if c in ignore:
                # Ignorování příkazu
                pass
            case "+":
                # Otočení doleva o určený úhel
                angle += angle_deg
            case "-":
                # Otočení doprava o určený úhel
                angle -= angle_deg
            case "|":
                # Otočení o 180 stupňů
                angle += 180
            case "[":
                # Uložení aktuálního stavu
                stack.append((x, y, angle))
            case "]":
                # Obnovení posledního uloženého stavu
                x, y, angle = stack.pop()
            case _:
                # Ignorování nerozpoznaných příkazů
                pass

    # Vykreslení všech čar
    for (x1, y1), (x2, y2) in lines:
        plt.plot([x1, x2], [y1, y2], color="black")

    # Přidání pravidel, úhlu a iterací jako text v pravém dolním rohu
    rules_text = "\n".join([f"{key} → {value}" for key, value in rules.items()])
    info_text = f"Pravidla:\n{rules_text}\n\nÚhel: {angle_deg}°\nIterace: {iterations}"
    plt.gcf().text(0.95, 0.05, info_text, ha="right", va="bottom", fontsize=8)

    # Konfigurace os a uložení diagramu jako obrázku
    plt.axis("equal")
    plt.axis("off")
    os.makedirs(output_dir, exist_ok=True)
    image_path = os.path.join(output_dir, f"{identifier}_iteration_{iterations}.png")
    plt.savefig(image_path, bbox_inches="tight", pad_inches=0.1)
    plt.close()

def Lsystem(axiom, rules, angle, iterations, identifier):
    """
    Generuje a ukládá obrázky pro každou iteraci L-systému.

    Args:
        axiom (str): Počáteční řetězec L-systému.
        rules (dict): Slovník produkčních pravidel pro L-systém.
        angle (float): Úhel ve stupních pro otáčení.
        iterations (int): Počet iterací k vygenerování.
        identifier (str): Jedinečný identifikátor pro pojmenování obrázků.
    """
    output_dir = "img"
    for i in range(iterations + 1):
        # Generování aktuálního řetězce L-systému
        current = generate_lsystem(axiom, rules, i)
        print(f"Iterace {i}: {current}")
        # Uložení aktuálního vykreslení L-systému jako obrázku
        draw_lsystem(current, angle, rules, i, output_dir, identifier)




# 3D L-Systém
def draw_lsystem_3d(instructions, angle_deg, rules, iterations, output_dir, identifier):
    """
    Vykreslí 3D L-systém na základě vygenerovaných instrukcí a uloží jej jako obrázek.

    Args:
        instructions (str): Řetězec L-systému, který bude interpretován pro kreslení.
        angle_deg (float): Úhel ve stupních pro otáčení.
        rules (dict): Produkční pravidla L-systému.
        iterations (int): Aktuální iterace L-systému.
        output_dir (str): Adresář, kam bude obrázek uložen.
        identifier (str): Jedinečný identifikátor pro pojmenování souboru obrázku.
    """
    # Počáteční souřadnice a úhly
    x, y, z = 0.0, 0.0, 0.0
    yaw, pitch, roll = 0.0, 0.0, 0.0

    # Zásobník pro ukládání stavu (pozice a orientace)
    stack = []

    # Seznam čar pro kreslení
    lines = []

    for cmd in instructions:
        match cmd:
            case "F":
                # Pohyb vpřed a kreslení čáry
                dx = math.cos(math.radians(yaw)) * math.cos(math.radians(pitch))
                dy = math.sin(math.radians(yaw)) * math.cos(math.radians(pitch))
                dz = math.sin(math.radians(pitch))
                x_new, y_new, z_new = x + dx, y + dy, z + dz
                lines.append(((x, y, z), (x_new, y_new, z_new)))
                x, y, z = x_new, y_new, z_new
            case "+":
                # Otočení doleva (yaw)
                yaw += angle_deg
            case "-":
                # Otočení doprava (yaw)
                yaw -= angle_deg
            case "&":
                # Naklonění dolů (pitch)
                pitch += angle_deg
            case "^":
                # Naklonění nahoru (pitch)
                pitch -= angle_deg
            case "\\":
                # Náklon doleva (roll)
                roll += angle_deg
            case "/":
                # Náklon doprava (roll)
                roll -= angle_deg
            case "[":
                # Uložení aktuálního stavu
                stack.append((x, y, z, yaw, pitch, roll))
            case "]":
                # Obnovení posledního uloženého stavu
                x, y, z, yaw, pitch, roll = stack.pop()

    # Vykreslení všech čar ve 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    for (x1, y1, z1), (x2, y2, z2) in lines:
        ax.plot([x1, x2], [y1, y2], [z1, z2], color="black")

    # Konfigurace os a uložení diagramu jako obrázku
    ax.axis("off")
    os.makedirs(output_dir, exist_ok=True)
    image_path = os.path.join(output_dir, f"{identifier}_iteration_{iterations}.png")
    plt.savefig(image_path, bbox_inches="tight", pad_inches=0.1)
    plt.close()

    model_path = os.path.join(output_dir, f"{identifier}_iteration_{iterations}.obj")
    save_lsystem_3d_model(lines, model_path)
    print(f"3D model uložen do {model_path}")

def save_lsystem_3d_model(lines, output_file):
    """
    Ukládá 3D L-systém jako 3D model ve formátu .obj.

    Args:
        lines (list): Seznam úseček, kde každá úsečka je dvojice bodů ((x1, y1, z1), (x2, y2, z2)).
        output_file (str): Cesta pro uložení souboru .obj.
    """
    vertices = []
    edges = []
    vertex_index = {}

    # Sběr jedinečných vrcholů a přiřazení indexů
    for (x1, y1, z1), (x2, y2, z2) in lines:
        for point in [(x1, y1, z1), (x2, y2, z2)]:
            if point not in vertex_index:
                vertex_index[point] = len(vertices) + 1
                vertices.append(point)
        edges.append((vertex_index[(x1, y1, z1)], vertex_index[(x2, y2, z2)]))

    # Zápis do souboru .obj
    with open(output_file, "w") as f:
        # Zápis vrcholů
        for x, y, z in vertices:
            f.write(f"v {x} {y} {z}\n")
        # Zápis hran jako čar
        for v1, v2 in edges:
            f.write(f"l {v1} {v2}\n")

def Lsystem3D(axiom, rules, angle, iterations, identifier):
    """
    Generuje a ukládá konečný 3D obrázek a model pro L-systém.

    Args:
        axiom (str): Počáteční řetězec L-systému.
        rules (dict): Slovník produkčních pravidel pro L-systém.
        angle (float): Úhel ve stupních pro otáčení.
        iterations (int): Počet iterací k vygenerování.
        identifier (str): Jedinečný identifikátor pro pojmenování konečného obrázku a modelu.
    """
    output_dir = "img"
    # Generování konečného řetězce L-systému
    final = generate_lsystem(axiom, rules, iterations)
    print(f"Konečná iterace {iterations}: {final}")
    # Uložení pouze konečného vykreslení L-systému jako 3D obrázku a modelu
    draw_lsystem_3d(final, angle, rules, iterations, output_dir, identifier)