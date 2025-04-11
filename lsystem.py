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




# 3D L-System
def draw_lsystem_3d(instructions, angle_deg, rules, iterations, output_dir, identifier):
    """
    Draws the 3D L-system based on the generated instructions and saves it as an image.

    Args:
        instructions (str): The L-system string to be interpreted for drawing.
        angle_deg (float): The angle in degrees for turning.
        rules (dict): The production rules of the L-system.
        iterations (int): The current iteration of the L-system.
        output_dir (str): The directory where the image will be saved.
        identifier (str): A unique identifier for naming the image file.
    """
    # Initial coordinates and angles
    x, y, z = 0.0, 0.0, 0.0
    yaw, pitch, roll = 0.0, 0.0, 0.0

    # Stack for saving the state (position and orientation)
    stack = []

    # List of lines to draw
    lines = []

    for cmd in instructions:
        match cmd:
            case "F":
                # Move forward and draw a line
                dx = math.cos(math.radians(yaw)) * math.cos(math.radians(pitch))
                dy = math.sin(math.radians(yaw)) * math.cos(math.radians(pitch))
                dz = math.sin(math.radians(pitch))
                x_new, y_new, z_new = x + dx, y + dy, z + dz
                lines.append(((x, y, z), (x_new, y_new, z_new)))
                x, y, z = x_new, y_new, z_new
            case "+":
                # Turn left (yaw)
                yaw += angle_deg
            case "-":
                # Turn right (yaw)
                yaw -= angle_deg
            case "&":
                # Pitch down
                pitch += angle_deg
            case "^":
                # Pitch up
                pitch -= angle_deg
            case "\\":
                # Roll left
                roll += angle_deg
            case "/":
                # Roll right
                roll -= angle_deg
            case "[":
                # Save the current state
                stack.append((x, y, z, yaw, pitch, roll))
            case "]":
                # Restore the last saved state
                x, y, z, yaw, pitch, roll = stack.pop()

    # Plot all lines in 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    for (x1, y1, z1), (x2, y2, z2) in lines:
        ax.plot([x1, x2], [y1, y2], [z1, z2], color="black")

    # Configure axes and save the plot as an image
    ax.axis("off")
    os.makedirs(output_dir, exist_ok=True)
    image_path = os.path.join(output_dir, f"{identifier}_iteration_{iterations}.png")
    plt.savefig(image_path, bbox_inches="tight", pad_inches=0.1)
    plt.close()

    model_path = os.path.join(output_dir, f"{identifier}_iteration_{iterations}.obj")
    save_lsystem_3d_model(lines, model_path)
    print(f"3D model saved to {model_path}")

def save_lsystem_3d_model(lines, output_file):
    """
    Saves the 3D L-system as a 3D model in .obj format.

    Args:
        lines (list): A list of line segments, where each segment is a tuple of two points ((x1, y1, z1), (x2, y2, z2)).
        output_file (str): The path to save the .obj file.
    """
    vertices = []
    edges = []
    vertex_index = {}

    # Collect unique vertices and assign indices
    for (x1, y1, z1), (x2, y2, z2) in lines:
        for point in [(x1, y1, z1), (x2, y2, z2)]:
            if point not in vertex_index:
                vertex_index[point] = len(vertices) + 1
                vertices.append(point)
        edges.append((vertex_index[(x1, y1, z1)], vertex_index[(x2, y2, z2)]))

    # Write to .obj file
    with open(output_file, "w") as f:
        # Write vertices
        for x, y, z in vertices:
            f.write(f"v {x} {y} {z}\n")
        # Write edges as lines
        for v1, v2 in edges:
            f.write(f"l {v1} {v2}\n")

def Lsystem3D(axiom, rules, angle, iterations, identifier):
    """
    Generates and saves the final 3D image and model for the L-system.

    Args:
        axiom (str): The initial string of the L-system.
        rules (dict): A dictionary of production rules for the L-system.
        angle (float): The angle in degrees for turning.
        iterations (int): The number of iterations to generate.
        identifier (str): A unique identifier for naming the final image and model.
    """
    output_dir = "img"
    # Generate the final L-system string
    final = generate_lsystem(axiom, rules, iterations)
    print(f"Final Iteration {iterations}: {final}")
    # Save only the final L-system drawing as a 3D image and model
    draw_lsystem_3d(final, angle, rules, iterations, output_dir, identifier)
