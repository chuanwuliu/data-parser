"""
Fix-width file generator
"""

import string
import random
from dataparser import DataParser


def random_string(k):
    """
    Create a string of k random characters including letters, digits and whitespace.
    :param k: length of string
    :return: generated random string
    """
    characters = string.ascii_letters + string.digits + ' '
    return ''.join(random.choices(characters, k=k))


def generate_line_full(offsets):
    line = ""
    for k in offsets:
        line += random_string(k)
    return line


def generate_line_left(offsets):
    line = ""
    for k in offsets:
        k1 = random.randint(a=0, b=k)
        k2 = k - k1
        line += random_string(k1) + " " * k2
    return line


def generate_line_right(offsets):
    line = ""
    for k in offsets:
        k1 = random.randint(a=0, b=k)
        k2 = k - k1
        line += " " * k1 + random_string(k2)
    return line


def generate_text(n, align='full'):
    """
    Generate a fixed width text of n lines.
    :param n: number of lines of the text
    :param align: alignment style ie. "full", "left" or "right"
    :return: generated text
    """
    f = {
        'full': generate_line_full,
        'left': generate_line_left,
        'right': generate_line_right
    }[align]
    dp = DataParser.factory()
    text = ""
    if dp.include_header is True:
        for i in range(len(dp.column_names)):
            width = dp.offsets[i]
            name = dp.column_names[i]
            if align == "right":
                text += ' ' * (width - len(name)) + name
            else:
                text += name  + ' ' * (width - len(name))
        text += '\n'
    for i in range(n - 1):
        text += f(dp.offsets) + '\n'
    text += f(dp.offsets)
    return text


# Generate fixed width files.
# Three files of different alignment styles will be generated in the tests folder.
if __name__ == "__main__":
    text = generate_text(n=5, align='full')
    with open('tests/temp1.txt', 'w') as file:
        file.write(text)
    text = generate_text(n=5, align='left')
    with open('tests/temp2.txt', 'w') as file:
        file.write(text)
    text = generate_text(n=5, align='right')
    with open('tests/temp3.txt', 'w') as file:
        file.write(text)
