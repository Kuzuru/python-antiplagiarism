import argparse


# Defines the string representation of the Boolean
def str_to_bool(value):
    if value.lower() in {'false', 'f', '0', 'no', 'n'}:
        return False
    elif value.lower() in {'true', 't', '1', 'yes', 'y'}:
        return True

    raise ValueError(f'{value} is not a valid boolean value')


def parse_args():
    parser = argparse.ArgumentParser(description="Assessing the similarity of two Python scripts")

    parser.add_argument("input_list", type=str, help="Input file with list of files to compare")
    parser.add_argument("scores_output", type=str, help="Output file of the similarity estimation of program texts")

    parser.add_argument(
        "-v", "--verbose",
        type=str_to_bool,
        nargs='?',
        const=True,
        default=False,
        help="Verbose output"
    )

    return parser.parse_args()


def main():
    parse_args()


if __name__ == "__main__":
    main()
