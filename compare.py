import argparse



class ArgsWorker:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Assessing the similarity of two Python scripts")

        parser.add_argument("input_list", type=str, help="Input file with list of files to compare")
        parser.add_argument("scores_output", type=str, help="Output file of the similarity estimation of program texts")

        parser.add_argument(
            "-v", "--verbose",
            type=self.str_to_bool,
            nargs='?',
            const=True,
            default=False,
            help="Verbose output"
        )

        # Uses to get arguments: args.get.input_list
        self.get = parser.parse_args()

    # Defines the string representation of the Boolean
    @staticmethod
    def str_to_bool(value) -> bool:
        if value.lower() in {'false', 'f', '0', 'no', 'n'}:
            return False
        elif value.lower() in {'true', 't', '1', 'yes', 'y'}:
            return True

        raise ValueError(f'{value} is not a valid boolean value')


def read_and_compare(file_orig, file_copy):
    print(f"Got files: {file_orig} and {file_copy}")


def main():
    args = ArgsWorker()

    with open(args.get.input_list, 'r') as f:
        for line in f:
            filenames = line.strip().split()
            read_and_compare(filenames[0], filenames[1])


if __name__ == "__main__":
    main()
