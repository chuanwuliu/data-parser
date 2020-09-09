# Fixed width file data parser and generator

## Run the Code
   ### Prerequisites:
    * Python 3.6
    * Git
 
   ### Download the repo
   ```bash
   # Download the repo
   git clone https://github.com/chuanwuliu/data-parser.git
   ``` 
   ### Interfaces
   The main data parser function is defined in `dataparser.py`. To convert a fixed width input_file save the result to output_file
   ```bash
   python dataparser.py input_file output_file
   ```
For example, to parse the input file `tests/test_input1.txt` and save the result to `tests/_temp_output2.csv`
```bash
python dataparser.py tests/test_input1.txt tests/_temp_output2.csv
```

The default delimiter is comma, you can customised the delimiter using the `-d` argument. For example parser with `@`
```bash
python dataparser.py tests/test_input1.txt tests/_temp_output2.csv --d @
```

More details about the usage
```bash
usage: dataparser.py [-h] [-d DELIMITER] [-s SPEC_FILE] input_file output_file

positional arguments:
  input_file    Path to the input (fixed width) file
  output_file   Path to save the output

optional arguments:
  -h, --help    show this help message and exit
  -d DELIMITER  Delimiter for parsing the file
  -s SPEC_FILE  Path to specification (json) file
```

## Test Cases:
Run the test cases
```bash
python testcases.py
```

Following cases have been tested:
  * Parse input file with fully filled up fields 
  * Parse input file with left aligned fields and blank fields
  * Parse input file with right aligned fields and blank fields
  * Parse file with all blank fields
  
In above cases, fields only include letters, digits and pure whitespace character.
Fields with more complicated whitespaces such as `\t` and `\r` have not been considered and tested.

## Contact:
Charles Liu: dr.liuchuanwu@gmail.com
