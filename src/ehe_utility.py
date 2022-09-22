#!/usr/bin/env python3
############################################################################
# Program:
#    ehe_utility
#
# Author:
#    Hunter Eidson / eeidson@hpcprdssh02
# Usage:
#    ehe_utility.py
#
# Version:
#    0.5
#
# Description:
#    Module file containing several functions that I've collected and grouped
#    together for easy use.
#
############################################################################
# @(#)ehe_utility.py     0.5 (Kennesaw State University) eeidson    23-Feb-2022
############################################################################
"""A set of utility functions that I'm collecting.  At some point I'll probably
   organize them better, once I have more, but for now, putting them in their
   own file is a start... :)"""
import sys

import humanize


def comma_fmt(number):
    """
    Function: comma_fmt

    Args: number to format with commas

    Returns: string
    """
    return f"{int(number):,}"


def size_fmt(number, binary=True):
    """
    Function: size_fmt

    Args:
        number: to format as a SI size
        binary: whether to use 10**3 or 2**10 definitions of suffixes

    Returns: string
    """
    return humanize.naturalsize(number, binary)


def list_to_string(alist, sep=", "):
    """Function to convert list to a formatted string

    Args:
        alist: list of items
        sep: seperator to place between list items

    Returns:
        A formatted string
    """
    # Create a format spec for each item in the input `alist`.
    # E.g., each item will be right-adjusted, field width=3.
    format_list = ["{:>1}" for item in alist]

    # Now join the format specs into a single string:
    # E.g., '{:>3}, {:>3}, {:>3}' if the input list has 3 items.
    my_str = sep.join(format_list)

    # Now unpack the input list `alist` into the format string. Done!
    return my_str.format(*alist)


def list_items_in_english(list_items, oxford_comma=True):
    """Produce a list of the items formatted as they would be in an
    English sentence.  So one item returns just the item, passing two
    items returns "item1 and item2" and three returns "item1, item2,
    and item3" with an optional Oxford comma.

    Originally From: https://stackoverflow.com/a/58692463/3168105

    Args:
        list_items: list of items to format
        oxford_comma: whether to use the oxford comma or not

    Returns:
        A formatted string
    """
    return ", ".join(
        list_items[:-2]
        + [
            ((oxford_comma and len(list_items) != 2) * "," + " and ").join(
                list_items[-2:]
            )
        ]
    )


def underline_string(
    text, border=None, position="below", newlines="neither", length=None
):
    """
    Function to underline text

     Args:
        text: string to underline
        border: list containing characters to underline below and above
                (in that order)
        position: Underline below, above, both, or neither
        newlines: Add a newline below, above, both, or neither
        length: Optional length of underline
    """
    if length is None:
        text_len = len(text)
    else:
        text_len = length

    position = position.lower()
    newlines = newlines.lower()
    if border is None:
        border = ["=", "="]

    if len(border) == 1:
        border = [border, border]

    if newlines in ("above", "both"):
        print("")
    if position in ("above", "both"):
        print(border[1] * text_len)
    print(text)
    if position in ("below", "both"):
        print(border[0] * text_len)
    if newlines in ("below", "both"):
        print("")


def make_ordinal(num):
    """
    Convert an integer into its ordinal representation::

     Args:
        num: Number to convert to ordinal representation

     Returns:
        String

     Examples:
        make_ordinal(0)   => '0th'
        make_ordinal(3)   => '3rd'
        make_ordinal(122) => '122nd'
        make_ordinal(213) => '213th'
    """
    num = int(num)
    if 11 <= (num % 100) <= 13:
        suffix = "th"
    else:
        suffix = ["th", "st", "nd", "rd", "th"][min(num % 10, 4)]
    return str(num) + suffix


def convert_nato(mytext):
    """
    Convert letters to NATO phonetic alphabet.

     Args:
        mytext: String to display using the NATO phonetic alphabet

     Returns:
        result: A list containing one string per character in the

    """
    letter_table = {
        "A": "Alpha",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliett",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "X-ray",
        "Y": "Yankee",
        "Z": "Zulu",
    }

    result = []
    for letter in mytext.upper():
        if letter.isdigit():
            result.append(f"{letter} as a number")
        elif letter.isalpha():
            result.append(f"{letter} as in {letter_table[letter]}")
        elif letter == "/":
            result.append("stroke")
        elif letter == "-":
            result.append("dash")
        else:
            result.append(f"(**) Not sure how to say {letter}")
    return result


def main():
    """Quick and dirty wrapper for this file"""
    index = 1
    underline_string("Demo of convert_nato...", border="#", newlines="below")
    arg_list = sys.argv[1:] if len(sys.argv) > 1 else ["Mailman"]
    for arg in arg_list:
        underline_string(f"  {make_ordinal(index)} Word  ", position="below")
        word_list = convert_nato(arg)
        for nato_word in word_list:
            print(nato_word)
        index += 1

    underline_string("Demo of comma_fmt...", border="#", newlines="both")
    print(f"{comma_fmt('1234') = }")
    print(f"{comma_fmt('234') = }")
    print(f"{comma_fmt('1234567890') = }")

    underline_string("Demo of size_fmt...", border="#", newlines="both")
    print(f"{size_fmt('1234') = }")
    print(f"{size_fmt('234') = }")
    print(f"{size_fmt('1234567890') = }")
    print(f"{size_fmt('1234', False) = }")
    print(f"{size_fmt('234', False) = }")
    print(f"{size_fmt('1234567890', False) = }")

    underline_string("Demo of list_items_in_english...", border="#", newlines="both")
    list_items = ["one", "two", "three", "four"]
    print(list_items_in_english(list_items[:1]))
    print(list_items_in_english(list_items[:2]))
    print(list_items_in_english(list_items[:3]))
    print(list_items_in_english(list_items))
    print(list_items_in_english(list_items, oxford_comma=False))


if __name__ == "__main__":
    main()
