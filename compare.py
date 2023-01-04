import argparse
import ast


class ArgsWorker:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Assessing the similarity of two Python scripts")

        parser.add_argument("input_list", type=str, help="Input file with list of files to compare")
        parser.add_argument("scores_output", type=str, help="Output file of the similarity estimation of program texts")

        parser.add_argument(
            "-v", "--verbose",
            type=self.str_to_bool,
            nargs="?",
            const=True,
            default=False,
            help="Verbose output"
        )

        # Uses to get arguments: args.get.input_list
        self.get = parser.parse_args()

    # Defines the string representation of the Boolean
    @staticmethod
    def str_to_bool(value) -> bool:
        if value.lower() in {"false", "f", "0", "no", "n"}:
            return False
        elif value.lower() in {"true", "t", "1", "yes", "y"}:
            return True

        raise ValueError(f"{value} is not a valid boolean value")


def get_code_syntax_tree(filename) -> str:
    with open(filename, "r") as f:
        code = f.read()

    node = ast.parse(code)

    # TODO: Replace the use of ast.dump() with something better
    normalized_code = ast.dump(node)

    return normalized_code


def levenstein(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)

    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n

        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]

            if str_1[j - 1] != str_2[i - 1]:
                change += 1

            current_row[j] = min(add, delete, change)

    return current_row[n]


def read_and_compare(file_orig, file_copy):
    code_orig = get_code_syntax_tree(file_orig)
    code_copy = get_code_syntax_tree(file_copy)

    # Calculate the Levenshtein distance between the two strings
    distance = 3  # TODO: levenstein(code_orig, code_copy)

    # Print the distance, or save it to a file if verbose output is disabled
    print(distance)


def main():
    args = ArgsWorker()

    with open(args.get.input_list, "r") as f:
        for line in f:
            filenames = line.strip().split()
            read_and_compare(filenames[0], filenames[1])


if __name__ == "__main__":
    main()
