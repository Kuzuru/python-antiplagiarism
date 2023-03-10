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
    def str_to_bool(value: str) -> bool:
        if value.lower() in {"false", "f", "0", "no", "n"}:
            return False
        elif value.lower() in {"true", "t", "1", "yes", "y"}:
            return True

        raise ValueError(f"{value} is not a valid boolean value")


class Antiplagiarism:
    def __init__(self):
        self.args = ArgsWorker()

    @staticmethod
    def get_code_syntax_tree(filename) -> str:
        with open(filename, "r") as f:
            code = f.read()

        node = ast.parse(code)

        # TODO: Replace the use of ast.dump() with something better
        normalized_code = ast.dump(node)

        return normalized_code

    @staticmethod
    def levenstein(str_1: str, str_2: str) -> int:
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

    # Reads and compares two files
    def read_and_compare(self, file_orig: str, file_copy: str) -> None:
        code_orig = self.get_code_syntax_tree(file_orig)
        code_copy = self.get_code_syntax_tree(file_copy)

        distance = self.levenstein(code_orig, code_copy)

        # - If distance == 0, the files are identical,
        # if the distance increases relative to 0,
        # they become more different
        # - So (distance / len(code_orig) is DIFFERENCE
        # and (1 - DIFFERENCE) is SIMILARITY
        similarity = 1 - (distance / len(code_orig))

        percent = similarity * 100
        formatted_percent = format(percent, ".1f") + "%"

        output = f"[ {file_orig} || {file_copy} ]\nLevenstein: {distance}\nSimilarity: {similarity}"
        output += f" (~ {formatted_percent})\n\n"

        # Print info on screen if verbose mode is on
        if self.args.get.verbose:
            if distance != 0 and len(code_orig) != 0:
                print(output)
            elif distance == 0 and len(code_orig) != 0:
                print(f"[ {file_orig} || {file_copy} ]\nFiles are identical\n\n")

        with open(self.args.get.scores_output, "a") as f:
            if distance != 0 and len(code_orig) != 0:
                f.write(output)
            elif distance == 0 and len(code_orig) != 0:
                f.write(f"[ {file_orig} || {file_copy} ]\nFiles are identical\n\n")

    # Reads and compares list of files
    def compare_inputs(self, input_list):
        with open(input_list, "r") as f:
            for line in f:
                filenames = line.strip().split()
                self.read_and_compare(filenames[0], filenames[1])


def main():
    apg = Antiplagiarism()
    apg.compare_inputs(apg.args.get.input_list)


if __name__ == "__main__":
    main()
