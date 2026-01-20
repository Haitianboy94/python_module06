import alchemy

if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print(f"Testing: {alchemy.elements.create_water()}")
    print(f"testing: {alchemy.elements.create_fire()}")
    print(f"testing: {alchemy.elements.create_earth()}")
    print(f"testing: {alchemy.elements.create_air()}")
    print()
    print("Testing package-level access (controlled by __init__.py):")
    try:
        print(f"Testing: {alchemy.create_water()}")
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print(f"Testing: {alchemy.create_fire()}")
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print(f"Testing: {alchemy.create_earth()}")
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print(f"Testing: {alchemy.create_air()}")
    except AttributeError:
        print("AttributeError - not exposed")
    print()
    print("Package metadata")
    print(f"Version: {alchemy.__version__}")
    print(f"Autor: {alchemy.__autor__}")
