import lsystem
import gifmaker

if __name__ == "__main__":
    # Define the L-system parameters
    axiom = "F"
    rules = {
        "F": "F+F-F-F+F",
        "+": "+",
        "-": "-"
    }
    angle = 90
    iterations = 4
    identifier = "example_lsystem"  # Unique identifier for this L-system

    # Generate and save the L-system images
    lsystem.process_lsystem(axiom, rules, angle, iterations, identifier)
    gifmaker.create_gif_from_images("img", "gif/lsystem.gif", identifier, duration=500)