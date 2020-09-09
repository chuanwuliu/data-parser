"""
File parser.
"""
import json

SPEC_FILE = "spec.json"


class DataParser(object):
    """
    Data format specification.
    """

    def __init__(self, spec):
        self._spec = spec

    @property
    def column_names(self):
        return self._spec["ColumnNames"]

    @property
    def offsets(self):
        return [int(k) for k in self._spec["Offsets"]]

    @property
    def include_header(self):
        return bool(self._spec["IncludeHeader"])

    def parse(self, input_file, output_file, delimiter=','):
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
    def factory(spec_file=SPEC_FILE):
        with open(spec_file) as file:
            spec = json.load(file)
        return DataParser(spec)


if __name__ == "__main__":
    import sys

    input_file, output_file = sys.argv[1:3]
    dp = DataParser.factory()
    dp.parse(input_file, output_file)
