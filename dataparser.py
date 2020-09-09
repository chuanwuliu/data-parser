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
        f_input = open(input_file, 'r')
        f_output = open(output_file, 'w')
        while(True):
            line = f_input.readline()
            if line == '':
                break
            else:
                filed_list = []
                j = 0
                for k in self.offsets:
                    filed_list += [line[j: j+k].strip()]
                    j += k
                line_parsed = delimiter.join(filed_list)
                line_parsed += '\n'
                f_output.write(line_parsed)
        f_input.close()
        f_output.close()


    @staticmethod
    def factory(spec_file=SPEC_FILE):
        with open(spec_file) as file:
            spec = json.load(file)
        return DataParser(spec)
