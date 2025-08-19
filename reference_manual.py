# reference_manual
from mapping import get_color_from_pair_number
from constants import TOTAL_PAIRS

def generate_reference_manual():
    """
    Generate a formatted string mapping pair numbers to color names.
    This can be printed or written to a file for field reference.
    """
    lines = []
    header = f"{'Pair Number':<12} {'Major Color':<12} {'Minor Color':<12}"
    lines.append(header)
    lines.append("-" * len(header))

    for pair_number in range(1, TOTAL_PAIRS + 1):
        major_color, minor_color = get_color_from_pair_number(pair_number)
        lines.append(f"{pair_number:<12} {major_color:<12} {minor_color:<12}")

    return "\n".join(lines)
