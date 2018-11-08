#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import argparse

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
    names_dict = {}
    names_list = []
    with open(filename) as file:
        content = file.read()
        year = re.findall(r'Popularity\sin\s(\d\d\d\d)', content)
        ranked_names = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', content)

    for rank, male, female in ranked_names:
        names_dict[male] = rank
        names_dict[female] = rank
    names_list.append(year[0])
    [names_list.append(n + ' ' + r) for n, r in sorted(names_dict.items())]
    return names_list

def create_summary(names):
    year = names[0]
    names = '\n'.join(sorted(names)) + '\n'
    with open('babynames' + year + '.html.summary', 'w') as f:
        f.write(names)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--summaryfile', help='creates a summary file', action='store_true')
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    file_list = args.files

    for file in file_list:
        if args.summaryfile:
            create_summary(extract_names(file))
        else:
            print('\n'.join(sorted(extract_names(file))) + '\n')


if __name__ == '__main__':
    main()
