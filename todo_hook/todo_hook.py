#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from ansicolor import green, yellow
import re
import sys
import click

@click.command()
def cli():
    search = subprocess.check_output("ag -i -C 2 '// ?todo' | sed 's#\([^/]\)[^/: ]*/#\\1/#g'", shell=True)
    search_lines = search.split("\n")
    search_lines.pop()

    print("")

    if not len(search_lines):
        print(green("✓ No TODOs found!"))
        sys.exit(0)

    print(yellow("⚠ Be aware of these TODOs:"))
    todo_line_pattern = re.compile(".*// ?todo.*", re.IGNORECASE)
    for line in search_lines:
        if re.match(todo_line_pattern, line):
            print(green(line))
        else:
            print(line)

    print("")

if __name__ == '__main__':
    main()
