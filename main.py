# -------------------------
# MAPPINGS
# -------------------------
MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ['Blue', 'Orange', 'Green', 'Brown', 'Slate']


# -------------------------
# TRANSLATION FUNCTIONS
# -------------------------
def color_pair_to_string(major_color, minor_color):
    return f"{major_color} {minor_color}"


def get_color_from_pair_number(pair_number):
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    if major_index >= len(MAJOR_COLORS):
        raise Exception("Major index out of range")

    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    if minor_index >= len(MINOR_COLORS):
        raise Exception("Minor index out of range")

    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]


def get_pair_number_from_color(major_color, minor_color):
    try:
        major_index = MAJOR_COLORS.index(major_color)
    except ValueError:
        raise Exception("Major index out of range")

    try:
        minor_index = MINOR_COLORS.index(minor_color)
    except ValueError:
        raise Exception("Minor index out of range")

    return major_index * len(MINOR_COLORS) + minor_index + 1


# -------------------------
# MANUAL GENERATOR
# -------------------------
def generate_color_coding_manual():
    """Return a formatted string reference manual of color codes."""
    manual_lines = ["Color Coding Reference Manual", "-" * 40]
    pair_number = 1

    for major in MAJOR_COLORS:
        for minor in MINOR_COLORS:
            manual_lines.append(
                f"{pair_number:2d}: {major:<10} - {minor}"
            )
            pair_number += 1

    return "\n".join(manual_lines)


# -------------------------
# TESTS
# -------------------------
def test_number_to_pair():
    major, minor = get_color_from_pair_number(1)
    assert major == "White" and minor == "Blue"

    major, minor = get_color_from_pair_number(10)
    assert major == "Red" and minor == "Slate"


def test_pair_to_number():
    pair_number = get_pair_number_from_color("Black", "Green")
    assert pair_number == 13

    pair_number = get_pair_number_from_color("Yellow", "Brown")
    assert pair_number == 19


# -------------------------
# MAIN EXECUTION
# -------------------------
def main():
    print("Example lookups:")
    print("Pair 4 corresponds to:", get_color_from_pair_number(4))
    print("Color (Red, Slate) corresponds to pair:", get_pair_number_from_color("Red", "Slate"))

    print("\n" + generate_color_coding_manual())


if __name__ == "__main__":
    # Run tests
    test_number_to_pair()
    test_pair_to_number()

    # Run program
    main()

  



