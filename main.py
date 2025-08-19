# main
from tests import run_all_tests
from reference_manual import generate_reference_manual

if __name__ == "__main__":
    run_all_tests()
    print("\nReference Manual:\n")
    print(generate_reference_manual())
