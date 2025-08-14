
#!/bin/bash
# Create folder
mkdir -p color_coding

# constants.py
cat > color_coding/constants.py << 'EOF'
MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]
EOF

# color_utils.py
cat > color_coding/color_utils.py << 'EOF'
from .constants import MAJOR_COLORS, MINOR_COLORS


def color_pair_to_string(major_color, minor_color):
    return f"{major_color} {minor_color}"


def get_color_from_pair_number(pair_number):
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    if major_index >= len(MAJOR_COLORS):
        raise ValueError("Major index out of range")

    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    if minor_index >= len(MINOR_COLORS):
        raise ValueError("Minor index out of range")

    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]


def get_pair_number_from_color(major_color, minor_color):
    try:
        major_index = MAJOR_COLORS.index(major_color)
    except ValueError:
        raise ValueError("Major index out of range")

    try:
        minor_index = MINOR_COLORS.index(minor_color)
    except ValueError:
        raise ValueError("Minor index out of range")

    return major_index * len(MINOR_COLORS) + minor_index + 1
EOF

# printer.py
cat > color_coding/printer.py << 'EOF'
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
EOF

# tests.py
cat > color_coding/tests.py << 'EOF'
from .color_utils import get_color_from_pair_number, get_pair_number_from_color


def test_number_to_pair(pair_number, expected_major_color, expected_minor_color):
    major_color, minor_color = get_color_from_pair_number(pair_number)
    assert major_color == expected_major_color
    assert minor_color == expected_minor_color


def test_pair_to_number(major_color, minor_color, expected_pair_number):
    pair_number = get_pair_number_from_color(major_color, minor_color)
    assert pair_number == expected_pair_number


def run_tests():
    test_number_to_pair(4, "White", "Brown")
    test_number_to_pair(5, "White", "Slate")
    test_pair_to_number("Black", "Orange", 12)
    test_pair_to_number("Violet", "Slate", 25)
    test_pair_to_number("Red", "Orange", 7)
    print("All tests passed.")
EOF

# main.py
cat > color_coding/main.py << 'EOF'
from .tests import run_tests
from .printer import print_reference_manual


if __name__ == "__main__":
    run_tests()
    print_reference_manual()
EOF

# __init__.py
touch color_coding/__init__.py

echo "✅ Color coding module created successfully!"
echo "Run it with: python -m color_coding.main"

