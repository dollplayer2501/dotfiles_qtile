#!/usr/bin/env python3
"""
generate_toc.py
===============

`python3 scripts/create_ToC.py` at `./.config/qtile`

Read `./doc/*.md` and create ToC.
And rewrite the ToC of the following file:
  - ./README.md
  - ./doc/README.md

The first line of `./doc/*.md` must be `# title`!
"""

import sys
import os
import re
from pathlib import Path
import pprint


DOCS_DIR = Path(os.path.expanduser('~/.config/qtile/docs/'))
PLACEHOLDER_IN = "<!-- {{TOC-IN}} -->"
PLACEHOLDER_OUT = "<!-- {{TOC-OUT}} -->"


def main():

  #
  # Read ToC
  #

  md_files = list(DOCS_DIR.glob('*.md'))
  if not md_files:
    print('No markdown files found in `' + str(DOCS_DIR) + '`.')
    return
  md_files.sort()

  full_toc_dict = {}
  for md_file in md_files:
    if 'README' in md_file.name:
      continue

    text = None
    with open(md_file, 'r', encoding = 'utf-8') as f:
      text = f.readline()
      f.close()

    tmp1 = text.rstrip('\n')
    tmp2 = tmp1[2:]
    full_toc_dict[md_file.name] = tmp2

  #
  # Create link markdown
  #

  toc_str_docs_readme = toc_str_top_readme = ''
  for key, value in full_toc_dict.items():
    tmp1 = ''
    if '00' == key[3:5]:
      tmp1 = F'- [%s](%s)\n'
    else:
      tmp1 = F'  - [%s](%s)\n'

    toc_str_docs_readme += tmp1 % (
      value, './' + key
    )
    toc_str_top_readme += tmp1 % (
      value, './docs/' + key
    )

  #
  # Rewrite `./docs/README.md`
  #

  in_file = os.path.join(DOCS_DIR, 'README.md')
  with open(in_file, 'r', encoding = 'utf-8') as f:
    text = f.read()
    f.close()

  tmp1 = R'' + PLACEHOLDER_IN + '.*?' + PLACEHOLDER_OUT
  tmp2 = PLACEHOLDER_IN + '\n' + toc_str_docs_readme + PLACEHOLDER_OUT
  result = re.sub(
    tmp1, tmp2, text,
    flags = re.DOTALL
  )

  with open(in_file, 'w', encoding = 'utf-8') as f:
    f.write(result)
    f.close()

  #
  # Rewrite `./README.md`
  #

  in_file = os.path.join(DOCS_DIR, '../README.md')
  with open(in_file, 'r', encoding = 'utf-8') as f:
    text = f.read()
    f.close()

  tmp1 = R'' + PLACEHOLDER_IN + '.*?' + PLACEHOLDER_OUT
  tmp2 = PLACEHOLDER_IN + '\n' + \
    '- [README.md: Document top](./docs/README.md)' + '\n' + \
    toc_str_top_readme + \
    PLACEHOLDER_OUT
  result = re.sub(
    tmp1, tmp2, text,
    flags = re.DOTALL
  )

  in_file = os.path.join(DOCS_DIR, '../README.md')
  with open(in_file, 'w', encoding = 'utf-8') as f:
    f.write(result)
    f.close()


if __name__ == "__main__":
  main()


##
