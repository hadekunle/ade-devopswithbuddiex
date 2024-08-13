import re
import argparse


def is_valid_license(license_plate):
    # Check length: must be exactly 7 characters
    if len(license_plate) != 7:
        return False

    # Check the first character: must be a digit from 1 to 9
    if not license_plate[0].isdigit() or license_plate[0] == "0":
        return False

    # Check the second to fourth characters: must be capital letters (A-Z, except I and O)
    if not re.match(r"^[A-HJ-NP-Z]{3}$", license_plate[1:4]):
        return False

    # Check the fifth to seventh characters: must be digits and cannot be the same
    if not re.match(r"^[0-9]{3}$", license_plate[4:7]):
        return False

    if license_plate[4] == license_plate[5] == license_plate[6]:
        return False

    return True


def main(file_path):
    try:
        with open(file_path, "r") as file:
            license_plates = file.read().splitlines()

        results = {plate: is_valid_license(plate) for plate in license_plates}

        for plate, is_valid in results.items():
            print(f"{plate}: {'Valid' if is_valid else 'Invalid'}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate license plates from a file.")
    parser.add_argument(
        "file", type=str, help="The path to the file containing license plates."
    )
    args = parser.parse_args()

    main(args.file)
