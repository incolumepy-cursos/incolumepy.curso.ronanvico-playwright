# !/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
from tempfile import gettempdir
from rstr import rstr
from string import ascii_letters, digits

__author__ = "@britodfbr"  # pragma: no cover


def filegen(suffix: str = ''):
    suffix = suffix or 'txt'
    suffix = f".{suffix.lstrip('.')}"
    while True:
        filename = Path(gettempdir()).joinpath('move_files', rstr(ascii_letters+digits, 15)).with_suffix(suffix)
        filename.parent.mkdir(exist_ok=True, parents=True, mode=755)
        filename.write_text('')
        yield filename


def run():
    # print(rstr(ascii_letters, 10))
    fileg = filegen('csv')
    print(next(fileg))
    for _ in range(10):
        print(next(fileg))


if __name__ == '__main__':  # pragma: no cover
    run()
