"""
File parser.
"""

import json


SPEC_FILE = "spec.json"


class Spec(object):
    """
    Data format specification.
    """

    def __init__(self, spec_file=SPEC_FILE):
        with open(spec_file) as file:
            self._data = json.load(file)

    @property
    def column_names(self):
        return self._data["ColumnNames"]

    @property
    def offsets(self):
        return [int(k) for k in self._data["Offsets"]]

    @property
    def include_header(self):
        return bool(self._data["IncludeHeader"])

    # @staticmethod
    # def factory(spec_file=SPEC_FILE):
    #     with open(spec_file) as file:
    #         data = json.load(file)
    #     return Spec(data)
