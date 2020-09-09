"""
Test cases
"""

from dataparser import DataParser, SPEC_FILE

dp = DataParser.factory(SPEC_FILE)


dp.parse("tests/test_input1.txt", "tests/temp_output1.txt", delimiter=',')
with open("tests/temp_output1.txt", 'r') as f:
    derived_output = f.read()
with open("tests/test_output1.txt", 'r') as f:
    expected_output = f.read()
assert derived_output == expected_output


print('All test passed!')