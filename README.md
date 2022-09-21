<a id="ehe_utility"></a>

# ehe\_utility

A set of utility functions that I'm collecting.  At some point I'll probably
organize them better, once I have more, but for now, putting them in their
own file is a start... :)

<a id="ehe_utility.comma_fmt"></a>

#### comma\_fmt

```python
def comma_fmt(number)
```

Function: comma_fmt

Args: number to format with commas

Returns: string

<a id="ehe_utility.size_fmt"></a>

#### size\_fmt

```python
def size_fmt(number, binary=True)
```

Function: size_fmt

**Arguments**:

- `number` - to format as a SI size
- `binary` - whether to use 10**3 or 2**10 definitions of suffixes

- `Returns` - string

<a id="ehe_utility.list_to_string"></a>

#### list\_to\_string

```python
def list_to_string(alist, sep=", ")
```

Function to convert list to a formatted string

**Arguments**:

- `alist` - list of items
- `sep` - seperator to place between list items


**Returns**:

  A formatted string

<a id="ehe_utility.list_items_in_english"></a>

#### list\_items\_in\_english

```python
def list_items_in_english(list_items, oxford_comma=True)
```

Produce a list of the items formatted as they would be in an
English sentence.  So one item returns just the item, passing two
items returns "item1 and item2" and three returns "item1, item2,
and item3" with an optional Oxford comma.

**Arguments**:

- `list_items` - list of items to format
- `oxford_comma` - whether to use the oxford comma or not


**Returns**:

  A formatted string

<a id="ehe_utility.underline_string"></a>

#### underline\_string

```python
def underline_string(text,
                     border=None,
                     position="below",
                     newlines="neither",
                     length=None)
```

Function to underline text

**Arguments**:

- `text` - string to underline
- `border` - list containing characters to underline below and above
  (in that order)
- `position` - Underline below, above, both, or neither
- `newlines` - Add a newline below, above, both, or neither
- `length` - Optional length of underline

<a id="ehe_utility.make_ordinal"></a>

#### make\_ordinal

```python
def make_ordinal(num)
```

Convert an integer into its ordinal representation::

**Arguments**:

- `num` - Number to convert to ordinal representation


**Returns**:

  String


**Examples**:

  make_ordinal(0)   => '0th'
  make_ordinal(3)   => '3rd'
  make_ordinal(122) => '122nd'
  make_ordinal(213) => '213th'

<a id="ehe_utility.convert_nato"></a>

#### convert\_nato

```python
def convert_nato(mytext)
```

Convert letters to NATO phonetic alphabet.

**Arguments**:

- `mytext` - String to display using the NATO phonetic alphabet


**Returns**:

- `result` - A list containing one string per character in the

<a id="ehe_utility.main"></a>

#### main

```python
def main()
```

Quick and dirty wrapper for this file

<a id="__init__"></a>

# \_\_init\_\_

############################################################################
Program:
__init__

Author:
Hunter Eidson / eeidson@kennesaw.edu

Usage:
__init__.py <arg1> <arg2> ... <argN>

Version:
0.1

Description:


TODO Notes:
* Add internal tags for export control and other things as needed
############################################################################
@(#)__init__.py     0.1 (Kennesaw State University) eeidson    15-Sep-2022
############################################################################
