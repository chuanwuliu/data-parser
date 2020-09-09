"""
File parser.
"""

import json
from typing import Dict, List

SPEC_FILE = "spec.json"


class DataParser(object):
    """
    Data Parser class.
    """

    def __init__(self, spec: Dict) -> None:
        """
        Initializer with specification dictionary.
        """
        self._spec = spec

    @property
    def column_names(self) -> List[str]:
        return self._spec["ColumnNames"]

    @property
    def offsets(self) -> List[int]:
        return [int(k) for k in self._spec["Offsets"]]

    @property
    def include_header(self) -> bool:
        return bool(self._spec["IncludeHeader"])

    def parse(self, input_file: str, output_file: str, delimiter: str = ',') -> None:
        """
        Parse a fixed width file `input_file`, separate columns with the given delimiter and write
         the output to file `output_file`.
        :param input_file: path of fixed width file
        :param output_file: path for saving the output
        :param delimiter: delimiter, default ','
        :return: None
        """
        with open(input_file, 'r') as f:
            input_lines = f.readlines()
        parsed_text = ""
        for line in input_lines:
            j = 0
            fields = []
            for k in self.offsets:
                fields += [line[j: j + k].strip()]
                j += k
            parsed_text += delimiter.join(fields) + '\n'
        parsed_text = parsed_text[:-1]
        with open(output_file, 'w') as f:
            f.write(parsed_text)

    @staticmethod
    def factory(spec_file: str = SPEC_FILE) -> 'DataParser':
        """
        Create a DataParser object using the specification `spec_file`.
        :param spec_file: specification in json
        :return: DataParser object
        """
        with open(spec_file) as file:
            spec = json.load(file)
        return DataParser(spec)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Path to the input (fixed width) file')
    parser.add_argument('output_file', help='Path to save the output')
    parser.add_argument('-d', dest='delimiter', default=',', help='Delimiter for parsing the file')
    parser.add_argument('-s', dest='spec_file', help='Path to specification (json) file')
    args = parser.parse_args()
    if args.spec_file:
        dp = DataParser.factory(spec_file=args.spec_file)
    else:
        dp = DataParser.factory(spec_file=SPEC_FILE)
    dp.parse(args.input_file, args.output_file, delimiter=args.delimiter)
