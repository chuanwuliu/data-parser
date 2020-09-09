"""
Test cases
"""

from dataparser import DataParser, SPEC_FILE

dp = DataParser.factory(SPEC_FILE)

print("Test file with full width fields", end='')
dp.parse("tests/test_input1.txt", "tests/_temp_output1.txt", delimiter=',')
with open("tests/_temp_output1.txt", 'r') as f:
    derived_output = f.read()
with open("tests/test_output1.txt", 'r') as f:
    expected_output = f.read()
assert derived_output == expected_output
print(" ==> passed!")

print("Test file with left aligned fields including blank fields", end='')
dp.parse("tests/test_input2.txt", "tests/_temp_output2.txt", delimiter=',')
with open("tests/_temp_output2.txt", 'r') as f:
    derived_output = f.read()
with open("tests/test_output2.txt", 'r') as f:
    expected_output = f.read()
assert derived_output == expected_output
print(" ==> passed!")

print("Test file with right aligned fields including blank fields", end='')
dp.parse("tests/test_input3.txt", "tests/_temp_output3.txt", delimiter=',')
with open("tests/_temp_output3.txt", 'r') as f:
    derived_output = f.read()
with open("tests/test_output3.txt", 'r') as f:
    expected_output = f.read()
assert derived_output == expected_output
print(" ==> passed!")

print("Test file with all blank fields", end='')
dp.parse("tests/test_input4.txt", "tests/_temp_output4.txt", delimiter=',')
with open("tests/_temp_output4.txt", 'r') as f:
    derived_output = f.read()
with open("tests/test_output4.txt", 'r') as f:
    expected_output = f.read()
assert derived_output == expected_output
print(" ==> passed!")
