#!/usr/bin/env python3

import sys
import csv
import re
from collections import defaultdict

import matplotlib.pyplot as plt

def get_row_columns(reader, columns_requested):
    column_names = next(reader)
    # print(f'Columns:\n{" | ".join(column_names)}', file=sys.stderr)
    column_is = []
    for name, i in zip(column_names, range(len(column_names))):
        if name in columns_requested:
            column_is.append(i)
    for row in reader:
        yield [row[i] for i in column_is]

def years(reader):
    years = (int(d[0].split('-')[0]) for d in get_row_columns(reader, ['Date of document']))
    year_sizes = defaultdict(int)
    for year in years:
        year_sizes[year] += 1
    year_sizes = list(year_sizes.items())
    year_sizes.sort()
    # print(year_sizes, file=sys.stderr)

    fig, ax = plt.subplots()

    years = [str(ys[0]) for ys in year_sizes]
    counts = [ys[1] for ys in year_sizes]

    ax.bar(years, counts)

    ax.set_ylabel('Number of documents')
    ax.set_title('Offical documents mentioning EUROTRA')
    ax.legend(title='Year')

    plt.show()

def languages(reader):
    rows = get_row_columns(reader, ['Date of document', 'Publication Reference'])
    langs = []
    for row in rows:
        year = row[0].split('-')[0]
        m = re.search('\(([^)]+)\)', row[1])
        if m is not None:
            year_langs = tuple(m.group(1).split(', '))
            langs.append((year, year_langs))
    langs = list(set(langs))
    langs.sort()
    for l in langs:
        print(l)

def language_speakers_eu_70s():
    pass # todo
        
with open('eurotra-search-results-20240328.csv', newline='') as f:
    reader = csv.reader(f)
    if sys.argv[1] == 'years':
        years(reader)
    elif sys.argv[1] == 'languages':
        languages(reader)
    else:
        print(f'error: unknown command {sys.argv[1]}', file=sys.stderr)
