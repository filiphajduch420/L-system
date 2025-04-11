import lsystem
import gifmaker

if __name__ == "__main__":
    # Koch Curve
    axiom_koch = "F"
    rules_koch = {
        "F": "F+F-F-F+F"
    }
    angle_koch = 90
    iterations_koch = 4
    identifier_koch = "koch_curve"
    lsystem.Lsystem(axiom_koch, rules_koch, angle_koch, iterations_koch, identifier_koch)
    gifmaker.create_gif_from_images("img", f"gif/{identifier_koch}.gif", identifier_koch, duration=500)

    # Sierpiński Triangle
    axiom_sierpinski = "F-G-G"
    rules_sierpinski = {
        "F": "F-G+F+G-F",
        "G": "GG"
    }
    angle_sierpinski = 120
    iterations_sierpinski = 5
    identifier_sierpinski = "sierpinski_triangle"
    lsystem.Lsystem(axiom_sierpinski, rules_sierpinski, angle_sierpinski, iterations_sierpinski, identifier_sierpinski)
    gifmaker.create_gif_from_images("img", f"gif/{identifier_sierpinski}.gif", identifier_sierpinski, duration=500)

    # Dragon Curve
    axiom_dragon = "FX"
    rules_dragon = {
        "X": "X+YF+",
        "Y": "-FX-Y"
    }
    angle_dragon = 90
    iterations_dragon = 10
    identifier_dragon = "dragon_curve"
    lsystem.Lsystem(axiom_dragon, rules_dragon, angle_dragon, iterations_dragon, identifier_dragon)
    gifmaker.create_gif_from_images("img", f"gif/{identifier_dragon}.gif", identifier_dragon, duration=500)

    # Define the L-System for "FILIP"
    axiom_filip = "FILIP"
    rules_filip = {
        "F": "F+F",
        "I": "I-I",
        "L": "L+L",
        "P": "P-F"
    }
    angle_filip = 30
    iterations_filip = 11
    identifier_filip = "filip_lsystem"
    lsystem.Lsystem(axiom_filip, rules_filip, angle_filip, iterations_filip, identifier_filip)
    gifmaker.create_gif_from_images("img", f"gif/{identifier_filip}.gif", identifier_filip, duration=500)

    # Define the L-System for "3D L-System"
    # 3D Tree Example
    axiom_tree = "F"
    rules_tree = {
        "F": "F[+F][-F]&F^F"
    }
    angle_tree = 25  # Angle for branching
    iterations_tree = 5  # Number of iterations
    identifier_tree = "3d_tree"

    # Generate and save the 3D tree
    lsystem.Lsystem3D(axiom_tree, rules_tree, angle_tree, iterations_tree, identifier_tree)
