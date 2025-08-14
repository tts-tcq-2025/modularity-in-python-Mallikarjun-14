from .constants import MAJOR_COLORS, MINOR_COLORS
from .color_utils import get_pair_number_from_color


def generate_reference_manual():
    """
    Returns a list of tuples mapping color pairs to their corresponding numbers.
    """
    manual_data = []
    for major in MAJOR_COLORS:
        for minor in MINOR_COLORS:
            pair_number = get_pair_number_from_color(major, minor)
            manual_data.append((pair_number, major, minor))
    return manual_data


def print_reference_manual():
    """
    Prints the reference manual in a readable table format.
    """
    print("25-Pair Color Code Reference Manual")
    print("=" * 45)
    print(f"{'Pair #':<8} {'Major Color':<10} {'Minor Color'}")
    print("-" * 45)
    for pair_number, major, minor in generate_reference_manual():
        print(f"{pair_number:<8} {major:<10} {minor}")
    print("=" * 45)
