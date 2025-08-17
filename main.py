from color_coding.translation import get_color_from_pair_number, get_pair_number_from_color
from color_coding.manual import generate_color_coding_manual


def main():
    print("Example lookups:")
    print("Pair 4 corresponds to:", get_color_from_pair_number(4))
    print("Color (Red, Slate) corresponds to pair:", get_pair_number_from_color("Red", "Slate"))

    print("\n" + generate_color_coding_manual())


if __name__ == "__main__":
    main()
