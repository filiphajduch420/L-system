import lsystem

if __name__ == "__main__":
    axiom = "F"
    rules = {
        "F": "F[+F]F[-F]F"
    }
    angle = 25
    iterations = 3

    lsystem.process_lsystem(axiom, rules, angle, iterations)