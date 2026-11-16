
from parameters import (
    WAVELENGTH,
    D,
    N
)

from plotting import plot_pattern

from direction import direction




def main():

    # Display project parameters
    print(f"Wavelength = {WAVELENGTH:.4f} m")
    print(f"Spacing = {D:.4f} m")
    print(f"Number of elements = {N}")

    # Plot beam steering patterns
    print("\nGenerating beam steering plots...")

    plot_pattern()

    # Validate beam direction
    direction()

if __name__ == "__main__":
    main()