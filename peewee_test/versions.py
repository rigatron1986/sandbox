# -*- coding: utf-8 -*-

"""
The purpose of this module is to implement the Version class. Example usage:

v1 = Version("12.0.01")
v2 = copy.deepcopy(v1)
v2.increment()
print v2.string
# 12.0.02

Note that comparisons have been defined correctly for these objects:

v3 = Version("2.0")
print v3 > v2
# False

print v3.string > v2.string
# True

"""

import os
from itertools import izip_longest



class StringNumberPair(object):
    """Holds a "string"/"number" pair. See description in Component"""

    def __init__(self, string, number):
        """"""
        super(StringNumberPair, self).__init__()
        self.string = string
        self.number = None if number is None else int(number)
        self.padding = 0 if number is None else len(number)

    def increment(self, default_padding=1):
        if self.number is None:
            self.number = 2  # if it's something that previously didn't have a digit at the end, start at 2
            self.padding = default_padding
        else:
            self.number += 1


class Component(object):
    """Holds a "component" of a version string.

    A component is viewed as a concatenation of non-digits (a "string") and digits (a "number").
    So "nuke_v9b6" is considered to be a concatenation of "nuke_v", 9, "b", 6.

    In the code, we're storing each pair of non-digits and digits in a StringNumberPair"""

    def __init__(self, string, separator):
        super(Component, self).__init__()

        self.string = string
        self.separator = separator
        self.string_number_pairs = []

        # populate the string_number_pair list
        self.breakdown()

    def breakdown(self):
        current_index = 0
        mode = "char"
        current_token = ""
        nondigits = []
        digits = []
        while True:
            if current_index >= len(self.string):
                current_char = ""
            else:
                current_char = self.string[current_index]
            if mode == "char":
                if current_char.isdigit() or current_char == "":
                    nondigits.append(current_token)
                    current_token = current_char
                    mode = "digit"
                else:
                    current_token += current_char
            else:
                if current_char.isdigit():
                    current_token += current_char
                else:
                    digits.append(current_token)
                    current_token = current_char
                    mode = "char"
            current_index += 1
            if current_index > len(self.string):
                break

        string_number_pairs = []
        for c, d in izip_longest(nondigits, digits):
            string_number_pairs.append(StringNumberPair(c, d))

        self.string_number_pairs = string_number_pairs

    def increment(self, default_padding):
        # TODO: Can there be no string_number_pairs?
        self.string_number_pairs[-1].increment(default_padding)


class Version(object):
    """An object that holds an arbitrarily constructed version number.

    We can break it down as follows:

    version_string = component+separator+component+...
    separator = ".", " ", "_", or ..., depending on what's given in init
    component = string_number_pair + string_number_pair"""

    def __init__(self, string, separators="."):
        """"""
        super(Version, self).__init__()

        self.string = string
        self.separators = separators

        # decompose the string into components and build a corresponding sort-structure
        self.breakdown()
        self.build_cmp_structure()

    def breakdown(self):
        separators = self.separators
        components = []
        string = self.string
        while True:
            best_index = len(string)
            best_separator = None
            for sep in separators:
                found_index = string.find(sep)
                if found_index >= 0 and (best_index is None or found_index < best_index):
                    best_index = found_index
                    best_separator = sep

            components.append(Component(string[:best_index], best_separator))
            if best_separator is None:
                break
            else:
                string = string[best_index + 1:]
        self.components = components

    def build_cmp_structure(self):
        cmp_structure = []
        for c in self.components:
            sort_components = []
            for p in c.string_number_pairs:
                sort_components.append(p.string.lower())  # NOTE: .lower() makes our comparisons case insensitive
                if p.number is not None:
                    sort_components.append(p.number)
            cmp_structure.append(sort_components)
            cmp_structure.append(c.separator)
        self.cmp_structure = cmp_structure

    def build_string(self):
        self.string = ""
        for c in self.components:
            for p in c.string_number_pairs:
                self.string += p.string
                if p.number is not None:
                    self.string += ("{0:0" + str(p.padding) + "}").format(p.number)
            if c.separator is not None:
                self.string += c.separator

    def increment(self, default_padding=1):
        # TODO: is there always at least one component?
        self.components[-1].increment(default_padding)

        # update the other structures
        self.build_string()
        self.build_cmp_structure()

    # for Python 2.6 we, have to define all 6 Rich Comparison operators
    def __lt__(self, other):
        return self.cmp_structure < other.cmp_structure

    def __le__(self, other):
        return self.cmp_structure <= other.cmp_structure

    def __eq__(self, other):
        return self.cmp_structure == other.cmp_structure

    def __ne__(self, other):
        return self.cmp_structure != other.cmp_structure

    def __gt__(self, other):
        return self.cmp_structure > other.cmp_structure

    def __ge__(self, other):
        return self.cmp_structure >= other.cmp_structure


def get_next_version_dir(parent_dir, starting_default="v001"):
    if not os.path.isdir(parent_dir):
        return starting_default

    any_dirs_found = False
    largest_dir = Version(starting_default)
    for entry in os.listdir(parent_dir):
        if os.path.isdir(os.path.join(parent_dir, entry)):
            v = Version(entry)
            if not any_dirs_found or v > largest_dir:
                largest_dir = v
                any_dirs_found = True

    while os.path.exists(os.path.join(parent_dir, largest_dir.string)):
        largest_dir.increment()

    return largest_dir.string


def get_latest_version_dir(parent_dir, starting_default="v001"):
    if not os.path.isdir(parent_dir):
        return starting_default

    any_dirs_found = False
    largest_dir = Version(starting_default)
    for entry in os.listdir(parent_dir):
        if os.path.isdir(os.path.join(parent_dir, entry)):
            v = Version(entry)
            if not any_dirs_found or v > largest_dir:
                largest_dir = v
                any_dirs_found = True

    return largest_dir.string
