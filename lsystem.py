import math
import matplotlib.pyplot as plt
import os

def generate_lsystem(axiom, rules, iterations):
    """
    Generates the L-system string after a specified number of iterations.

    Args:
        axiom (str): The initial string of the L-system.
        rules (dict): A dictionary of production rules for the L-system.
        iterations (int): The number of iterations to apply the rules.

    Returns:
        str: The resulting L-system string after the specified iterations.
    """
    result = axiom
    for _ in range(iterations):
        next_result = ""
        for symbol in result:
            # Replace the symbol based on the rules or keep it unchanged
            next_result += rules.get(symbol, symbol)
        result = next_result
    return result

def draw_lsystem(instructions, angle_deg, rules, iterations, output_dir, identifier):
    """
    Draws the L-system based on the generated instructions and saves it as an image.

    Args:
        instructions (str): The L-system string to be interpreted for drawing.
        angle_deg (float): The angle in degrees for turning.
        rules (dict): The production rules of the L-system.
        iterations (int): The current iteration of the L-system.
        output_dir (str): The directory where the image will be saved.
        identifier (str): A unique identifier for naming the image file.
    """
    # Initial coordinates and angle
    x, y = 0.0, 0.0
    angle = 0.0

    # Stack for saving the state (position and angle)
    stack = []

    # List of lines to draw
    lines = []

    # Character definitions for actions
    draw = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # Characters for drawing
    move = "abcdefghijklmnopqrstuvwxyz"           # Characters for moving without drawing
    ignore = "VWXvwxYZyz"                         # Characters to ignore

    for cmd in instructions:
        match cmd:
            case c if c in draw:
                # Draw a line in the current direction
                x_new = x + math.cos(math.radians(angle))
                y_new = y + math.sin(math.radians(angle))
                lines.append(((x, y), (x_new, y_new)))
                x, y = x_new, y_new
            case c if c in move:
                # Move without drawing
                x += math.cos(math.radians(angle))
                y += math.sin(math.radians(angle))
            case c if c in ignore:
                # Ignore the command
                pass
            case "+":
                # Turn left by the specified angle
                angle += angle_deg
            case "-":
                # Turn right by the specified angle
                angle -= angle_deg
            case "|":
                # Reverse direction (180-degree turn)
                angle += 180
            case "[":
                # Save the current state
                stack.append((x, y, angle))
            case "]":
                # Restore the last saved state
                x, y, angle = stack.pop()
            case _:
                # Ignore unrecognized commands
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

def Lsystem(axiom, rules, angle, iterations, identifier):
    """
    Generates and saves images for each iteration of the L-system.

    Args:
        axiom (str): The initial string of the L-system.
        rules (dict): A dictionary of production rules for the L-system.
        angle (float): The angle in degrees for turning.
        iterations (int): The number of iterations to generate.
        identifier (str): A unique identifier for naming the images.
    """
    output_dir = "img"
    for i in range(iterations + 1):
        # Generate the current L-system string
        current = generate_lsystem(axiom, rules, i)
        print(f"Iteration {i}: {current}")
        # Save the current L-system drawing as an image
        draw_lsystem(current, angle, rules, i, output_dir, identifier)