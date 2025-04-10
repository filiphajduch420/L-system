import math
import matplotlib.pyplot as plt
import os

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

def draw_lsystem(instructions, angle_deg, rules, iterations, output_dir, identifier):
    """Draws the L-system and saves the image with a specific identifier."""
    # Initial coordinates and angle
    x, y = 0.0, 0.0
    angle = 0.0

    # Stack for saving state
    stack = []

    # List of lines to draw
    lines = []

    # Character definitions for actions
    draw = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # Drawing
    move = "abcdefghijklmnopqrstuvwxyz"           # Move without drawing
    ignore = "VWXvwxYZyz"                         # Ignored characters

    for cmd in instructions:
        match cmd:
            case c if c in draw:
                x_new = x + math.cos(math.radians(angle))
                y_new = y + math.sin(math.radians(angle))
                lines.append(((x, y), (x_new, y_new)))
                x, y = x_new, y_new
            case c if c in move:
                x += math.cos(math.radians(angle))
                y += math.sin(math.radians(angle))
            case c if c in ignore:
                pass
            case "+":
                angle += angle_deg
            case "-":
                angle -= angle_deg
            case "|":
                angle += 180
            case "[":
                stack.append((x, y, angle))
            case "]":
                x, y, angle = stack.pop()
            case _:
                pass

    # Plot all lines
    for (x1, y1), (x2, y2) in lines:
        plt.plot([x1, x2], [y1, y2], color="black")

    # Add rules, angle, and iterations as text in the bottom-right corner
    rules_text = "\n".join([f"{key} → {value}" for key, value in rules.items()])
    info_text = f"Rules:\n{rules_text}\n\nAngle: {angle_deg}°\nIterations: {iterations}"
    plt.gcf().text(0.95, 0.05, info_text, ha="right", va="bottom", fontsize=8)

    # Configure axes and save the plot as an image
    plt.axis("equal")
    plt.axis("off")
    os.makedirs(output_dir, exist_ok=True)
    image_path = os.path.join(output_dir, f"{identifier}_iteration_{iterations}.png")
    plt.savefig(image_path, bbox_inches="tight", pad_inches=0.1)
    plt.close()

def process_lsystem(axiom, rules, angle, iterations, identifier):
    """Generates and saves the L-system images with a specific identifier."""
    output_dir = "img"
    for i in range(iterations + 1):
        # Generate the current L-system string
        current = generate_lsystem(axiom, rules, i)
        print(f"Iteration {i}: {current}")
        # Save the current L-system drawing as an image
        draw_lsystem(current, angle, rules, i, output_dir, identifier)